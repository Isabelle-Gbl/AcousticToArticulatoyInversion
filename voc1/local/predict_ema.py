#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2022 Peter Wu
#  Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0)

"""
python3 local/predict_ema.py
"""
import numpy as np
import os
import s3prl.hub as hub
import soundfile as sf
import torch
import yaml

from tqdm import tqdm

from articulatory.utils import load_model


model_name = 'hubert_large_ll60k'
hubert_model = getattr(hub, model_name)() 
hubert_device = 'cpu'
hubert_model = hubert_model.to(hubert_device)
input_modality = 'hubert'

interp_factor = 4
hop_length = 80

inversion_checkpoint_path = "voc1/exp/my_model_h2/best_mel_ckpt.pkl" 
inversion_config_path = "voc1/exp/my_model_h2/config.yml" 

# load config
with open(inversion_config_path) as f:
    inversion_config = yaml.load(f, Loader=yaml.Loader)

inversion_device = torch.device("cpu")
inversion_model = load_model(inversion_checkpoint_path, inversion_config)
inversion_model.remove_weight_norm()
inversion_model = inversion_model.eval().to(inversion_device)

wav_d = 'voc1/data/input'
fs = os.listdir(wav_d)
fs = [f for f in fs if f.endswith('.wav')]

output_feats_d = 'voc1/data/output'
if not os.path.exists(output_feats_d):
    os.makedirs(output_feats_d)

with torch.no_grad():
    for f in tqdm(fs):
        p = os.path.join(wav_d, f)
        fid = f[:f.rfind('.')]
        output_art_path = os.path.join(output_feats_d, fid+'.npy')

        audio, sr = sf.read(p)
        wavs = [torch.from_numpy(audio).float().to(hubert_device)]
        states = hubert_model(wavs)["hidden_states"]
        feature = states[-1].squeeze(0)  # (seq_len, num_feats)
        target_length = len(feature)*interp_factor
        feature = torch.nn.functional.interpolate(feature.unsqueeze(0).transpose(1, 2), size=target_length, mode='linear', align_corners=False)
        feature = feature.transpose(1, 2).squeeze(0)  # (seq_len, num_feats)
        feat = feature.to(inversion_device)



        pred = inversion_model.inference(feat, normalize_before=False)
        np.save(output_art_path, pred.cpu().numpy())

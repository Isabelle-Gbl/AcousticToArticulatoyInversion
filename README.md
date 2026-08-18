 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧
                                                                                                     
                                            ....:+**+:..                                            
                                            ..:++***+=+....                                         
                                          ...:++******=*.....                                       
                                         ...:+=********=+:...                                       
                                         ..:*=**********++:..                                       
                                       ...-++************++:...                                     
                                       ..-++******+=******++:..                                     
                                     ...-++******=..=******=*:..                                    
                                  .....-*+******=....=******++-...                                  
                                  ....=++******=......-*******==...                                 
                                  ...==*******=........-*******+-....                               
                                  ..==*******-.... .....:******++-....                              
                               ....=+*******-.....    ...-*******+=...                              
                               ...=+*******:..        ....:+******-*..                              
                               ..+=*******:..         .....:*******=+...                            
                            ....+-*******:....           ...:*******+=..                            
                            ...+=*******:.....       .........+******++...                          
                            .:=+*******:....       ..:+*#*-....+******=*...                         
                          ...+=******+:..          .-%@@@@@+....+******=#..                         
                         ...#-******+:..............=@@@@@@#.....+******=+:..                       
                       ...:*=******+...+@@@@@@@@@@%=:*@@@@%-.   ..+******+=:..                      
                       ..-++******+..-%@@@@@@@@@@@@@+...:....   ...=******++:...                    
                       .-++******+..=%@@%+++%@@@@@@@*.....      ....=******+*:.....                 
                     ..:*+******=..=%@@%:..*@@@@@@@@*.          .....-******++-....                 
                  ....-*+******=..:@@@%...+@@@@@@@@@*.             ...=*******==...                 
                  ...-=*******=.. :%@@@=.=@@@@@@@@@@*.             ....:*******==..                 
                 ...+=*******=.....:-:.+@@@@@@@@@@@@*.             .....:******++=...               
                ...==*******-..   .....*@@@@@@@##@@@*.               ....:*******+=...              
                ..=+*******:...   ....*###@@@@%=*@@@*.                  ..:+******=+..              
              ...++*******:....   ...*@@@@%#*#+%@@@@*.                   ..:+******=+...            
            ....*=*******-....    .:*@@@@@@@@#-.*@@@*..            ..... ...:*******=+..            
            ...*-*******:...      .*@@@@*+%@@@%==%@@@+..        ....:++-......*******+=:...         
          ....++*******:....   ...#@@@@*..-%@@@@+:*%**@#:.........*@@@@@@=.....+******++...         
          ..:=+*******......  ...%@@@@+....:%@@@@=.....+%#-.....+@@@@@@@@@*.....+******=*:...       
          .:++******+:...   ...:#@@@@+.. ...:@@@@=.   ...=%#=.=%@@@@@@@@@@@%-....=******=*:...      
       ...:*=******+:....   ..:#@@@%=..  ...:@@@@=.     ..:#@@@@@@@@@@@@@@@@@+....=******++-...     
      ...:++******+......   .:#@@@%=...  ...:@@@@=.   ...-%@@@@@@@@@@@@@@@@@@@#:...=******++-..     
     ...-++******+....      :%@@@@=..    ...:@@@@=. ....#@@@@@@@@@@@@@@@@@@@@@@%=...-******++-..    
     ..-++******+.....      -@@@@-.        .:@@@@=....+@@@@@@@@@@@@@@@@@@@@@@@@@@*...-******+*-...  
   ...-++******=..........  -@@%-............%@@@=..-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:..-******++=... 
   ..-++******=..............:+-.............:*%@=:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*...-*******==.. 
   .-++******+----------------------------------=-==================================----+*******+=..
   .++*******************************************************************************************+-.
   .+=*******************************************************************************************+-.
   ..*=+***************************************************************************************===..
   ....:-=====================================================================================-:... 
                                                                                                    
  🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧 🚧 ⛔ 🚧 ⛔ 🚧 ⛔ 🚧
 # !! In Progress !!


# Articulatory Synthesis and Inversion
## Original AAI Code from:
Peter Wu (peterw1@berkeley.edu)
https://github.com/articulatory/articulatory

## This Adaption:
This repository has a lot of reductions from the original repository.
There could be probably more deleted, maybe this will happen later successive.



## Installation

## Speech-to-EMA

Here is a [link](https://drive.google.com/drive/folders/1O-1kX_ngHf1T8EN7HXWABCaEIJLNqxUI?usp=sharing) to the weights of an already-trained articulatory inversion model. Inputs to this model are 16 kHz waveforms and the first 12 dimensions of the outputs are EMA features (lower incisor x, y, upper lip x, y, lower lip x, y, tongue tip x, y, tongue body x, y, tongue dorsum x, y).

```bash
cd egs/ema/voc1
python3 local/predict_ema.py [model_dir] [input_wav_dir] [output_dir]
```

## Papers
respective paper from original repository: https://github.com/articulatory/articulatory

[**Deep Speech Synthesis from Articulatory Representations**](http://arxiv.org/abs/2209.06337)<br>
Interspeech 2022

```
@inproceedings{peter2022artsyn,
  title={Deep Speech Synthesis from Articulatory Representations},
  author={Wu, Peter and Watanabe, Shinji and Goldstein, Louis and Black, Alan W and Anumanchipalli, Gopala Krishna},
  booktitle={Interspeech},
  year={2022}
}
```

[**Speaker-Independent Acoustic-to-Articulatory Speech Inversion**](https://arxiv.org/abs/2302.06774)<br>
ICASSP 2023

```
@inproceedings{peter2023artinv,
  title={Speaker-Independent Acoustic-to-Articulatory Speech Inversion},
  author={Wu, Peter and Chen, Li-Wei and Cho, Cheol Jun and Watanabe, Shinji and Goldstein, Louis and Black, Alan W and Anumanchipalli, Gopala K},
  booktitle={ICASSP},
  year={2023}
}
```

[**Evidence of Vocal Tract Articulation in Self-Supervised Learning of Speech**](https://arxiv.org/abs/2210.11723)<br>
ICASSP 2023

```
@inproceedings{cho2023evidence,
  title={Evidence of Vocal Tract Articulation in Self-Supervised Learning of Speech},
  author={Cho, Cheol Jun and Wu, Peter and Mohamed, Abdelrahman and Anumanchipalli, Gopala K},
  booktitle={ICASSP},
  year={2023},
}
```

## Acknowledgements

Based on https://github.com/kan-bayashi/ParallelWaveGAN.

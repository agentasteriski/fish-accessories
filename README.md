# fish-accessories
tools for use with fish-diffusion


## tool list
1. gui-preprocess.py
2. gui-train.py
3. gui-inference.py

## 1. gui-preprocess.py
![image](https://user-images.githubusercontent.com/99069711/226149835-1dccd68a-c01e-4a1d-818f-5545c4c79ed9.png)

note: this is intended to be used to process dataset/train and dataset/valid SEPARATELY so you can disable augmentation on dataset/valid while leaving it on for the main data. 
## 2. gui-train.py
![image](https://user-images.githubusercontent.com/99069711/226150149-ce471813-a9e3-4e5c-a4e8-2282c8425c58.png)

notes: 
  - don't use select ckpt with the 'train from scratch' option
  - 'enable tensorboard' does nothing if you don't have tensorboard set up(which i don't know anything about, this was added by request and is still untested)
  - it doesn't report steps through the command line for some reason, just use wandb/tensorboard to check that (if you can't use either, it still gives that pickle error at every checkpoint)

## 3. gui-inference.py
![image](https://user-images.githubusercontent.com/99069711/234364136-478334a1-75c6-4b43-83d0-5de3ed14bb15.PNG)

notes:
  - for single-speaker models, leave the speaker set to 0.
  - variables currently unavailable are speaker_mapping and pitches_path due to question of use. if you would like to see these implemented, please let me know
## credits
[fish-diffusion](https://github.com/fishaudio/fish-diffusion) by @leng-yue

[diff-svc-gui](https://github.com/Kangarroar/diff-svc-GUI) by @kangarroar

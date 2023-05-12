# fish-accessories
tools for use with fish-diffusion. place in fish-diffusion-main and write significantly less command line!


## tool list
1. gui-preprocess.py
2. gui-train.py
3. gui-inference.py
OR the all-in-one
4. fishual.py

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
![image](https://github.com/agentasteriski/fish-accessories/assets/99069711/1af2db1c-eb3d-48c5-84a3-b8701988fdc5)

notes:
  - for single-speaker models, leave the speaker set to 0.
  - variables currently unavailable are speaker_mapping and pitches_path due to question of use. if you would like to see these implemented, please let me know

## 4. fishual.py
![image](https://github.com/agentasteriski/fish-accessories/assets/99069711/4aae6bc9-9717-4cce-94d4-33dce9c8a2cf) ![image](https://github.com/agentasteriski/fish-accessories/assets/99069711/c36e225c-ef76-4e84-9ec0-aa380c23d2bf) ![image](https://github.com/agentasteriski/fish-accessories/assets/99069711/7795c4af-fa7a-4e7d-a82b-b481aa92e956)

all of the above combined into one easy multi-tab GUI with cleaner layouts. recommended over the standalone versions.

## 5. fishual_alt.py
dark mode version of fishual.py. requires [sv-ttk](https://github.com/rdbende/Sun-Valley-ttk-theme). no functional difference. probably won't bother updating it.

## credits
[fish-diffusion](https://github.com/fishaudio/fish-diffusion) by @leng-yue

[diff-svc-gui](https://github.com/Kangarroar/diff-svc-GUI) by @kangarroar

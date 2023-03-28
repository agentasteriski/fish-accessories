# How to build your very own *Salmon Cannon*
###### (it launches Fish.)


## 1. Notepad
you have it. open it.

## 2. locate conda
where did you leave that thing anyways?
#### likely locations: 
C:\ProgramData\Anaconda3 
C:\ProgramData\miniconda3
C:\Users\\(username)\\.conda
if it's not in any of those places, idk what to tell you. good luck.

## 3. locate Fish

![hand pointing at group of koi](https://thumbs.dreamstime.com/z/finger-pointing-to-many-carp-koi-fish-swimming-water-asia-finger-pointing-to-many-carp-koi-fish-swimming-water-248837844.jpg)wow there they are

## 4. select your cannon
this just launches a python script. pick which one it launches. if you're using this with ~fish accessories\~, that would be either [gui-preprocess](gui-preprocess.py) or [gui-train](gui-train.py). you might also have kanga's inference gui, which was initially just `gui.py`, or my edit(superior, not broken in current versions) `gui2.py`.
## 5. build your cannon

it goes like this

    call <CONDA LOCATION>\condabin\conda_hook.bat
    call conda activate <CONDA ENV>
    python <FULL PATH TO GUI OF CHOICE>
put it in Notepad and save as .bat

## this is what a fully assembled Salmon Cannon looks like

    call C:\ProgramData\miniconda3\condabin\conda_hook.bat
    call conda activate fish
    python F:\fish-diffusion-main\gui-preprocess.py
my conda is at C:\ProgramData\miniconda3. my env is fish. my gui is in F:\fish-diffusion-main\. it preprocesses.
# Fish: launched
![salmon cannon.gif](http://cdn-0.drowningworms.com/wp-content/uploads/2014/08/Salmon-cannon3.gif)

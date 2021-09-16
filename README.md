# What this is?
This is essentially the voltaic progress sheet but implemented in Python's Dash library
# Why does this exist?
    - My progress sheet always broke for some unknwon reason so i decided to make my own
    - I don't want to manually enter scores so this reads all your scores for you
    - I just wanted to see if I could do it and wanted to better learn the dash data table so this was a learning experience
# Is this affiliated with voltaic?
No this is a solo endeavor and not meant to in anyway negatively affect voltaic I'm simply a fan making a spin off project
# Bugs
At the moment I'm the lone user and am unaware of any bugs

# How to use
### With Pipenv
Im assuming you have git installed on your machine and understand how to use it

Steps:

1.) Click on the green code button and copy the link in the popup that shows up
![alt text](/img/step_1.JPG)

2.) Open your command line or powershell and type: `git clone 'the thing you copied'` press enter
![alt text](/img/step_2.JPG)
    
3.) Move into the repo by typing `cd voltaic_progress_dash` in the command line

4.) Type `pipenv shell --python 3.7`

5.) Type `pipenv update`

7.) In the ./apps/data_handle.py file change the DIR variable to be the path to your scores for most people this will probably be `C:/Program Files (x86)/Steam/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats`

6.) Type `python index.py` Your screen should now look like this and the app will be running. 
![alt text](/img/step_6.JPG)

7.) Go to `http://127.0.0.1:8050/` in your browser and you should see this
![alt text](/img/step_7.JPG)

8.) Click on either Beginner or advanced and you should see the correct table
![alt text](/img/step_8.gif)
### Without Pipenv

TODO: Make this more straight forward
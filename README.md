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

# Assumptions for use
Im assuming you have git installed on your machine and python 3.8

# How to use

Steps:

1.) Click on the green code button and copy the link in the popup that shows up
![alt text](/img/step_1.JPG)

2.) Open your command line or powershell and type: `git clone 'the thing you copied'` press enter
![alt text](/img/step_2.JPG)
    
3.) Move into the repo by typing `cd voltaic_progress_dash` in the command line

4.) Type `pipenv shell --python 3.8`

5.) Type `pipenv update`

6.) Type `python index.py` Your screen should now look like this and the app will be running. 
![alt text](/img/step_6.JPG)

7.) Go to `http://127.0.0.1:8050/` in your browser and you should see this
![alt text](/img/step_7.JPG)

8.) Click on either Beginner or advanced and you should see the correct table
![alt text](/img/step_8.gif)
### Without Pipenv

Steps:

1.) Go to https://www.dropbox.com/s/87571gmupzf3qrj/main.zip?dl=0

2.) Download the zip

3.) Unzip it

4.) Go into the main folder and run volt_dash.exe

At this point you should see a command line and chrome should have force itself open. If everythong worked then the chrome tab should look like step 8
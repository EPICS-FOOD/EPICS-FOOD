# EPICS-FOOD
Amazon Registry Webscraper Bot, Incentivization Website

## What is in this repo?
### 1. ['Bot'](##Bot) Contains selenium code for bot to webscrape Amazon Registry, for more information, read Bot section of this read me on how to get started with it.
### 2. More stuff in the future to come hopefully :-)


## <ins>Bot</ins>

#### <ins>Getting Started</ins>
  This bot has been created using [<ins>Selenium</ins>](https://selenium-python.readthedocs.io/), please reference this documentation when working in this package! This page already contains an explination of how to get started with selenium on your own system, and there are many guides online.
  
##### Step 1
   Download Google Chrome to your system, and or update your current chrome version.
   Once this is done, figure out what version of Google Chrome you are running, top right, settings, help, 'about'
   Here is an example of how this should look:
   
   
   ![image](https://user-images.githubusercontent.com/43898891/230170642-f0cbcc58-402c-4590-a284-96cc1cadea1f.png)
   
   Notice that the current updated version in this image may be different than the one you are using now, no worries about this.
   
   

##### Step 2
   Download the correct webdriver for your system [here](https://chromedriver.chromium.org/downloads), current options MacOS, Linux, Windows

##### Step 3
   Git clone this repo, this step requires you to make sure Git is set up on your computer or that you know how to handle git. I followed this guide [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo), I decided to download Git Bash, and set up a P.A.T. (Personal Access Token). For long term usage, it would be wise to look into the git manager.
   
   After that, it should be as easy as:
    
    'git clone https://github.com/EPICS-FOOD/EPICS-FOOD.git'
   
   in your git bash or however else you manage your local repos.
   
##### Step 4
   Go to your local repo and navigate to the 'drivers' folder inside the bot folder. Here, you should place the driver you obtained in step 2.
    
   In my case, you will see that I was using the windows chrome driver, you can find it in the following place: 
   
    '~/bot/drivers/chromedriver_win32\chromedriver.exe'
    
   Note, that even if you are using windows this driver might not work for yours specifically. 
 
##### Step 5
  
   Open up the bot folder in your preferred IDE, I am using VSC which I recommend for this project, and locate the browser code in the 'main.py' file:
    
    browser = Browser('drivers\chromedriver_win32\chromedriver.exe')
    
   If your driver changed from the one that was previously in use, please string path to fit yours!
    
##### Step 6
 
   You will now also need to install selenium onto your current python,
    
   If you have correctly set up python, this should be as simple as going into your terminal and typing in the following:
    
    'pip install selenium'
    
   You can confirm this installation was successful by going into your python IDE and running
    
    >>> import selenium
    >>> print(selenium)
    
   Your IDE should output a path, once you see this, you are almost ready to go!
    
 ##### Step 7
 
   Run the main.py file and confirm that it is booting up correctly, once you see this, you are definitely done!
     
   Happy developing, keep in mind that all changes made in your local need to be:
     
     'git add .' 
     'git commit -m "insert message description" '
     'git push'
    
   Additionally, when we start pushing this code into a cloud service such as AWS (which is currently the plan) the drivers and code will again need to be changed.
     
   
  
    
    
 
  
#### Documentation
  
#### Bugs & Concerns
  -a
  -b
  -c

#### TODO:
  -a
  -b
  -c


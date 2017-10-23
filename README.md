# Android_appcrawl_from_google_play_store
Written in Python using web crawling of google play store to get app category



This project is to address below real life problem. Please note that data given is just sample. Real data cannot be shared. Real data is also large in volume.

Problem Statement: An organization wants to do campaign for different kinds of customers. They like to know the usage of what kind of mobile app customer is using. There is an app to collect information from customer device. It captures actual package name of the application. However, every application is of different category - like song, education, game etc. It is know which type of application customer is using most to understand the behaviour. It is limited to only Android app for the time being and only to Google Play store app.

Data file: Sample data file contains app package name

Solution: Program is written in Python and to crawl google play store web to get the category. Program can be modified to fetch other attribute as well.

Prerequisite:

You need to have Python installed version 3.5 or above and environment setup properly
You need to have BeautifulSoup and request package installed 
Usage: It is written and tested for Windows 7 OS. It should run in other environment also, but not tested. May be little bit changes are required as per demand of that OS. Please keep data file in same folder where source program is located. Data file is without any header. From command line following command should be executed.

python getAppCategory.py

Output: It will generate a "|" separated file, "appresults.csv" in same folder where datafile and source program are located. Output file will have three fields separated with comma. Fields are as below

app package name
app user friendly name
app category

************ Enjoy and don't forget to give credit if it helps ****************

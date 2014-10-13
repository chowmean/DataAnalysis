DataAnalysis
============

Twitter data analysis, location plotting, suggestion extraction and Time line generations from rss feeds. 


It requires few minutes to configure.All details are mentioned here.
For any assistance drop a mail i would love to help. :)
Pre-requisite.:
1. Linux
2. Python 2.7 or above
3. Libraries : sudo apt-get install python-requests
sudo apt-get install python-oauth2
sudo apt-get install python-textblob
sudo apt-get install python-geopy
There may be few more libraries requireed according to your base system config.
4. An apache server.
5. Active net connections for geopy and maps
You may have to change just few lines to run these code in your windows. Server files will work perfectly in windows server.
Instructions to use:
#####################
1. For getting tweets run the searching.py file in data exraction folder/tweets by replacing the costumer keys of your twitter api keys.
2. Change the file to save the tweets in different folder it is located in last 2 3 lines.
3. Run the python programs using in terminal to get the tweets.
4. Now move to every folder you extaracted and run the test file located in and paste the cleanansanalyze.py in there and run the file in the folder. it will clean and make a 3 new files location.json, results.json and suggestion.json. This is you required data. Put the files along with the folder in the server data_analysis directory and located in server files and you will get the results in webpage on refreshing.
5. For RSS feeds.RUn the Execute.py file in the readfeeder directory.
6. then run noun_filter and then timeline.py , it will create a folder named datastore. replace this datastore in folder server/live to get the data displayed in the web page on refreshing.
Running python program in terminal
>> python filename.py


## Author:chowmean
## Mail: gaurav.dev.iiitm@gmail.com
## Contributors: Gaurav Yadav(chowmean), Abhishek Kumar Yadav(manofsteel), Mohammad Afjal.
## Twitter and rss data analysis.
## Libraires used : Textblob, nltk, collections, re, json, oauth2, requests, etc.
## github: https://github.com/chowmean/DataAnalysis.git can fork from here.

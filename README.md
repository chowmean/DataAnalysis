DataAnalysis
============

Twitter data analysis, location plotting, suggestion extraction and Time line generations from rss feeds. 


It requires few minutes to configure.All details are mentioned here.
For any assistance drop a mail i would love to help. :)
Pre-requisites.
1. Linux.<br>
2. Python 2.7 or above.<br>
3. Libraries : sudo apt-get install python-requests.<br>
sudo apt-get install python-oauth2.<br>
sudo apt-get install python-textblob.<br>
sudo apt-get install python-geopy.<br>
There may be few more libraries requireed according to your base system config.<br>
4. An apache server.<br>
5. Active net connections for geopy and maps.<br>
You may have to change just few lines to run these code in your windows. Server files will work perfectly in windows. server.<br>

##Instructions to use:

1. For getting tweets run the searching.py file in data exraction folder/tweets by replacing the costumer keys of your twitter api keys.
2. Change the file to save the tweets in different folder it is located in last 2 3 lines.
3. Run the python programs using in terminal to get the tweets.
4. Now move to every folder you extaracted and run the test file located in and paste the cleanansanalyze.py in there and run the file in the folder. it will clean and make a 3 new files location.json, results.json and suggestion.json. This is you required data. Put the files along with the folder in the server data_analysis directory and located in server files and you will get the results in webpage on refreshing.
5. For RSS feeds.RUn the Execute.py file in the readfeeder directory.
6. then run noun_filter and then timeline.py , it will create a folder named datastore. replace this datastore in folder server/live to get the data displayed in the web page on refreshing.<br>
Running python program in terminal
<br>>> python filename.py


_Author:chowmean_ <br>
_Mail: gaurav.dev.iiitm@gmail.com_<br>
_Contributors: Gaurav Yadav(chowmean), Abhishek Kumar Yadav(manofsteel), Mohammad Afjal._<br>
_Twitter and rss data analysis._<br>
_Libraires used : Textblob, nltk, collections, re, json, oauth2, requests, etc._<br>
_github: https://github.com/chowmean/DataAnalysis.git can fork from here._<br>

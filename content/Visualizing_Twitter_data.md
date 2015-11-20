Title: Visualizing Twitter data
Date: 2014-08-22 00:16
Tags: python, data-science
Summary: Ferguson was big at the time of writing. I scoured Twitter for favorite words describing Ferguson

Data visualization is awesome. Who doesn't enjoy looking at cool graphs of various data? 

I decided to capitalize on the recent events in Ferguson, MO and practice my data crunching skills by looking at patterns in words used in tweets. I am still fairly new to the data science field so this was an exercise to get my feet wet. 

## Keywords are easy

I began with simple keyword searches. I was watching Jurassic Park and it was late so I did not want to stretch my brain further than it was capable. 

After watching the Twitter feed for `#Ferguson` for some time I decided on a few words that seemed to come up often or that seemed relevant. 

```
white
racist
ftp
tear gas
rifle
camera
milk
loot
```
Yes lots of other words are missing such as `black` but this was good enough to get a feel for what I was doing. 

In order to interact with Twitter I used a Python module called `tweepy`. `tweepy` seems to be one of the more popular choices by Pythonistas and it is easy to use. 

`tweepy` provides a class for listening to Twitter streams. This allows for real time monitoring of whatever keywords your heart desires. Using it is as simple as creating a subclass of `tweepy.StreamListener` and carrying out the desired behavior when a tweet is seen. I wanted it to count the total number of tweets seen and the count of each word as it is seen. 

This is the result.

<script src="https://gist.github.com/ThaWeatherman/9a2151fcf23bf66844d0/fe2dcfe9904f527121956c8c7cb0e948c76d1694.js"></script>

It is by no means elegant (remember, the velociraptors were hunting everyone at this point), but it does the job. A cleaner solution would have contained the keywords in a list and had a dictionary to track the counts. Printing would have been cleaner this way as well. 

The script itself is simple. When a tweet is seen it checks for the desired words and if a word is found that word's count is incremented. Then the total counts are printed for viewing. 

I let this script run for 12 hours and the final result was the following. 

```
----------GOT A TWEET-----------
total is 314259
number with 'racist' is 2933
number with 'white' is 10230
number with 'ftp' is 624
number with 'tear gas' is 2207
number with 'rifle' is 1140
number with 'camera' is 1735
number with 'milk' is 569
number with 'loot' is 2508
--------------------------------
```
Not a bad first attempt! But I can do better than just keyword searches. 

## Track all the words!

It is more interesting to see which words _actually_ appear the most rather than guessing which ones _might_ appear the most. 

Instead of tracking keywords we have our custom stream listener store a dictionary mapping words to the number of times they appear in tweets. We do not want to track words like "the" or "an" so we make sure to filter those out. We also do not want to track URLs for this specific experiment so we filter those out as well. However it would be interesting to look at which links are shared the most in a different experiment. Finally we filter out usernames. 

Since the stream is constantly running we need a way to save the data. Ideally we would save the data every minute or so, but for now saving it when the script stops running is good enough. 

The final result is the following. 

<script src="https://gist.github.com/ThaWeatherman/9a2151fcf23bf66844d0.js?file=analyze.py"></script>

Note that since everything is stored in memory you should not let this script run for more than a few hours unless you have a lot of memory to work with.

Having all of this data is cool, but visualizations are even more cool. I decided to use word clouds to give an idea of which words appear the most frequently. 

I began with a 15 minute test run of the script. Unfortunately I do not have the total number of tweets seen, but the result is about what you would expect. 

![15 minute run](/content/images/2014/Aug/example_cloud.png)

Some words I did not expect showed up such as "nacional" (is that a word?), "livingblessed", and "mirror". Either way it worked so now it was time to do a longer run.

### The final result

Because of the dataset size and file size limits on the web services I used for making the word clouds I only let it run for two hours. The final JSON file was about 1.1 MB, and after converting it to a giant block of text for feeding to the word cloud generators it was ~5.2 MB. This was too large so I ignored words with counts less than 10 and removed "ferguson", bringing the size down to ~4.2 MB. In total the script saw 64845 tweets. 

This one is from [Wordle](http://www.wordle.net/create).
![wordle final](/content/images/2014/Aug/final_cloud.png)

This one is from [Jason Davies](http://www.jasondavies.com/wordcloud/#%2F%2Fwww.jasondavies.com%2Fwordtree%2Fcat-in-the-hat.txt).
![tag crowd final](/content/images/2014/Aug/download.png)

I also used [Tag Crowd](http://tagcrowd.com/), but I liked these two the best with Wordle being my favorite. 

The words are pretty much the same as those from the 15 minute run. 

From this data we can see the general feeling towards the events in Ferguson and we can gain an understanding of the most talked about events or people. Data analysis helps open the door to understanding the big picture and this simple word analysis in only the beginning!

#### Materials used

- pip
- tweepy
- virtualenv
- Python 2.7.5
- Wordle

See all of it [here on Github](https://gist.github.com/ThaWeatherman/9a2151fcf23bf66844d0). 

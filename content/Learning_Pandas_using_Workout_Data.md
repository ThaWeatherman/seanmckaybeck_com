Title: Learning Pandas using Workout Data
Date: 2014-08-22 22:12
Tags: python, data-science
Summary: An intro to Python Pandas

### Introduction

`pandas` is a data analysis library for Python. It is extremely useful and fairly straightforward to work with. To see how simple it is we will look at some of my lifting data using `pandas` and graph it using `matplotlib`. 

## Read it in

The data is saved in a CSV which `pandas` can easily load and manipulate. Let's begin.

```
from pandas import read_csv

df = read_csv('stronglifts.csv')
print df.columns
'''
This prints - 

Index([u'Date', u'Note', u'Workout', u'Body Weight', u'Exercise 1', u'Weight (KG)', u'Weight (LB)', u'Set 1', u'Set 2', u'Set 3', u'Set 4', u'Set 5', u'Exercise 2', u'Weight (KG).1', u'Weight (LB).1', u'Set 1.1', u'Set 2.1', u'Set 3.1', u'Set 4.1', u'Set 5.1', u'Exercise 3', u'Weight (KG).2', u'Weight (LB).2', u'Set 1.2', u'Set 2.2', u'Set 3.2', u'Set 4.2', u'Set 5.2'], dtype='object')
'''
```
That was easy! No special iterative reading of rows and columns required. Pandas takes the CSV and loads it for you into the pandas' `DataFrame` object. The DataFrame is what you will more than likely use the most when using pandas. 

## Work with the data

This workout data is specific to the [Stronglifts 5x5](http://stronglifts.com/5x5) lifting routine which uses bench press, squats, overhead press, deadlift, and barbell row in its workouts. The `Exercise 2` column will either be "Bench press" or "Overhead press" and the `Exercise 3` column will either be "Deadlift" or "Barbell row". In order to play with the information on a per-lift basis we need to extract it into lists. 

```
>>> from dateutil import parser
>>> import datetime
>>> squat = []
>>> overhead = []
>>> bench = []
>>> barbell = []
>>> deadlift = []
>>> for idx, row in df.iterrows():
...     date = parser.parse(row['Date'])
...     date = date.strftime('%Y-%m-%d')
...     date = datetime.datetime.strptime(date, '%Y-%m-%d')
...     val = df.iloc[idx, 6]
...     squat.append((date, val))
...     val = df.iloc[idx, 14]
...     if row['Exercise 2'] == 'Overhead press':
...             overhead.append((date, val))
...     else:
...             bench.append((date, val))
...     val = df.iloc[idx, 22]
...     if row['Exercise 3'] == 'Deadlift':
...             deadlift.append((date, val))
...     else:
...             barbell.append((date, val))
...
```
Now that the data is organized into lists of tuples we can do whatever we like with it! In this case I will make a graph showing my progress in each of the lifts. 

## Graph it

To test the code I will only graph my squat data. 

```
>>> from matplotlib import pyplot as plt
>>> from matplotlib.dates import date2num
>>> x = [date2num(date) for (date, val) in squat]
>>> y = [val for (date, val) in squat]
>>> fig = plt.figure()
>>> graph = fig.add_subplot(111)
>>> graph.plot(x, y, 'r-o')
>>> graph.set_xticks(x)
>>> graph.set_xticklabels([date.strftime('%Y-%m-%d') for (date, val) in squat])
>>> fig.autofmt_xdate()
>>> plt.savefig('myplot.png')
```

That produces the following. 

![squat graph](/content/images/2014/Aug/myplot.png)

Following the same process we can graph all of the lift data. 

```
>>> from matplotlib import pyplot as plt
>>> from matplotlib.dates import date2num
>>> from matplotlib import rc
>>>
>>> rc('xtick', labelsize=8)
>>> fig = plt.figure()
>>> x = [date2num(date) for (date, val) in squat]
>>> y = [val for (date, val) in squat]
>>> graph = fig.add_subplot(111)
>>> graph.plot(x, y, 'r-o', label='squat')
>>> graph.set_xticks(x)
>>> graph.set_xticklabels([date.strftime('%Y-%m-%d') for (date, val) in squat])
>>> fig.autofmt_xdate()
>>>
>>> x = [date2num(date) for (date, val) in bench]
>>> y = [val for (date, val) in bench]
>>> graph = fig.add_subplot(111)
>>> graph.plot(x, y, 'b-o', label='bench')
>>>
>>> x = [date2num(date) for (date, val) in overhead]
>>> y = [val for (date, val) in overhead]
>>> graph = fig.add_subplot(111)
>>> graph.plot(x, y, 'g-o', label='overhead')
>>>
>>> x = [date2num(date) for (date, val) in barbell]
>>> y = [val for (date, val) in barbell]
>>> graph = fig.add_subplot(111)
>>> graph.plot(x, y, 'y-o', label='barbell')
>>>
>>> x = [date2num(date) for (date, val) in deadlift]
>>> y = [val for (date, val) in deadlift]
>>> graph = fig.add_subplot(111)
>>> graph.plot(x, y, 'c-o', label='deadlift')
>>>
>>> plt.legend(loc='upper left')
>>> plt.savefig('myplot_all.png')
```

![everything](/content/images/2014/Aug/myplot_all.png)

Since I squat every time I lift I could use its date values for the x axis and never have to reconfigure it to use different dates for the other lifts. `matplotlib` handles all of the graph construction for us, making visualization much easier.

Now we have a nice visualization of the data! There are plenty of other things I could do with the data, but this is intended to be introductory. `pandas` makes working with CSVs simple so we can focus on wrangling our data. 

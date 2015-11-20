Title: Zapping Rachel
Date: 2014-08-17 04:20
Tags: python, data-science, defcon
Summary: I took second at a contest at Defcon. This is my solution

I went to DEF CON for the first time about a week ago and I must say it was quite enjoyable. There were all sorts of things to participate in. One of these things was a contest put on by the FTC called [Zapping Rachel](http://www.ftc.gov/zapping-rachel). The contest focused on the problems and annoyances caused by robocalls and aimed to find ways to address the issue. Contestants could create a honey pot for robocalls, find vulnerabilities in the honey pots, or analyze a data set and determine whether or not each phone call was a robocall. I decided to analyze data as I wanted to use the `pandas` Python module for something but have not had any large data sets to work with. 

The FTC provided two datasets: one an example and the other to analyze. The data only contained the time of the phone call, the caller, and the receiver. Yes that sucks but if you think about it there really is not anything else to go off of in a situation like this. 

I ended up coming in second place. 61 people signed up for this phase, and I have no idea how many people submitted something, but I came in second and won some money which paid for the whole trip. So thaat's awesome. Here is how I did it.

## The Solution

If you just want to look at the data and my code [please feel free](https://github.com/ThaWeatherman/zapping_rachel_3_solution). In hindsight the best thing to do would have been to use some sort of machine learning. But I do not know anything about that so I winged it.

It was a lot of data to go through but I found two general trends. Between 4 AM and noon there were a very, very small number of robocalls. Also, if a number called more than five people it was probably a robot. I separated the data from the example set into robocalls and normal calls (this was provided) and found general trends. But each trend had exceptions. Most people in the normal set only called one number, but there were some robots who only called one number. Most robots called more than five numbers, but there were some people who did this too. Area codes were unhelpful. It really boiled down to my two general trends (even though the latter had a few exceptions). 

So I only filtered based on time of call being between 4 AM and noon and calls to greater than five numbers. I guarantee I missed a lot of robots and also qualified a few humans as robots, but I got the points I needed. At this point I wanted to go pick locks so I strategized based on the [contest rules](http://www.ftc.gov/zapping-rachel/rules). I wanted maximum points gained while losing very few and this was the best approach. 

## Conclusion

I submitted my hack answer and went on with life, only to be surprised with the email stating I actually did well. Unfortunately I have only been able to find one other person's solution online. See it [here](https://github.com/y4n9squared/defcon). Basically it is something complex and intelligent.

I would like to set up a honey pot for robocalls and help with this problem. No one should have to deal with robots on the phone. It's bad enough we have to go through the crappy robot menus when calling any and every store now. If you get a robot call **from someone other than a charity** make sure to report the number. Together we can stop the rise of the machines!

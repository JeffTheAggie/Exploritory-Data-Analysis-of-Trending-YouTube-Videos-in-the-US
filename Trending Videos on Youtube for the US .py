#!/usr/bin/env python
# coding: utf-8

# # Exploritory Analysis of Trending YouTube Videos in the US

# In this project, we will discover what categories affect the viewrship of the most trending YouTube videos in the US. What we can gain from analyzing these categories would be that we can improve recommending different types of videos to other people based on the majority opinion of what genres of videos are perceived as worthwhile to watch.

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
#Storing the csv files of the trending youtube videos from the US as a variable
USvideos_data = pd.read_csv("USvideos.csv")
USvideos_data


# In[3]:


Videos_In_US = USvideos_data.drop_duplicates(subset = "title", keep = "first")


# In[4]:


#Organizing the most trending US Videos by views
Videos_In_US.sort_values(by = "views", ascending = False)


# We are now going to analyze the top 10 most viewed YouTube Videos in the US and we're going to see what common group(s) of generes have put these videos in a very high percentile in terms of viewership.

# In[5]:


#Top 10 Most Watched Videos from the 2017-2018 Period
Videos_In_US_Top_10 = Videos_In_US.nlargest(10, "views")


# In[6]:


Videos_In_US_Top_10.head()


# In[12]:


#Plot of the Number of Views from the Top 10 Most Watched Videos from the 2017-2018 Period
plt.figure(figsize=(13, 7), dpi=200)
plt.bar(Videos_In_US_Top_10["title"],Videos_In_US_Top_10["views"])
plt.xticks(rotation=90)
plt.ylabel("views")
plt.title("Amount of Views for the Top 10 YouTube Videos")
plt.show()


# From the bar graph from above, we can see that the top 10 most viewed videos in the US tend to be in the genres of music videos and superhero films (for example, "Marvel Studios' Avengers: Infinity War Official Trailer" and "VENOM - Official Trailer(HD)"). The only videos that seem to be the exception of the rule in this trend would be "YouTube Rewind: The Shape of 2017|#YouTubeRewind" and "Sanju|Official|Trailer|Ranbir Kapoor|Rajkumar Hirani|Releasing on 29th June" since Youtube's 2017 Rewind is simply a compulation of popular YouTube channels/videos from that year and the Sanju film is a biographical film about the actor Sanjay Dutt. 

# In[9]:


#Observing the differences of the number of likes, dislikes, and comments of trending videos in the US
number_of_likes = sns.jointplot(x = "views", y = "likes", data = Videos_In_US, kind = "reg")
number_of_likes.annotate(stats.pearsonr)
number_of_comments = sns.jointplot(x = "views", y = "comment_count", data = Videos_In_US, kind = "reg")
number_of_comments.annotate(stats.pearsonr)
number_of_dislikes = sns.jointplot(x = "views", y = "dislikes", data = Videos_In_US, kind = "reg")
number_of_dislikes.annotate(stats.pearsonr)
plt.figure(figsize = (16, 9), dpi = 200)
plt.show()


# For the three graphs, we can see that the one thing that they have in common is that they all have fairly weak positive linear relatioships since a fair amount of points tend to be scattered away from the line of best fit, but a large portion of the points are very close to the line of best fit. However, the differences that I have seen in each graph would be that the graph that focuses on the number of likes in each trending video shows a trend in which as the videos increase in the amount of views that they have, there's an increase in the amount of likes that it will have (we really start to see this consistent level of growth around 5,000,000 views, reaches it's peak at 40,000,000 views with 4,000,000 likes, and then declines right after that); the graph with the number of comments has a similar style of growth as the graph with the number of likes, but the difference between the two is that the graph with the number of comments has a much larger dispersion of data points from the best line of fit at around 2,000,000 views and reaches it's max comment count at 15,000,000 views with around 720,000 comments; the graph with the number of dislikes is the most different out of the three graphs in which it reaches it's maximum peak on its perspective y axis very early at 15,000,000 views with 600,000 dislikes and after that point, there's a consistent increase in dislikes as the views increase, but the majority of those dislikes are under 100,000 dislikes. Based on these observations, we can safely conclude that as the more popular a video gets in viewership, the more likes and commentary that the video will receive; and as the least popular a video gets in viewership, the more dislikes that the video will receive.

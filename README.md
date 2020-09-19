# Data

A collection of data science practice in no particular order.

This project began with the merging of pre-scraped datasets relating to the most popular Google play store apps. An updated version of this dataset is available from https://www.kaggle.com/lava18/google-play-store-apps/data, though for this practice an unmodified dataset was available from Pluralsight's online learning platform.     Datasheets were combined using VLOOKUP, INDEX & MATCH functions. Some descriptive statistics were then generated using SUM, ROUNDAVERAGE, & COUNTIF functions; these yielded average ratings, total reviews, the average number of reviews per app, & the total number of free & paid apps in the dataset. 

This was followed by a small project utilyzing PowerQuery to import car sales data from several sources into one sheet. I then returned to the play store dataset, transformed date of last update into an integer & generated descriptive statistics for time since last update, number of reviews, & total downloads. Generating descriptive statistics with excels's analysis toolkit revealed incredibly high levels of kurtosis, with visual inspection of histograms suggesting a highly uneven distribution. For practice purposes a regression was conducted anyway, using Total Downloads as a DV and Time since Update & Number of Reviews as independent variables. This predictably yielded nonsense.  

Recently I've been experimenting with Python, especially Numpy & Pandas.

  






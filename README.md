# Data

A collection of data science projects, in order to develop proficiency.

This project began with the merging of pre-scraped datasets relating to the most popular Google play store apps. An updated version of this dataset is available from https://www.kaggle.com/lava18/google-play-store-apps/data, though for this practice an unmodified dataset was available from Pluralsight's online learning platform.        

To begin with datasheets were combined using VLOOKUP, INDEX & MATCH functions. Some descriptive statistics were then generated using   SUM, ROUNDAVERAGE, & COUNTIF functions; these yielded average ratings, total reviews, the average number of reviews per app, & the total number of free & paid apps in the dataset. 

This was followed by a small project utilyzing PowerQuery to import car sales data from several sources into one sheet. I then returned to the play store dataset, transformed date of last update into an integer, & generated descriptive statistics for time since last update, number of reviews, & total downloads. Generating descriptive statistics with excels's analysis toolkit revealed incredibly high levels of kurtosis, with visual inspection of histograms suggesting a highly uneven distribution. For practice purposes a multivariate regression was conducted anyway, using total downloads as a DV and time since update & number of reviews as independent variables.  

Somewhat predictably for a non-parametric sample simply jammed into an OLS regression, no p-value in the regression model was greater than 0.85 (!), with relationships between data therefore indistinguishable from chance occurence. As such this model provides little predictive value when trying to identify factors related to the total number of installs. 







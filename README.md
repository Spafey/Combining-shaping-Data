# Data

A collection of data science projects, in order to develop proficiency.

This project began with the merging of pre-scraped datasets relating to the most popular Google play store apps. An updated version of this dataset is available from https://www.kaggle.com/lava18/google-play-store-apps/data, though for this practice an unmodified dataset was available from Pluralsight's online learning platform.        

To begin with datasheets were combined using VLOOKUP, INDEX & MATCH functions. Some descriptive statistics were then generated using   SUM, ROUNDAVERAGE, & COUNTIF functions; these yielded average ratings, total reviews, the average number of reviews per app, & the total number of free & paid apps in the dataset. 

This was followed by a small project utilyzing PowerQuery to import car sales data from several sources into one sheet. I then returned to the play store dataset, transformed the date of last update into a integer, & generated descriptive statistics for time since last update, number of reviews, & total downloads, this revealing incredibly high levels of kurtosis & histograms suggesting a highly uneven distribution. For practice, a multivariate regression was conducted using total downloads as the DV and Time since last update & the number of reviews as independent variables.  

Somewhat predictably for a non-parametric sample simply jammed into an OLS regression, No p-value in the regression was greater than 0.85 (!), suggesting this ad-hoc model and its paths hold little predictive value when trying to assess the total number of installs. 







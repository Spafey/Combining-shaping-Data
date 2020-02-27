# Data

A collection of data science projects, in order to develop proficiency.

This project began with the merging of pre-scraped datasets relating to the most popular Google play store apps. An updated version of this dataset is available from https://www.kaggle.com/lava18/google-play-store-apps/data, though for this practice an unmodified dataset was available from Pluralsight's online learning platform.        

To begin with datasheets were combined using VLOOKUP, INDEX & MATCH functions. Some descriptive statistics were then generated using   SUM, ROUNDAVERAGE, & COUNTIF functions; these yielded average ratings, total reviews, the average number of reviews per app, & the total number of free & paid apps in the dataset. 

This was followed by a small project utilyzing PowerQuery to import car sales data from several sources into one sheet. I then returned to the play store dataset, transformed date of last update into an integer, & generated descriptive statistics for time since last update, number of reviews, & total downloads. Generating descriptive statistics with excels's analysis toolkit revealed incredibly high levels of kurtosis, with visual inspection of histograms suggesting a highly uneven distribution. For practice purposes a regression was conducted anyway, using Total Downloads as a DV and Time since Update, & Number of Reviews as independent variables.  

  no p-value in the regression model was greater than 0.85 (!), with relationships between data therefore indistinguishable from chance occurrence regardless of F value. Further data cleaning in Excel using quartiles was quick, messy, & yielded an only slightly less leptokurtic sample that also failed to find any statistical significance. Lack of bonferroni aside, the sample was not parametric and could not be overfitted into an OLS regression no matter the amount of post-hoc hacking. If this data were of importance however, non-parametric tests such as wilcoxin's & spearman's could be considered.
  






# House-Prices-Advanced-Regression-Problem
My solution for the House Prices Advanced Regression Problem

The first step to be taken in the project is to view and explore the data using various plotting methods. One such method that I applied was to group the categorical value type columns according to their count and plot them against the sale price to gain a better understanding of the data. 

Depending on the relation between the data in the columns and the sale price, we group one or more categories into a band so that the model has better prediction. The 'replace()' function is meant to take in the dataset (either train or test) and categorize them into usable values by the regression model. 

The replace() function makes use of the band_create() function. The band_create function is a simple function that replaces the string values of a categorical type data column and converts them into integer values for use by the regression model. However, using the band_create function for all data columns would be crude and counterproductive, hence the replace function specifically converts and replaces bands in a few columns such as 'LotShape', 'OverallCond' and 'ExterCond' and many more based on the way the data behaves, rather than simply classifying each different kind of string. For example the prices for the houses having sale condition as 'Abnormal' and 'Family' were almost always equal, and hence they are grouped into one band. 

Since the data variables have a huge factor of interconnection between the variables, through hit and trial it was found that the Ridge Regressor works the best for our particular model. 

Thus after replacing 'Obj' type missing data with a blank string that will later be categorized in band_create, and replacing missing values in integer type values as 0, we fit the data into the model and finally obtain our answer after choosing almost all variables, excluding a few such as Utilities(since almost all houses have the value 'AllPub') and PoolQC('99% lf values are missing), we fit and predict our answer. 

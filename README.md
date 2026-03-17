# Dallas_County_ResidentialProperty_Stats

This EtLT and data analysis project uses data from the Dallas County Appraisal District, the Census Bureau, and the Home Mortgage Disclosure Act Datasets. The objective is to compare existing homeownership statistics to the statistics of households that are able to purchase homes in the current environment by looking at loans that were approved.

The data for this analysis came from several different local and federal agencies and required a bit of pre-processing since it is not homogenous. The pre-processing was done in python and those files are included in this repo. 

The data was then uploaded to GCP (Google Cloud Platform) and then into BigQuery, where further processing using SQL was done before the data was finally ready for use in Looker Studio. 

The link to the full Looker Studio Dashboard - https://lookerstudio.google.com/reporting/10ef134b-3076-4163-8511-29178927b567

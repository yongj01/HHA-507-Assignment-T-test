#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:56:16 2021

@author: jeremyyong
"""

import pandas as pd
from scipy.stats import ttest_ind
from numpy.random import seed
from numpy.random import randn
import scipy.stats as stats
from scipy.stats import shapiro
from matplotlib import pyplot



diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(100)

diabetes ['totalCountprocedures'] = diabetes['num_lab_procedures'] + diabetes['num_procedures']



## Questions: 
    
## 1) Is there a difference between sex (M:F) and the number of days in hospital?

## gender
## timeinhospital


sex = diabetes['gender']
timeinhospital = diabetes['time_in_hospital']

## I first tried to do a shapiro test 

shapiro(timeinhospital)

## ShapiroResult(statistic=0.8869138360023499, pvalue=0.0)

timeinhospital_stat, timeinhospital_p = shapiro(timeinhospital)
sex_stat, sex_p = shapiro(sex)

## could not convert string to float: 'Female'

## I created a histogram of time in hospital 

pyplot.hist(timeinhospital).show()

## Pearson

from scipy.stats import spearmanr, pearsonr

pearsonr(timeinhospital, sex)

## pearson returned error

spearmanr(timeinhospital, sex)

## spearmanrResult(correlation=-0.038631577215696454, pvalue=6.383652632491919e-35)

## Added a variable for spearman correlation

spearmancorrelation, spearmanp =spearmanr(timeinhospital, sex)

## Performed T test 

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']
ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

## The results are Ttest statistic=9.542637042242887, pvalue=1.4217299655114968e-21

## Since the p value is below 0.05, there is a significant difference between the sex (M:F) and number of days in the hospital.



## 2) Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?

## race
## timeinhospital

## I did a count of all the race categories

diabetes['race'].value_counts()

## I created two variables for Caucasian and AfricanAmerican

Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

## The results are Ttest statistic=-5.0610017032095325, pvalue=4.178330085585203e-07

## Since the p value is below 0.05, there is a significant difference between the race (Caucasian and African American) and number of days in the hospital.


## 3) Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?


## I created a variable for Asian

Asian = diabetes[diabetes['race']=='Asian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Asian['num_lab_procedures'], AfricanAmerican['num_lab_procedures'])

## The results are Ttest_ind statistic=-3.9788715315360292, pvalue=6.948907528800307e-05

## Since the p value is below 0.05, there is a significant difference between the race (Asian and African American) and number of lab procedures performed.









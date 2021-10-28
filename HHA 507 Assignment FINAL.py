#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:56:16 2021

@author: jeremyyong
"""

import pandas as pd
from scipy.stats import ttest_ind



diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

diabetes_small = diabetes.sample(100)


## Questions: 
    
## 1) Is there a difference between sex (M:F) and the number of days in hospital?

## gender
## timeinhospital


sex = diabetes['gender']
timeinhospital = diabetes['time_in_hospital']

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']
ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

## The results are Ttest statistic=9.542637042242887, pvalue=1.4217299655114968e-21


## 2) Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?

## race
## timeinhospital

diabetes['race'].value_counts()

Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

## The results are Ttest statistic=-5.0610017032095325, pvalue=4.178330085585203e-07

## 3) Is there a difference between RACE (Asian and African American) and the number of lab procedures performed?


Asian = diabetes[diabetes['race']=='Asian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Asian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

## The results are Ttest statistic=-4.193460125064539, pvalue=2.7592265975996794e-05









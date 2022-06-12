#importing libraries
#import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
 
dataset = dataset.drop('State',axis=1)

sns.heatmap(dataset.corr(),cmap='Blues')

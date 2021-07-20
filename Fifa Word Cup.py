# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:25:30 2021

@author: Taofeek Oyedele

Data SOurce: https://www.kaggle.com/abecklas/fifa-world-cup

Aim: To analyse goals scored at the World Cup using seaborn library
"""

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\Fifa Word Cup.xlsx', 'Fifa Word Cup')
print(df.head())
print(df.info)
print(df.describe())

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']


WC_1998 = df[df.Year == 1998]
WC_2002 = df[df.Year == 2002]
WC_2006 = df[df.Year == 2006]
WC_2010 = df[df.Year == 2010]
WC_2014 = df[df.Year == 2014]
Last_Five_WC = pd.concat([WC_1998, WC_2002, WC_2006, WC_2010, WC_2014])
print(Last_Five_WC)
Last_Five_WC.Stage = Last_Five_WC.Stage.replace(to_replace=['Match for third place','Play-off for third place'],
                     value='Third place')


def total_goals_scored():
    sns.set_style('whitegrid')
    sns.set_context('notebook', font_scale=1.25)
    plt.figure(figsize=(12,7))
    ax=plt.subplot()
    ax = sns.barplot(data=df, x='Year', y='Total Goals', ci='sd')
    ax.set_title('Total Goals scored at each WC')
    plt.show()

total_goals_scored()


def goals_scored_in_last_five_WC():
    sns.set_context('poster', font_scale=0.5)
    plt.figure(figsize=(25,10))
    ax2=plt.subplot()
    ax2 = sns.barplot(data=Last_Five_WC,hue='Year', y='Total Goals', x='Stage')
    ax2.set_title('Total Goals scored at each stage of 2010 and 2014 WC')
    plt.show()
    
goals_scored_in_last_five_WC()


def goals_scored():
    df_goals = pd.read_excel(r'C:\Users\Taofeek Oyedele\Documents\Python Scripts\Fifa Word Cup.xlsx', 'Goals')
    print(df_goals.head())
    sns.set_context('notebook', font_scale=1.25)
    plt.figure(figsize=(12,7))
    ax4=plt.subplot()
    sns.set_palette('Spectral')
    ax4 = sns.boxplot(data=df_goals, x='year', y='goals')
    ax4.set_title('Goals scored')
    plt.show()

goals_scored()

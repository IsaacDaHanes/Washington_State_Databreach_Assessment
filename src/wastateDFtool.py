#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import argparse
import os
import dataframe_image as dfi

# setting a path variable to be used later
mypath = "C:/Users/isaac/galvanize/daimil10/case_studies/Washington_State_Databreach_Assessment/images"

# keeps pandas from displaying scientific notation
pd.options.display.float_format = '{:.0f}'.format

# building a class to hold information about the dataframe and methods to use it
class WaStateDBDF():

    def __init__(self, filepath):
        self.uncleandf = pd.read_csv(filepath)
        self.columnlist = self.cleandf.columns.values
        
    @property
    def cleandf(self):
        '''
        gets a clean df from the unclean df import upon instantiation, stores as property
        '''
        # helper functions
        def to_datetime_date_helpfunction(dataframe):
            '''
            Inputs: dataframe

            Outputs: dataframe with all values in columns that have 'date' in their 
                                                        name as datetime.date objects    
            '''

            colsarray = dataframe.columns.values

            for x in colsarray:
                if 'Date' in x:
                    dataframe[f'{x}'] = pd.to_datetime(dataframe[f'{x}']).dt.date
            return

        wa_databreach_df = self.uncleandf 
        # drop unusable or unneccessary columns
        wa_databreach_df = wa_databreach_df.drop(['Id', 'YearText', 'Year','EndedOnDayDiscovered'],axis=1)

        # Scrub all instances where databreach cause is cyberattack and cyberattacktype is NaN, replace with 'Unreported'
        wa_databreach_df.loc[:, 'CyberattackType'][(wa_databreach_df['DataBreachCause'] == 'Cyberattack') 
                                                & (wa_databreach_df['CyberattackType'].isnull())] = 'Unreported'
        
        # Enact the to_datetime_date_helpfunction on the dataframe
        to_datetime_date_helpfunction(wa_databreach_df)

        return wa_databreach_df

    def get_data_stats(self, argument):
        '''
        Grabs data statistics from self.cleandf and outputs them in a readable/usable format.

        Inputs: argument(use 'o' to output to images file, use 's' to output for viewing in jupyter notebook)

        Outputs: a fig,axs object containing information about the table or a .png file
        '''
        # help function
        def get_nanscount_helpfunction(dataframe):
            '''
            Inputs: Dataframe

            Outputs: A list of counts of nans per column
            '''
            countlist = []
            colsarray = self.columnlist

            for x in colsarray:
                countlist.append(dataframe[f'{x}'].isnull().sum().sum())
            return countlist

        # help function
        def get_uniquescount_helpfunction(dataframe):
            '''
            Inputs: Dataframe

            Outputs: A list of counts of uniques per column
            '''
            countlist = []
            colsarray = self.columnlist
         
            for x in colsarray:
                countlist.append(len(dataframe[f'{x}'].unique()))
            return countlist

        # make a 2x2 fig,axs where each axs contains pertintent info about the dataframe
        fig, axs = plt.subplots(2,1,figsize=(10,16))

        fig.tight_layout()
        
        axs[0].barh(self.columnlist, get_nanscount_helpfunction(self.cleandf))
        axs[0].set_title('Number of NaNs per Column')

        axs[1].barh(self.columnlist, get_uniquescount_helpfunction(self.cleandf))
        axs[1].set_title('Number of Unique Values per Column')
        
        if argument == 'o':
            fig.savefig(f'{mypath}/data_stats', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    # the three methods directly below will be used in the various plotting methods
    def get_vcount(self, columnname):
        '''
        Inputs: column name

        Outputs: a pandas value count series object for the given column name
        '''
        return self.cleandf[columnname].value_counts()
    
    def get_uniques(self, columnname):
        '''
        Inputs: colum name

        Outputs: numpy array of unique values from the given column name
        '''
        return self.cleandf[columnname].unique()

    def get_groupby(self, columnname, aggregation):
        '''
        Inputs: Column name and an argument specifying the aggregation type, 'c' or 's'

        Outputs: A dataframe grouped in the fashion indicated by the input
        '''
        if aggregation == 'c':
            grouped_df = self.cleandf.groupby(columnname).count()

        elif aggregation == 's':
           grouped_df = self.cleandf.groupby(columnname)

        else:
            grouped_df = self.cleandf.groupby(columnname).count()

        return grouped_df   

    # these are the methods used to plot various sections of the data
    def plot_pie(self, columnname, argument, title='Pie Chart'):
        '''
        Inputs: column name, an 's' or an 'o', and a title

        Ouputs: a pie chart for the given column, saved or shown, with given title, or 'Pie Chart' as default
        '''
        
        fig, ax = plt.subplots()
        
        ax.pie(self.get_vcount(columnname), labels=self.get_vcount(columnname).index, autopct='%1.1f%%')
        
        ax.set_title(title)
        
        if argument == 'o':
            fig.savefig(f'{mypath}/{title}', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    def plot_businesses_affected(self, argument):
        '''
        Input: argument, 's' or 'o'
        
        Output: A pie chart of business types most affected, threshold count < 20, will save with 'o', or just show with 's'
        '''

        bustype = self.get_vcount('BusinessType')

        fig, ax = plt.subplots()

        ax.pie(bustype[bustype > 20], labels=bustype[bustype > 20].index, autopct='%1.1f%%')

        ax.set_title('Businesses Most Affected')

        if argument == 'o':
            fig.savefig(f'{mypath}/Businesses Most Affected', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    def plot_disinprog(self, argument):
        '''
        Inputs: argument, 's' or 'o'

        Outputs: A pie chart indicating how often attacks were discovered in progress, will save with 'o', or just show with 's'
        '''
        
        fig, ax = plt.subplots()

        ax.pie(self.get_vcount('DiscoveredInProgress'), labels=['Not Discovered In Progress','Discovered In Progress'], autopct='%1.1f%%')
        ax.set_title('How often were attacks discovered while they were happening?')

        if argument == 'o':
            fig.savefig(f'{mypath}/Discovered In Progress', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    def plot_affected_ranges(self, argument):
        '''
        Inputs: argument, 's' or 'o'

        Outputs: A bar chart indicating how many attacks affected each range of Washingtonians, will save with 'o', or just show with 's'
        '''

        affected_ranges = self.get_groupby('WashingtoniansAffectedRange','c')['Name']

        fig, ax = plt.subplots()

        fig.tight_layout

        ax.bar(affected_ranges.index, affected_ranges.values)

        ax.set_title('Washingtonians Affected by Ranges')

        ax.set_xticklabels(affected_ranges.index, rotation = 45, fontsize = 8)

        if argument == 'o':
            fig.savefig(f'{mypath}/Affected Ranges', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    def plot_by_date(self, argument):
        '''
        Inputs: argument, 's' or 'o'

        Outputs: A scatterplot indicating how many attacks were carried out on a given day, will save with 'o', or just show with 's'
        '''
        
        plotbydate = self.get_groupby('DateStart', 'c')
        plotdates_notfebsev = plotbydate[plotbydate['Name'] < 108]
        
        fig,ax = plt.subplots()

        ax.scatter(plotdates_notfebsev.index, plotdates_notfebsev['Name'])

        ax.set_title('Attacks by Date')

        ax.set_xticklabels(ax.get_xticklabels(), rotation=65, fontsize=10)

        if argument == 'o':
            fig.savefig(f'{mypath}/Attacks By Date', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    # the below functions will explore the breaches that occured 2020-02-07
    @property
    def onebigx(self):
        '''
        Inputs: None

        Outputs: Gets a table of the attacks that occurred on feb 07 2022 and saves it as a property.
        '''

        dtsv = dt.date(2020,2,7) # dtsv is date to search variable

        onebigx = self.cleandf[self.cleandf['DateStart']==dtsv][['Name', 'IndustryType', 'CyberattackType', 'WashingtoniansAffected', 'DaysOfExposure', 'DaysElapsedBetweenEndAndDiscovery', 'DiscoveredInProgress', 'DaysOfExposure', 'DaysElapsedBeforeNotification']].reset_index().drop('index', axis=1)
    
        return onebigx
    
    def plot_onebigx_cybattacktype(self, argument):
        '''
        Inputs: argument, 's' or 'o'

        Outputs: Pie chart of cyberattack types for breaches on 2020-02-07, 's' to show, 'o' to save
        '''
        # getting onebigx df
        onebigx = self.onebigx
        
        # extracting values needed to plot
        onebigx_vc = onebigx['CyberattackType'].value_counts()
        onebigx_labels = onebigx_vc.index

        fig, ax = plt.subplots()

        ax.pie(onebigx_vc, labels=onebigx_labels, autopct='%1.1f%%')
        ax.set_title('Cyber Attacks by Type')

        if argument == 'o':
            fig.savefig(f'{mypath}/2020-02-07 Attack Type Piechart', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    def plot_onebigx_industrytype(self, argument):
        '''
        Inputs: argument, 's' or 'o'

        Outputs: Pie chart of industry types for breaches on 2020-02-07, 's' to show, 'o' to save
        '''
        # getting onebigx df
        onebigx = self.onebigx
        
        # extracting values needed to plot
        onebigx_vc = onebigx['IndustryType'].value_counts()
        onebigx_labels = onebigx_vc.index

        fig, ax = plt.subplots()

        ax.pie(onebigx_vc, labels=onebigx_labels, autopct='%1.1f%%')
        ax.set_title('Industries Affected by Type')

        if argument == 'o':
            fig.savefig(f'{mypath}/2020-02-07 Industry Type Piechart', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    def plot_onebigx_affected_scatter(self, argument):
        '''
        Inputs: argument, 's' or 'o'

        Outputs: Scatterplot of number affected for breaches on 2020-02-07, 's' to show, 'o' to save
        '''
        # getting onebigx df
        onebigx = self.onebigx
        
        # extracting values needed to plot
        onebigx_vc = onebigx['IndustryType'].value_counts()
        onebigx_labels = onebigx_vc.index

        fig, ax = plt.subplots()

        ax.scatter(onebigx.index, onebigx['WashingtoniansAffected'])
        ax.set_title('Washingtonians Affected per Organization Breached')
        ax.set_ylabel('Number Affected(In Millions)')

        if argument == 'o':
            fig.savefig(f'{mypath}/2020-02-07 Washingtonians Affected By Org', bbox_inches='tight')
        
        elif argument == 's':
            plt.show()
        
        else:
            plt.show()

    # this function will save a viewable table of the top 10 largest breaches

    def view_top_10(self):
        '''
        Inputs: None

        Outputs: A .png file of the top 10 largest breaches in the database
        '''

        # getting a table of the top 10
        biggestbreaches = self.cleandf[self.cleandf['WashingtoniansAffected'] > 500000].sort_values(by='WashingtoniansAffected',ascending=False).reset_index().drop('index', axis=1)[['Name', 'IndustryType', 'DataBreachCause', 'CyberattackType', 'WashingtoniansAffected']]
        # renaming columns to make them more readable
        biggestbreaches['Number of Washingtonians Affected'] = biggestbreaches['WashingtoniansAffected']
        biggestbreaches['Organization'] = biggestbreaches['Name']
        biggestbreaches['Industry Type'] = biggestbreaches['IndustryType']
        biggestbreaches['Attack Type'] = biggestbreaches['CyberattackType']
        biggestbreaches['Breach Cause'] = biggestbreaches['DataBreachCause']
        biggestbreaches = biggestbreaches.drop(['WashingtoniansAffected', 'Name', 'IndustryType','CyberattackType', 'DataBreachCause'], axis=1)
        # organizing the columns
        biggestbreaches = biggestbreaches[['Organization', 'Industry Type', 'Breach Cause', 'Attack Type', 'Number of Washingtonians Affected']]

        # export the table as a png
        biggestbreaches.dfi.export('../images/Top 10 Breaches.png')


if __name__ == '__main__':
    Databreaches = WaStateDBDF('../data/wa_state_data_breaches.csv')

    Databreaches.cleandf
    Databreaches.columnlist

    Databreaches.get_data_stats('s')
    Databreaches.get_data_stats('o')

    Databreaches.get_vcount('DiscoveredInProgress')
    Databreaches.get_uniques('DiscoveredInProgress')

    Databreaches.plot_pie('DataBreachCause','s', 'Causes of Data Breaches')
    Databreaches.plot_pie('DataBreachCause','o', 'Causes of Data Breaches')

    Databreaches.plot_businesses_affected('s')
    Databreaches.plot_businesses_affected('o')
    
    Databreaches.plot_disinprog('s')
    Databreaches.plot_disinprog('o')

    Databreaches.get_groupby('DataBreachCause', 'c')

    Databreaches.plot_affected_ranges('s')
    Databreaches.plot_affected_ranges('o')

    Databreaches.plot_by_date('s')
    Databreaches.plot_by_date('o')

    Databreaches.onebigx

    Databreaches.plot_onebigx_cybattacktype('s')
    Databreaches.plot_onebigx_cybattacktype('o')

    Databreaches.plot_onebigx_industrytype('s')
    Databreaches.plot_onebigx_industrytype('o')

    Databreaches.plot_onebigx_affected_scatter('s')
    Databreaches.plot_onebigx_affected_scatter('o')

    Databreaches.view_top_10()
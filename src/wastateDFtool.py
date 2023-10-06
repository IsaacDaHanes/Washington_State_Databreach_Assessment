#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import argparse
import os

# setting a path variable to be used later
mypath = "c:/Users/RGBMonster/galvanize/daimil10/case_studies/Mid_Term_Repos/Washington_State_Databreach_Assessment/images"

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
    
    def get_vcount(self, columname):
        '''
        Inputs: column name

        Outputs: a pandas value count series object for the given column name
        '''
        return self.cleandf[columname].value_counts()
    
    def get_uniques(self, columname):
        '''
        Inputs: colum name

        Outputs: numpy array of unique values from the given column name
        '''
        return self.cleandf[columname].unique()

    def plot_():
        pass

if __name__ == '__main__':
    Databreaches = WaStateDBDF('../data/wa_state_data_breaches.csv')

    Databreaches.cleandf
    Databreaches.columnlist
    Databreaches.get_vcount('DiscoveredInProgress')
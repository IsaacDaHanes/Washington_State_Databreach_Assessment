#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

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
        wa_databreach_df = wa_databreach_df.drop(['Id', 'YearText', 'Year','WashingtoniansAffectedRange'],axis=1)

        # Scrub all instances where databreach cause is cyberattack and cyberattacktype is NaN, replace with 'Unreported'
        wa_databreach_df.loc[:, 'CyberattackType'][(wa_databreach_df['DataBreachCause'] == 'Cyberattack') 
                                                & (wa_databreach_df['CyberattackType'].isnull())] = 'Unreported'
        
        # Enact the to_datetime_date_helpfunction on the dataframe
        to_datetime_date_helpfunction(wa_databreach_df)

        # Reorder columns human-logically
        wa_databreach_df = wa_databreach_df.loc[:,['','','','','','','','','','','','','','']]

        return wa_databreach_df
    
    @property
    def columnlist(self):
        '''
        gets a list of columns from self.cleandf, stores as property
        '''
        
        
        
        pass

    def get_data_stats(self):
        '''
        Grabs data statistics from self.cleandf and outputs them in a readable/usable format
        '''
        pass

    def get_vcount(self, columname):
        '''
        Gets pandas value count series from the given column name
        '''
        pass
    
    def get_uniques(self, columname):
        '''
        Gets numpy array of unique values from the given column name
        '''
        pass


if __name__ == '__main__':
    Databreaches = WaStateDBDF('../data/wa_state_data_breaches.csv')
import pandas as pd
from matplotlib.axes import SubplotBase
import matplotlib.pyplot as plt


# A -----------------------------------------------------------------------------
def read_files(travels_file, missions_file):
    pass
# B.1 -----------------------------------------------------------------------------


def merge_tables(df_travels,df_missions):
   pass

# B.2 -----------------------------------------------------------------------------

def scatter_plot(df_merged):
   pass
   
    
# C -----------------------------------------------------------------------------

def add_gain_per_monster(df_merged):
    pass

# D -----------------------------------------------------------------------------


def daily_gain_per_universe(df_merged):
    pass

# E -----------------------------------------------------------------------------

def drop_nonprofitable_universes(df_merged):
    pass
    
# F -----------------------------------------------------------------------------

def mean_duration(df_5):
    pass

# G -----------------------------------------------------------------------------

def drop_least_daily_lucrative_universe(df_5):
    pass 

# H ------------------------------ ----------------------------------------------

def drop_least_daily_lucrative_universe_with_teleporting(df_merged):
    pass



if __name__=="__main__":

    print("===   A   ===")
    df_travels,df_missions=read_files("travels.csv", "missions.csv")
    print("Travels:")
    print(df_travels)
    print("Missions:")
    print(df_missions)
    
    print("===   B.1   ===")
    df_merged=merge_tables(df_travels,df_missions)
    print(df_merged)

    print("===   B.2   ===")
    ax=scatter_plot(df_merged)
    print("Is correct return type?", isinstance(ax,SubplotBase))
    plt.show()
    
    print("===   C   ===")
    df_merged_cpy=df_merged.copy()
    add_gain_per_monster(df_merged_cpy)
    print(df_merged_cpy)
    
    print("===   D   ===")
    daily_gain=daily_gain_per_universe(df_merged)
    print(daily_gain)

    print("===   E   ===")
    df_5=drop_nonprofitable_universes(df_merged)
    print(df_5)

    print("===   F   ===")
    avg=mean_duration(df_5)
    print(avg)

    print("===   G   ===")
    df_7=drop_least_daily_lucrative_universe(df_5)
    print(df_7)
    
    print("===   H   ===")
    df_8=drop_least_daily_lucrative_universe_with_teleporting(df_merged)
    print(df_8)
    
    

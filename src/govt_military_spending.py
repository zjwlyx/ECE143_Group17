import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to perform Exploratory data analysis on Military Spendings
def military_spending_vs_gpi(military_spending_data,gpi_data):

    """
    Read the military expediture data collected from worldbank and compare it with Global Peace index
    Args:
        File locations of the govt education and literacy csv files
    Returns:
        matplotlib.plt object to display data analysis result
    """

    df_govt_military = pd.read_csv("../data/Govt_Military_Spending_csv.csv")

    countries = df_govt_military.iloc[4:270,0]

    date_range = df_govt_military.iloc[3,4:66]

    spending_data = df_govt_military.iloc[4:270,4:66]
        
    df_govt_mil_spend_f = pd.DataFrame(spending_data.to_numpy(),index=list(countries),columns=list(date_range))

    gpi_data = pd.read_csv("../data/GPI_data_csv.csv")

    gpi_country_pd = pd.DataFrame(gpi_data.iloc[0:163,2:17].to_numpy(),index=list(gpi_data.iloc[:,0]),columns=list(gpi_data.columns)[2:17])

    global_gpi_pd = gpi_country_pd.sum(0)/163

    global_gpi_pd_all_year = pd.DataFrame([np.nan]*len(date_range), index=list(date_range))
    #global_gpi_pd_all_year
    global_gpi_pd_all_year.loc[2008:2022,0] = global_gpi_pd.iloc[:-1].to_numpy()

    df_govt_mil_spend_per_year = df_govt_mil_spend_f.sum(0)

    len(df_govt_mil_spend_per_year.index)
    df_govt_mil_spend_per_year.to_numpy()
    x_list = [int(x) for x in list(df_govt_mil_spend_per_year.index)]
    x_str_list = [str(x) for x in x_list]

    bar_width = 0.8

    fig, ax = plt.subplots(figsize=(15, 8))

    p = ax.bar(x_str_list,df_govt_mil_spend_per_year.to_numpy()/1e12,bar_width)
    #ax.bar_label(p,label_type='center')
    #fig.set_figwidth(15)
    #fig.figsize(15,6)
    plt.xticks(rotation=70,fontsize = 12)
    ax.set_title("Global Military Spending vs. Global Peace Index",fontsize = 20)
    ax.set_xlabel("Spending per Year 1960 - 2021", fontsize = 20)
    ax.set_ylabel("Military expenditure (in trillion USD)", fontsize = 15)

    ax2 = ax.twinx()

    color = 'tab:red'
    ax2.set_ylabel('Global Peace Index (GPI)',color=color, fontsize = 15)
    ax2.plot(x_str_list,global_gpi_pd_all_year.to_numpy(),color=color,linewidth=5)
    ax2.tick_params(axis='y',labelcolor=color)
    ax2.set_ylim(1.5,3.0)

    ax.legend(['Global Militray Sending'],fontsize = 15, loc='upper left')
    ax2.legend(['Global Peace Index'],fontsize = 15, loc='lower right')

    fig.tight_layout()
    #plt.show()

    return plt
    
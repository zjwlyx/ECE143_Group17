# ECE143_Group17
ECE143 Group_17 Project: Investigate and Analyze the Effect of Government Spending
## Motivation
How does the government spending influence people's daily life?

Will the government spending help booster the countries economy?


## Team Members
-@AjayUCSD

-@boucsd

-@hari201995

-@vvishnus

-@zjwlyx

## Packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
```bash
pip install pandas
pip install matplotlib
pip install seaborn
pip install geopandas
```

## Main File and Repo Structure

The main file is src/Group_17_project.ipynb . Please run all the cells to generate plots. some plots may be missing because of plotly issues. 
```
├── LICENSE
├── README.md                      <- The top-level README for developers using this project.
├── requirements.txt               <- Required 3rd party modules. 
├── data
│   ├── processed      		       <- Data from the sources used for our EDA
│
├── ECE143_Group_17_Presentation <- Presentation ppt
│
└── src                		       <- Source code for use in this project.
    ├── __init__.py    		       <- Makes src a Python module.
    │
    ├── *.py, *.ipynb            <- Individual EDA on different topics within our presentation
    │
		└── Group_17_Project_updated.ipynb   	   <- File containing functions used in visualizations.ipynb.
```
## Infra Code Disclaimer 

When running the infrastructure setting, if one gets an error of [2021] not present, please run the data loading cell only again and run the cell where the error was 
there. The error should go this time.
## References
[1]. [Ourworldindata.org](https://ourworldindata.org/government-spending#government-spending-is-an-important-instrument-to-reduce-inequality)

[2]. World Bank Data - https://databank.worldbank.org/home.aspx

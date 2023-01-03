# Cultural Data Science Exam - NLP & Danish Prime Minister's New Year's Speeches 

This repository holds all necessary files to run the analyses conducted in my Introduction to Cultural Datascience Exam Project in January 2023. The project employs various NLP techniques and text mining methods to conduct an exploratory analysis of the language in 30 New Year's Speeches held by Danish Prime Ministers in the period 1993 - 2023. 

The code and project was made by Emma Risgaard Olsen, 5th semester student at Cognitive Science, Aarhus University. 


The repository contains the following:

| File/folder | Content | 
|:--|:-:|
|`scraping_url_to_txt.Rmd`|R Markdown used to scrape articles from URL using the `rvest` package|
|`scraped_txts`|Folder containing the scraped articles as separate .txt files|
|`stopord.txt`|Text file containing Danish stop words|
|`helper_functions.py`|Python file containing functions used in pre-processing and analysis
|`preprocessing.ipynb`| Jupyter Notebook file used to preprocess the speeches|
|`speeches_df.csv`|CSV file containing all the cleaned speeches to be loaded as a dataframe| 
|`analysis_and_visualisation.ipynb`|Jupyter Notebook file used for analysis and visualisation of speeches|


# Process_module
This is a file.py which regroup functions or application that can help to explore DataFrame and do preprocessing and visualisation
# Python Code
"import requests
url = 'https://raw.githubusercontent.com/Hassen-Ti/Process_module/main/process_app.py'

response = requests.get(url)

with open('process_app.py', 'wb') as file:

    file.write(response.content)
    
import process_app as pa"
#OR you can copy this code and use pa.url(df) ...
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display, clear_output
from scipy import stats
import requests
# URL  GitHub
url = 'https://raw.githubusercontent.com/Hassen-Ti/Process_module/main/process_app.py'
response = requests.get(url)
# saving temporarly
with open('process_app.py', 'wb') as file:
    file.write(response.content)
import process_app as pa 
# Try my super cool application for data preprocessing
you can try with any df  / 
df = pd.read_csv("path.csv")  /
pa.preprocessing(df)  /
pa.visual(df)
url_df()

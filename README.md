# Process_module

This is my first project `file.py` which groups methods and functions that can help to explore DataFrames and do visualization.

## Python Code

# you can copy this code, and try to use my functions ;) 

```python
import requests

url = 'https://raw.githubusercontent.com/Hassen-Ti/Process_module/main/process_app.py'

response = requests.get(url)

with open('process_app.py', 'wb') as file:
    file.write(response.content)

import process_app as pa
```

# saving temporarly
```
with open('process_app.py', 'wb') as file:
    file.write(response.content)
import process_app as pa 
## Try my super cool application for data preprocessing
```
# you can try with any df 
```
df = pd.read_csv("path.csv")
pa.preprocessing(df)  # finished
pa.visual(df) # under development and fitting
url_df() # under development
```

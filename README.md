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

# you can try with any df 
```
df = pd.read_csv("path.csv")
pa.preprocessing(df)  # finished
pa.visual(df) # can be used , under development and fitting
pa.missing_value_manager(df) # can be used, under fitting
pa.url_df() # under development
pa.MachineLearn(df) # under developemnt
```
## example after importing my functions try to do 
```
import pandas as pd
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
df = pd.read_csv(url)
pa.preprocessing(df)
pa.visual(df)          # try to use it, and see what it gives ;)
```

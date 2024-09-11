# Process module

This is my first Python project, which includes a file process_app.py that groups several methods and functions to help explore DataFrames and perform visualizations.

# How to Use the Code
## You can easily integrate and try out my functions by copying the code below:
```python
import requests

# Download the process_app.py file from my GitHub repository
url = 'https://raw.githubusercontent.com/Hassen-Ti/Process_module/main/process_app.py'

response = requests.get(url)

with open('process_app.py', 'wb') as file:
    file.write(response.content)

# Import the module containing my functions
import process_app as pa

```

# Using Your Own DataFrame 
## You can test the functions with any DataFrame:
```
# Example with your own CSV file
df = pd.read_csv("path/to/your/csvfile.csv")

# Available functions in the module
pa.preprocessing(df)            # Ready to use
pa.visual(df)                   # Ready to use, but still under optimization
pa.missing_value_manager(df)    # Ready to use, but still under optimization
pa.url_df()                     # Under development
pa.MachineLearn(df)             # Under development
```
## Example: Working with the Titanic Dataset
```
import pandas as pd

# Load Titanic dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
df = pd.read_csv(url)

# Use the preprocessing function
pa.preprocessing(df)

# Try visualizing the dataset
pa.visual(df)  # Try using it and explore the results ;)
```

# Process_module
This is a file.py which regroup functions or application that can help to explore DataFrame and do preprocessing

import requests
# URL  GitHub
url = 'https://raw.githubusercontent.com/Hassen-Ti/Process_module/8cfe96ebce84203543ef349b37d59e06db4fd3e0/process_app.py'
response = requests.get(url)
# saving temporarly
with open('process_app.py', 'wb') as file:
    file.write(response.content)
# importing module 
import process_app as pa

you can try with any df 
df = pd.read_csv("path.csv")
pa.preprocessing(df)
pa.visual(df)

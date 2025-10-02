# Import required libraries
import pandas as pd
from google.colab import files
import io

# Upload file
uploaded = files.upload()

# Read the uploaded file assuming the filename is 'dataset.csv'
df = pd.read_csv(io.BytesIO(uploaded['dataset.csv']))

# Display first few rows to verify
df.head()

     

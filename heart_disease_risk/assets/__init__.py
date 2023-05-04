# Assets are used to create data pipelines
# Data pipelines are used to read data, process it and return it in a format that can be used by the model
# Note: Create an assets does not mean that the data is read, processed and returned (materialized) which will be stored on databases or cloud storage.
# Think of the materialization as a instance of the asset which would create a snapshot of the data at that point in time
# Assets can be manually materialized (GUI) or automatically materialized (https://docs.dagster.io/_apidocs/ops#dagster.AssetMaterialization)

from dagster import asset, file_relative_path # Import the asset decorator
from dagstermill import define_dagstermill_asset # Import the define_dagstermill_asset decorator
import pandas as pd # Import the pandas library

# Function that reads the data from the csv file and stores it in a pandas dataframe
## Panda dataframe is a 2-dimensional labeled data structure with columns of potentially different types, similar to an Excel spreadsheet or SQL table
@asset # Decorator that marks the function as an asset (SDA - Software Defined Asset)
def read_csv_data(): 
	# csv is stores in the data folder that is in the same directory as the assets.py file
	csv_file_path = "heart_disease_risk/data/risco_cardiaco.csv"
	csv_file = pd.read_csv(csv_file_path) # Read the csv file and store it in a pandas dataframe

	dataframe = pd.DataFrame(csv_file) # Create a pandas dataframe from the csv file
	return dataframe # Return the pandas dataframe

# The define_dagstermill_asset decorator is used to create a dagstermill asset
# The decorator returns a dagstermill asset
# Importante Note: define_dagstermill_solid is deprecated and will be removed in a future release. Use define_dagstermill_asset instead.
heart_disease_risk_jupyter_notebook = define_dagstermill_asset(
	name = "heart_disease_risk_jupyter", # Name of the asset
	notebook_path = file_relative_path(__file__, "../notebooks/risco-doenca-cardiaca.ipynb"), # Path to the notebook that will be used to create the asset
	group_name = "heart_disease_risk", # Name of the group that the asset belongs to. It should be the same as the name of the directory that the notebook is in
) # Create a dagstermill asset
import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # URL for the GitHub API call to get release assets
    api_url = "https://api.github.com/repos/DataTalksClub/nyc-tlc-data/releases/71979983/assets"

    # Make the API request
    response = requests.get(api_url)

    # Parse the JSON response
    release_data = response.json()
    wanted_files = ['green_tripdata_2020-10.csv.gz','green_tripdata_2020-11.csv.gz','green_tripdata_2020-12.csv.gz']
    # Loop through the assets and download them
    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    df = pd.DataFrame()
    for asset in release_data:
        asset_name = asset['name']
        # Check the asset name if it matches your criteria
        if asset_name in wanted_files:
            print(f"Downloading {asset_name}...")
            
            # Download the file
            url = asset['browser_download_url']
            temp = pd.read_csv(url, sep=',', compression='gzip', dtype=taxi_dtypes,parse_dates=parse_dates)
            df = pd.concat([df, temp], ignore_index=True)
        
    print(len(df))      

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

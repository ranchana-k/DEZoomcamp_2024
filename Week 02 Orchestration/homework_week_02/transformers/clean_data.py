import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    print("Rows having 0 passengers:", data['passenger_count'].isin([0]).sum()) # 661
    print("Rows having no distance:", data['trip_distance'].isin([0]).sum()) # 8862
    data = data[(data['passenger_count']>0) & (data['trip_distance'] > 0)]
    print(len(data)) # 139,370
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    print(pd.unique(data['VendorID'])) # [2, 1]
    data = data.rename(columns={'VendorID': 'vendor_id', 
                        'RatecodeID': 'ratecode_id',
                        'PULocationID': 'pu_location_id',
                        'DOLocationID': 'do_location_id'})
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['vendor_id'].isin([1, 2]).all(),"This dataframe has vendor_id other than 1 and 2."
    assert output['passenger_count'].isin([0]).sum() == 0, "This dataframe has rows with 0 passengers."
    assert output['trip_distance'].isin([0]).sum() == 0, "This dataframe has rows with 0 trip distance."

# import modules
import pandas as pd
from sodapy import Socrata

# API endpoint as a primary copy of the datasets
# do I need a higher limit?
# is JSON or CSV preferred?
# crashes_endpoint = "https://data.cityofchicago.org/resource/85ca-t3if.json"
# vehicles_endpoint = "https://data.cityofchicago.org/resource/68nd-jvt3.json"
# people_endpoint = "https://data.cityofchicago.org/resource/u6pd-qa9d.json"

# attempt unauthenticated client
client = Socrata("data.cityofchicago.org", None)
crashes_results = client.get("85ca-t3if", limit=2000)

# load datasets into dataframes
crashes_master = pd.DataFrame.from_records(crashes_results)

working_df = crashes_master.copy(deep=True)

if __name__ == '__main__':
    print(working_df.head())

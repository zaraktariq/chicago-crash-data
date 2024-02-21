# import modules
import pandas as pd
from sodapy import Socrata

# API endpoint as a primary copy of the datasets
# do I need a higher limit?
# is JSON or CSV preferred?
# crashes_endpoint = "https://data.cityofchicago.org/resource/85ca-t3if.json"
# vehicles_endpoint = "https://data.cityofchicago.org/resource/68nd-jvt3.json"
# people_endpoint = "https://data.cityofchicago.org/resource/u6pd-qa9d.json"

domain = "data.cityofchicago.org"

# attempt an authenticated client
clientAuth = Socrata(domain,
                     "YA4Qqo2jgEauLCdtGL8DRSJuk",
                     "zaraktariq7@gmail.com",
                     "xC|[F8H/bmL^^B@$^'E<s4e$C7_t%G/@_Wb2LB,<")
crashes_results = clientAuth.get("85ca-t3if", limit=2000)
vehicles_results = clientAuth.get("68nd-jvt3", limit=2000)
people_results = clientAuth.get("u6pd-qa9d", limit=2000)

# load datasets into dataframes
crashes_master = pd.DataFrame.from_records(crashes_results)
working_crashes = crashes_master.copy(deep=True)

vehicles_master = pd.DataFrame.from_records(vehicles_results)
working_vehicles = vehicles_master.copy(deep=True)

people_master = pd.DataFrame.from_records(people_results)
working_people = people_master.copy(deep=True)

if __name__ == '__main__':
    # print(working_crashes.head())
    # print(working_crashes.shape)
    # for column in range(working_crashes.shape[1]):
    #    print(working_crashes[working_crashes.columns[column]].count())
    print(working_crashes.describe())
    print(working_vehicles.describe())
    print(working_people.describe())

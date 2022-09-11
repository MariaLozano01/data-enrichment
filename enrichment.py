import pandas as pd
adi = pd.read_csv('US_2019_ADI_Census Block Group_v3.1.csv.zip')
adi
import pandas as pd
discharges = pd.read_csv('Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv.zip')
discharges

discharges.columns
adi.columns
discharges['Zip Code - 3 digits']
adi['FIPS']

df_adi_small = adi(('Unnamed: 0', 'GISJOIN', 'FIPS', 'ADI_NATRANK', 'ADI_STATERNK'))
print[df_adi_small.sample(10).to_markdown()] 

df_discharges_small = discharges(('Health Service Area', 'Hospital County', 'Facility Id', 'Facility Name', 'Zip Code - 3 digits', 'Total Charges', 'Total Costs'))
print[df_discharges_small.sample(10).to_markdown()] 

combined_df = pd.merge(df_discharges_small, df_adi_small, how= 'left', left_on= 'FIPS', right_on= 'Zip Code - 3 digits')

 

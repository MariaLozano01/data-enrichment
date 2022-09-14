import pandas as pd
adi = pd.read_csv('US_2019_ADI_Census Block Group_v3.1.csv.zip') ##Used this line in order to upload the file with pandas
adi ##Ran the code so I could see the file
discharges = pd.read_csv('/Users/marialozano/Documents/GitHub/data-enrichment/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv', on_bad_lines= 'skip', encoding= 'latin1') ##Used this line in order to upload the file with pandas
## on_bad_lines= 'skip', encoding= 'latin1' were both used to solve readining errors and encoding errors that I was encountering 
discharges
discharges.columns #This code was used to get a list of column names present in the file  
adi.columns

discharges['Facility Id'] 
adi['FIPS']

df_adi_small = adi[['Unnamed: 0', 'GISJOIN', 'FIPS', 'ADI_NATRANK', 'ADI_STATERNK']] ##Creates a visual of the columns included within the brackets from the file selected 
print(df_adi_small.sample(10).to_markdown()) ##Prints only 10 columns of the sample 

df_discharges_small = discharges[['Hospital County', 'Facility Id', 'Facility Name', 'Zip Code - 3 digits', 'Total Charges', 'Total Costs']]
print(df_discharges_small.sample(10).to_markdown())

combined_df = pd.merge(df_discharges_small, df_adi_small, how= 'left', left_on= 'FIPS', right_on= 'Facility Id') #Merges the two datasets within the parameters mentioned in the functions above 
combined_df ##runs the function above 

combined_df = df_discharges_small.merge(df_adi_small, how= 'left', left_on= 'Facility Id', right_on= 'FIPS') #Merges the two datasets within the parameters mentioned in the functions above 
combined_df ##runs the function above 

adi.dtypes 
discharges.dtypes



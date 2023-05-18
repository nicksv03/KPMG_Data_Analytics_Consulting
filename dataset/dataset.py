import pandas as pd
dataset = pd.ExcelFile('/Users/nikhil/Library/CloudStorage/GoogleDrive-dcbs17nikhilverma@gmail.com/My Drive/Github/KPMG_Data_Analytics_Consulting/KPMG_VI_New_raw_data_update_final.xlsx')
transactions = 'Transactions'
new_customer_list = 'NewCustomerList'
customer_demographic = 'CustomerDemographic'
customer_address = 'CustomerAddress'

transactions = dataset.parse(transactions)
new_customer_list = dataset.parse(new_customer_list)
customer_demographic = dataset.parse(customer_demographic)
customer_address = dataset.parse(customer_address)

transactions.to_csv('transactions.csv', index=False)
new_customer_list.to_csv('new_customer_list.csv', index=False)
customer_demographic.to_csv('customer_demographic.csv', index=False)
customer_address.to_csv('customer_address.csv', index=False)
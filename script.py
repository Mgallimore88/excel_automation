import pandas as pd
from date import Date



# read raw export
df_raw = pd.read_csv('Edited Export.csv')

# iterate over the df and convert to strings
df_raw.convert_dtypes('b')

# instantiate Date and ZAQ
# specify dataframe column to pick dates from
date = Date()
dates_list = df_raw['Created at']
date.process_dates(dates_list)
#Test
print(date.end_month.upper())

# input_start_date = input("start date MMM YYYY")
# input_end_date = input("end date MMM YYYY")
last_weeks_highest_order_number = input("Enter last week's highest order no:  ")

# SHEET 1
# Open CSV in Excel and Copy and paste ALL data into google sheets in this folder... 
# Label this tab 'All Data MMM DD to MMM DD'

# SHEET 2
# Create new tab
# Duplicate ALL data tab to a new tab and name this tab
# 'WIP OrderExport_YYYY.MM.DD'
# Use this as the sheet's file name also


# On 'WIP OrderExport_YYYY.MM.DD'
# Reduce columns should have to 8 columns
# Order number, Email, Created at, Quantity, Item description, Refunded amount, Phone number, Name
# reduce down by dropping email, refund, created at, then add one col called collected
wip_order_export = df_raw[["Name", "Email", "Created at", "Lineitem quantity", "Lineitem name", "Refunded Amount", "Billing Phone", "Billing Name" ]]
wip_order_export.rename(columns = {'Name':'Order No.'}, inplace = True)

# Ensure that NAME and PHONE data are included
# Add 2 new columns; one for Vlookup names one for phone numbers
# See Vlookup tab for information on how to do this

# # check datatypes
# for index,n in enumerate(wip_order_export['Billing Name']): 
#     print(f'{n},{type(n)}, {wip_order_export["Billing Phone"][index]}', {type(wip_order_export["Billing Phone"][index])})


def fill_missing_values(dataframe, column):
    # populates empty fields with the previous populated field
    # assumes that the first entry for each customer always has name data.
    for index,n in enumerate(dataframe[column]): 
        if type(n) != str:
            dataframe[column][index] = dataframe[column][index-1]

def fill_missing_numbers(dataframe, column, corresponding_column):
    # populates empty fields with the previous populated field
    # assumes that the first entry for each customer always has name data.
    # does not populate an empty field if corresponding field is populated, as in 
    # case of withheld phone numbers.
    for index,n in enumerate(dataframe[column]): 
        if type(n) != str and type(corresponding_column[index]) != str: 
            dataframe[column][index] = dataframe[column][index-1]

            
fill_missing_numbers(wip_order_export, 'Billing Phone', wip_order_export['Billing Name'])
fill_missing_values(wip_order_export, 'Billing Name')

# Filter for Refunded amounts.
# Look these non $0 amounts in Shopify by searching with the order number.
# Notes will be left on the files relating to refunds.
# Make amends to the data according to the refund notes
refunds = wip_order_export.loc[wip_order_export['Refunded Amount'] > 0]
memberships = wip_order_export.loc[wip_order_export['Lineitem name'].str.contains("Membership Share")]
donations = wip_order_export.loc[wip_order_export['Lineitem name'].str.contains("TO DONATE")]
refunds = refunds.append([memberships, donations])

# test = pd.Series(['Mike', 'Alessa', 'Nick', 'Kim', 'Britney'])



# Add emails Billing Name and Billing Phone to a new tab called Vlookup
# Undertake the Vlookup - see Vlookup tab for notes
order_export = wip_order_export[['Order No.', 'Billing Name', 'Billing Phone', 'Email']]
order_export['Collected'] = ''
order_export.rename(columns = {'Billing Name':'Name', 'Lineitem quantity':'Qty', 'Lineitem name':'Item'}, inplace = True)
#re-order columns

# Duplicate to a new tab and call this 'OrderExport_YYYY.MM.DD'

# Look at last week's highest order number
# Any order number higher than that, highlight it green

# Reduce to orders for just this week
# Sort by item name and remove those that were already fulfilled/ or future orders. 
# Order numbers highlighted green should not be being deleted so if this occurs interrogate the data. Were they a 'day-of/ Sunday/ Monday/ Tuesday' purchase?

# Create new tab	
# Duplicate ORDER EXPORTS tab to new tab and create eg. CustPickupSheet_YYYY.MM.DD


# orders should be alphabetical by name.

# Reduce and re-order for the pickup sheet	
# Reduce columns required and add 'collected' column

# Donations	
# Copy donations gifted to the donations spreadsheet

# Remove donations gifted from Pickup Sheet

# Put donation requests into Donations sheet and Pickup sheet

# Membership	
# Put new members into MEMBERSHIP and NON MEMBER boxes into membership spreadsheet

# Create and format pickup sheet	
# On Pickup Sheet - Sort by name A-Z

# Create pivot table	
# Create Pivot table for summary data

# Shade the table with alternate customers shaded	
# Use the formula in the customer pickup sheet here to make the name shading easy (highlighted in green, column G)

# Hide shading formula column

# Format Pickup Sheet	
# Format cells - font, borders etc







#create a Pandas Excel writer using XlsxWriter as the engine
writer = pd.ExcelWriter(f'WIP OrderExport_{date.year}.{date.month}.{date.day}.xlsx', engine='xlsxwriter')

#write each DataFrame to a specific sheet # Only need 8 cols jfor df13
df_raw.to_excel(writer, sheet_name=f'All Data {date.start_month} {date.start_day} to {date.end_month} {date.end_day}', index=False)
wip_order_export.to_excel(writer, sheet_name=f'WIP OrderExport_{date.year}.{date.month}.{date.day}', index=False)
refunds.to_excel(writer, sheet_name=f'Refunds_Mem_Don_{date.year}.{date.month}.{date.day}', index=False)
order_export.to_excel(writer, sheet_name=f'Order Export_{date.year}.{date.month}.{date.day}', index=False)
# #close the Pandas Excel writer and output the Excel file
writer.save()



print('End of program')





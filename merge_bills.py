import pandas as pd

#replace empty titles in bills_introduced to 'Not_Applicable'. can also use replace + fillna but I was running into errors
bills_introduced = pd.read_excel('bills_introduced.xlsx')
bills_negatived = pd.read_csv('bills_negatived.csv')

bills_introduced['key'] = bills_introduced.apply(lambda row: str(row.year) + str(row.billno) + str(row.house_of_introduction) + row.title.lower(), axis=1)
bills_introduced=bills_introduced.replace({'\n': ' '}, regex=True)
bills_introduced['key']=bills_introduced['key'].replace({' ': ''}, regex=True)

bills_negatived['key'] = bills_negatived.apply(lambda row: str(row.year) + str(row.billno) + str(row.house_of_introduction) + row.title.lower(), axis=1)
bills_negatived['key']=bills_negatived['key'].replace({' ': ''}, regex=True)

bills_merged = pd.merge(bills_introduced, bills_negatived[['key','bill_status']],on='key', how='left')
bills_merged.to_csv('bills_merged.csv',',')
bills_negatived.to_csv('check_merge.csv',',')

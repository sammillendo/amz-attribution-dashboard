import pandas as pd

df1 = pd.read_csv('amazon.csv', usecols=('Date', 'Order','Line item', 'Total units sold', 'Total sales USD' ))
df2 = pd.read_csv('google.csv', header=2, usecols=('Day', 'Campaign', 'Ad group', 'Impressions', 'Clicks', 'Avg. CPC', 'Cost'))
print(df1)
#print(df2)

def amazon():
    new = df1.loc[df1.Order.str.startswith("GA")]
    return new
print(amazon())




#sum of click-throughs of order per date
#df_order_cts = df.groupby(['Date','Order'])['Click-throughs'].sum()
#print(df_order_cts)

#sum of total dpv of order per date
#df_order_dpv = df.groupby(['Date', 'Order'])['Total DPV'].sum()
#print(df_order_dpv)

#total units sold per order
#df_order_unit_sold = df.groupby('Order')['Total units sold'].sum()
#print(df_order_unit_sold)

#total units sold per date
#df_order_unit_sold_date = df.groupby(['Date', 'Order'])['Total units sold'].sum()
#print(df_order_unit_sold_date)

#total sales per order
#df_order_sales = df['Total sales USD'].str.strip('$').astype(float).sum()
#df_order_sales = '${:.2f}'.format(df_order_sales)
#print(df_order_sales)

#total sales of order per date
#df['Total sales USD'] = df['Total sales USD'].str.strip('$').astype(float)
#df_order_sales_date = df.groupby(['Date', 'Order'])['Total sales USD'].sum()
#df_order_sales = df.loc['Total sales USD'] = convert_to_dollar()
#print(df_order_sales)









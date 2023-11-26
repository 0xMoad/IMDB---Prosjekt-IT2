"""

  ____ _____ _____ __  __ __  __ _____ _   _ _____      __
 / ___|_   _| ____|  \/  |  \/  | ____| \ | | ____|  _ / /
 \___ \ | | |  _| | |\/| | |\/| |  _| |  \| |  _|   (_) | 
  ___) || | | |___| |  | | |  | | |___| |\  | |___   _| | 
 |____/ |_| |_____|_|  |_|_|  |_|_____|_| \_|_____| (_) | 
                                                       \_\



"""


import pandas as pd
import plotly.express as px

 
df = pd.read_csv('grossing.csv')
df['Lifetime Gross'] = df['Lifetime Gross'].replace('[\$,]', '', regex=True).astype(float) 
df['Lifetime Gross Formatted'] = '$' + df['Lifetime Gross'].apply(lambda x: "{:,}".format(x))
 
fig = px.scatter(df, x='Year', y='Lifetime Gross', size='Lifetime Gross', color='Title',
                 hover_name='Title',
                 title='Top 200 Grossing Movies',
                 labels={'Lifetime Gross': 'Lifetime Gross', 'Year': 'Year', 'Title': 'Title:'},
                 hover_data={'Year': True, "Lifetime Gross": False, 'Lifetime Gross Formatted': True, 'Title': False})

 
fig.update_layout(xaxis_title='Year', yaxis_title='Lifetime Gross Revenue ($)', plot_bgcolor='rgba(255,255,255,0)',  # transparent background
    xaxis=dict(showgrid=True, gridcolor='lightgray'),
    yaxis=dict(showgrid=True, gridcolor='lightgray'))
fig.update_traces(marker=dict(symbol='diamond'), selector=dict(mode='markers'))

 
fig.show()

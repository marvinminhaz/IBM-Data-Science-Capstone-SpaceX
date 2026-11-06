import os
import wget
import pandas as pd
import dash
import plotly.express as px
import plotly.graph_objects as go 
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

#Downloading dataset and reading it into a dataframe
dataset = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'
dataset_path = '../data/raw/spacex_launch_dash.csv'

if os.path.exists('../data/raw/spacex_launch_dash.csv'):
    dash_df = pd.read_csv(dataset_path)
    print('File present & read.')
else:
    wget.download(dataset, out='../data/raw/')
    dash_df = pd.read_csv(dataset_path)
    print('File downloaded and read.')

# Formatting dataframe
dash_df = dash_df.rename(columns={
    'Flight Number': 'Flight_Number',
    'Launch Site': 'Launch_Site',
    'Payload Mass (kg)': 'Payload_Mass_kg',
    'Booster Version' : 'Booster_Version',
    'Booster Version Category' : 'Booster_Version_Category'
})
dash_df = dash_df.drop('Unnamed: 0', axis=1)

#Variables for APP
launch_sites = list(dash_df.Launch_Site.values.unique())
dropdown_options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': site, 'value': site} for site in launch_sites
]

#DASH APP
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'text-align': 'center', 'color': '#503D36', 'font-size': '40'}
    ),
    html.Br(),
    
    dcc.Dropdown(dropdown_options, value='ALL', id='site-dropdown', placeholder="Select a Launch Site here"),

    html.Br(),

    html.Div(dcc.Graph(id='success-pie-chart')),

    html.Br(),

    html.P('Payload range (Kg):'),

    dcc.RangeSlider(
        dash_df.Payload_Mass_kg.min(), 
        dash_df.Payload_Mass_kg.max(), 
        value=[2121, 3412.50], id='payload-slider'
    ),

    html.Br(),

    html.Div(dcc.Graph(id='success-payload-scatter-chart'))
])

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)

def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(dash_df, values='class', names='Launch_Site', title='Combined Sucesses from ALL Launch Sites')
        return fig
    else:
        site_df = dash_df[dash_df['Launch_Site']==entered_site]
        site_df['Outcome'] = site_df['class'].map({0:'Failure', 1:'Success'})
        fig = px.pie(site_df, names='Outcome', title=f'Success vs Failure for: {entered_site}')
        return fig


if __name__ == '__main__':
    app.run()
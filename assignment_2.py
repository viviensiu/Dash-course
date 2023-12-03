#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:02:37 2023

@author: graeme
"""

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

filepath = "https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv"
df = pd.read_csv(filepath)

app = Dash(__name__)

# =============================================================================
# Exercise A
# =============================================================================
app.layout = html.Div([
     html.Div(className='row', children=[
         html.H1('Exercise A',
              style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
         
         html.Div(children ='US Agricultural Exports 2011' , id='my-title'),
     
         dcc.Dropdown(options=df.state, value=['Alabama','Arkansas'], id='state_dropdown', multi=True),

         dcc.Graph(id='graph1')
         ]),
     ])
# =============================================================================
# Exercise B
# =============================================================================
@callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='state_dropdown', component_property='value')
)
def update_graph(state_selected):
    # For state_dropdown without multi=True
    # df_country = df.loc[df['state'].str.contains(state_selected), ['state', 'beef','pork','fruits fresh']]
    df_country = df.loc[df['state'].isin(state_selected), :]
    return px.bar(df_country, x='state', y = ['beef','pork','fruits fresh'])
    
if __name__ == '__main__':
    app.run(debug=True)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:15:50 2023

@author: graeme
"""

from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

app = Dash(__name__)

# =============================================================================
# Exercise A
# =============================================================================
app.layout = html.Div([
    html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
    dcc.Dropdown(id="state-dropdown", options=df.state.unique(), value=["Alabama","Arkansas"], multi=True),
    html.Button(children='submit', id='state-button'), #, n_clicks=0),
    dcc.Graph(id="graph1"),
])

@app.callback(
    Output(component_id='graph1', component_property='figure'),
    #Input(component_id='state-dropdown', component_property='value')    
    State(component_id='state-dropdown', component_property='value'), 
    Input(component_id='state-button', component_property='n_clicks'),
    prevent_initial_call=True
)
def update_graph(states_selected, button_clicks):
    df_states = df[df.state.isin(states_selected)]
    if button_clicks > 0: 
        fig1 = px.bar(data_frame=df_states, x='state', y=['beef','pork','fruits fresh'])
        return fig1
    else:
        return px.bar()


# =============================================================================
# Exercise B
# =============================================================================
# =============================================================================
# app.layout = html.Div([
#     html.Div(id="my-title", children="Us Agricultural Exports in 2011"),
#     dcc.Graph(id="graph1"),
#     dcc.Interval(id='updates', interval=2000, n_intervals=0)
# ])
# 
# @app.callback(
#     Output(component_id='graph1', component_property='figure'),
#     Input(component_id='updates', component_property='n_intervals')
# )
# def update_graph(n):
#     if 0 < n < 6:
#         state_added = df.state[0:n] # take rows from zero to n
#         df_states = df[df.state.isin(state_added)]  # filter the dataframe (df) state column by state_added
#         fig1 = px.bar(data_frame=df_states, x='state', y=['beef','pork','fruits fresh'])
#         return fig1
#     else:
#         return px.bar()
# =============================================================================


if __name__ == '__main__':
    app.run(debug=True)

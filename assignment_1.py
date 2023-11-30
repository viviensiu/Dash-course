#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:21:43 2023

@author: graeme
"""

# =============================================================================
# import plotly
# import dash
# 
# print("plotly version=", plotly.__version__)
# print("dash version=", dash.__version__)
# =============================================================================

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# read dataset
filepath = "https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv"
df = pd.read_csv(filepath)

# get unique brands
list_brand = df['brand'].unique().tolist()
#print(list_brand)

# get unique groups and sort in asc order
list_group = sorted(df['group'].unique())
#print(list_group)

# get group labels
group_labels = ["Fenty Beauty's PRO FILT'R Foundation Only",
    "Make Up For Ever's Ultra HD Foundation Only",
    "US Best Sellers",
    "BIPOC-recommended Brands with BIPOC Founders",
    "BIPOC-recommended Brands with White Founders",
    "Nigerian Best Sellers",
    "Japanese Best Sellers",
    "Indian Best Sellers"]

# merge groups and labels into dictionary
dict_group = dict(zip(list_group, group_labels))

# create DAG grid. Set columnSize= sizeToFit for autofit to windows.
# Set pagination=True to enable pagination
# defaultColDef enables/disables resizing, sorting and filtering functions in each column
grid = dag.AgGrid(
    id="dag_df",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    columnSize="sizeToFit",
    defaultColDef={"resizable": True, "sortable": True, "filter": True},
    dashGridOptions={"pagination": True},
)

# create checklist for multiple selection on brands and/or products
list_product = df['product'].unique().tolist()
list_product_short = df['product_short'].unique().tolist()
dict_product = dict(zip(list_product_short, list_product))

# create scatterplot
fig_VS = px.scatter(df, 'V', 'S')
fig_VS.update_layout(    title="Foundation Shade",
    xaxis_title="Value/Brightness",
    yaxis_title="Saturation",)

# initialize app
app = Dash(__name__)

# =============================================================================
# Exercise A
# =============================================================================
app.layout =  html.Div([
     html.Div(className='row', children=[
         html.H1('Exercise A',
              style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
     
         dcc.Dropdown(options=list_brand, value='Revlon', id='dropdown_brand'),

         dcc.RadioItems(options=[{'label':v,'value':k}  for k,v in dict_group.items()], 
                        value='0', inline=False, id='radio_group')
         ]),
# =============================================================================
# Exercise B
# =============================================================================
    html.Div(className='row', children=[
         html.H1('Exercise B',
              style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    
    html.Div([grid]),
    ]),
# =============================================================================
# Exercise C
# =============================================================================
   html.Div(className='row', children=[
        html.H1('Exercise C',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
   
        dcc.Checklist(options = [{'label':v, 'value':k} for k,v in dict_product.items()],
                       id='checklist_product', inline=True),
        
        html.Button('Submit', id='button_checklist_product', n_clicks=0)
        
        
       ]),   
# =============================================================================
# Exercise D   
# =============================================================================
    html.Div(className='row', children=[
        html.H1('Exercise D',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
        
        dcc.Graph(figure=fig_VS, id='scatterplot_df')
        ])

])

if __name__ == '__main__':
    app.run(debug=True)

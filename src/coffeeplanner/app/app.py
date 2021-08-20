import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table

import datetime

from coffeeplanner.generate_couples import (
    generate_couple,
    list_names,
    couples_df,
    used_names,
    past_couples,
    couples,
    week
)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

tabs_styles = {
    'height': '40px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'color': '#5C6369'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#FF5500',
    'color': 'white',
    'padding': '6px'
}


dropdown_options=[]
for name in sorted(list_names):
    dropdown = {'label': name, 'value': name}
    dropdown_options.append(dropdown)


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.Div([
        html.Img(
            src=app.get_asset_url("Navara_Logo.png"),
            className="app__menu__img",
        ),
        html.Img(
            src=app.get_asset_url("coffee.png"),
            className="app__menu__img",
        )
    ]),
    html.H3('/ COFFEE APP', style={'color': '#FF5500'}),
    html.H3(f'Week {week}', id='week', style={'color': '#FFF'}),
    dcc.Tabs(id='tabs', children=[
        dcc.Tab(label='Genereer koppels', value='tab-1', style=tab_style, selected_style=tab_selected_style, children=[
            dcc.Dropdown(
                    id='dropdown',
                    options=dropdown_options,
                    style={'color': '#666', 'margin-top': '20px'},
                    placeholder="Selecteer je eigen naam",
            ),
            html.P('Zodra u uw naam selecteert en op de knop klikt, wordt er een koppel aangemaakt.'),
            html.Div(id='dd-output-container'),
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in couples_df[week].columns],
                data=couples_df[week].to_dict('records'),
                style_header={'backgroundColor': '#00345B'},
                style_cell={
                    'font_family': 'Avenir',
                    'font_size': '1.3rem',
                    'padding': '5px',
                    'backgroundColor': '#1E5078',
                    'color': 'white',
                    'textAlign': 'left'
                },
            ),
        ]),
        dcc.Tab(label='Koffie geschiedenis', value='tab-2', style=tab_style, selected_style=tab_selected_style, children=[
            html.P('Vind hier alle koffie geschiedenis!'),
            dash_table.DataTable(
                id='table1',
                columns=[{"name": i, "id": i} for i in past_couples['past_couples'].columns],
                data=past_couples['past_couples'].to_dict('records'),
                style_header={'backgroundColor': '#00345B'},
                style_cell={
                    'font_family': 'Avenir',
                    'font_size': '1.3rem',
                    'padding': '5px',
                    'backgroundColor': '#1E5078',
                    'color': 'white',
                    'textAlign': 'left'
                },
            )
        ]),
    ],
    style=tabs_styles),
])


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
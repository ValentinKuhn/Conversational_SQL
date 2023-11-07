from dash import html, dcc, Dash
import requests
from dash.dependencies import Input, Output, State
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Chat with the database', style={'textAlign': 'center'}),
    dcc.Input(
        id='input-box',
        type='text',
        placeholder='Type your SQL query here...',
        style={'width': '100%', 'padding': '10px 15px', 'margin': '0 0 10px 0'}  # Added style here
    ),
    dcc.Loading(
        id="loading",
        type="circle",
        children=[
            html.Button('Send', id='button'),  # You can also adjust button style if needed
            html.Div(id='output-box', style={"height": "400px", "overflow": "auto", "padding": "0 15px"}, children=[])
        ]
    )
])


@app.callback(
    Output('output-box', 'children'),
    Input('button', 'n_clicks'),
    State('input-box', 'value'),
    State('output-box', 'children')
)
def update_output(n_clicks, input_value, chat_history):
    if n_clicks is None or n_clicks == 0:
        return chat_history
    else:
        response = requests.post('http://gateway:5000/chat', json={'input': input_value})
        reply = response.json().get('reply')
        formatted_reply = reply.replace('\n', '<br>')
        new_chat_history = chat_history + [
            html.Div(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), style={"textAlign": "right", "color": "grey"}),
            html.Div(input_value, style={"background": "grey", "padding": "5px", "borderRadius": "5px"}),
            html.Div(dcc.Markdown(formatted_reply, dangerously_allow_html=True), style={"background": "lightblue", "padding": "5px", "borderRadius": "5px"}),
        ]
        return new_chat_history



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

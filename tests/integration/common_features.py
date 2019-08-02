from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
from time import sleep

PASS = 'passed'
FAIL = 'failed'


def simple_app_layout(
        component
):
    return [
        dcc.Input(id='prop-name'),
        dcc.Input(id='prop-value'),
        html.Div(id='pass-fail-div'),
        html.Button('Submit', id='submit-prop-button'),
        component
    ]


def simple_app_callback(
        app,
        dash_duo,
        component,
        component_id,
        test_prop_name,
        test_prop_value,
        process_value=None,
        validation_fn=None
):
    if validation_fn is None:
        def validation_fn(x): return x == test_prop_value

    if process_value is None:
        def process_value(x): return x

    @app.callback(
        Output(component_id, test_prop_name),
        [Input('submit-prop-button', 'n_clicks')],
        [State('prop-value', 'value')]
    )
    def setup_click_callback(nclicks, value):
        if nclicks is not None and nclicks > 0:
            return process_value(value)
        return None
    @app.callback(
        Output('pass-fail-div', 'children'),
        [Input(component_id, test_prop_name)]
    )
    def simple_callback(prop_value):
        passfail = PASS if validation_fn(prop_value) else FAIL
        return html.Div(passfail, id='passfail')

    dash_duo.start_server(app)
    dash_duo.wait_for_element('#'+component_id)

    input_prop_name = dash_duo.find_element('#prop-name')
    input_prop_value = dash_duo.find_element('#prop-value')

    input_send_button = dash_duo.find_element('#submit-prop-button')

    input_prop_name.send_keys(test_prop_name)
    input_prop_value.send_keys(test_prop_value)
    input_send_button.click()

    dash_duo.wait_for_element('#passfail')

    dash_duo.percy_snapshot(f'{component_id}_{test_prop_name}_{test_prop_value}')
    
    assert dash_duo.find_element('#passfail').text == PASS

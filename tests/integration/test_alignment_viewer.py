import dash
import dash_bio
import dash_html_components as html

from common_features import simple_app_layout, simple_app_callback

_data = None

with open(
        'tests/dashbio_demos/sample_data/alignment_viewer_p53.fasta', 'r'
) as f:
    _data = f.read()


def test_dbav001_hide_conservation(dash_duo):

    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.AlignmentChart(id='test-alignment-chart', data=_data)
    ))

    simple_app_callback(
        app,
        dash_duo,
        'test-alignment-chart',
        'showconservation',
        'False',
        process_value=lambda x: eval(x),
        validation_fn=lambda x: x is False
    )

    # TODO also assert that the length of the list containing all elements
    # returned by the selector for the conservation bar plot is 0


def test_dbav002_change_colorscale(dash_duo):

    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.AlignmentChart(id='test-alignment-chart', data=_data)
    ))

    simple_app_callback(
        app,
        dash_duo,
        'test-alignment-chart',
        'colorscale',
        'hydro',
    )


def test_dbav003_change_conservation_colorscale(dash_duo):

    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.AlignmentChart(id='test-alignment-chart', data=_data)
    ))

    simple_app_callback(
        app,
        dash_duo,
        'test-alignment-chart',
        'conservationcolorscale',
        'Blackbody'
    )

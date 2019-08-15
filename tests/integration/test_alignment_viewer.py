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

    assert len(dash_duo.find_elements('g.cartesianlayer.xy3')) == 0


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
        take_snapshot=True
    )

    # the heatmap background is an image, so we can't programmatically
    # assert that the colors are correct; this test requires a look at
    # the Percy snapshot that is taken


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

    # first bar should be black
    dash_duo.wait_for_style_to_equal(
        '#test-alignment-chart > div > div > div > div > svg:nth-child(1) > '
        'g.cartesianlayer > g.subplot.xy2 > g.plot > g > g > g > '
        'g:nth-child(1) > path', 'fill', 'rgb(0, 0, 0)')

    # second bar should be this orange color
    dash_duo.wait_for_style_to_equal(
        '#test-alignment-chart > div > div > div > div > svg:nth-child(1) > '
        'g.cartesianlayer > g.subplot.xy2 > g.plot > g > g > g > '
        'g:nth-child(2) > path', 'fill', 'rgb(230, 103, 0)')

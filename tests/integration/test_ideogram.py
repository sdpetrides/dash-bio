import json

import dash
import dash_bio
import dash_html_components as html

from common_features import simple_app_layout, simple_app_callback
from selenium.webdriver.support.ui import WebDriverWait


def test_dbid001_displayed_chromosomes(dash_duo):

    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.Ideogram(
            id='test-ideogram'
        )
    ))

    chromosome_set_new = [str(i+1) for i in range(5)]

    simple_app_callback(
        app,
        dash_duo,
        'test-ideogram',
        'chromosomes',
        json.dumps(chromosome_set_new),
        process_value=lambda x: json.loads(x),
        validation_fn=lambda x: json.dumps(x) == json.dumps(chromosome_set_new)
    )

    WebDriverWait(dash_duo.driver, 1).until(
        lambda _:
        len(dash_duo.find_elements('g.chromosome-set-container')) == 5
    )


def test_dbid002_click_rotation(dash_duo):

    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.Ideogram(
            id='test-ideogram'
        )
    ))

    simple_app_callback(
        app,
        dash_duo,
        'test-ideogram',
        'rotatable',
        'True',
        process_value=lambda x: x == 'True',
        validation_fn=lambda x: x is True
    )

    # ensure that it loads un-rotated
    WebDriverWait(dash_duo.driver, 1).until(
        lambda _: 'rotate(90)' in dash_duo.find_element(
            '#chr1-9606-chromosome-set').get_attribute('transform'))

    # click to rotate and ensure that the correct chromosome is rotated
    dash_duo.find_element('#chr1-9606-chromosome-set').click()

    # rotation shouldn't take more than 1-2 seconds
    WebDriverWait(dash_duo.driver, 1).until(
        lambda _: 'rotate(0)' in dash_duo.find_element(
            '#chr1-9606-chromosome-set').get_attribute('transform'))


def test_dbid003_click_rotation_disabled(dash_duo):
    app = dash.Dash(__name__)

    app.layout = html.Div(simple_app_layout(
        dash_bio.Ideogram(
            id='test-ideogram'
        )
    ))

    simple_app_callback(
        app,
        dash_duo,
        'test-ideogram',
        'rotatable',
        'False',
        process_value=lambda x: x == 'True',
        validation_fn=lambda x: x is False
    )

    WebDriverWait(dash_duo.driver, 1).until(
        lambda _: 'rotate(90)' in dash_duo.find_element(
            '#chr1-9606-chromosome-set').get_attribute('transform'))

    # click to rotate and ensure that the correct chromosome is rotated
    dash_duo.find_element('#chr1-9606-chromosome-set').click()

    WebDriverWait(dash_duo.driver, 1)

    assert 'rotate(90)' in dash_duo.find_element(
        '#chr1-9606-chromosome-set').get_attribute('transform')

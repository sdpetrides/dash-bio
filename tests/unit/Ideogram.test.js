import Ideogram from '../../src/lib/components/Ideogram.react.js';
import React from 'react';
import {mount, render} from 'enzyme';


test('Ideogram renders', () => {
    const component = render(<Ideogram id={'hi'}/>);
    expect(component.html()).toBeDefined();
});

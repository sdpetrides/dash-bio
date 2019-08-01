import Molecule2dViewer from '../../src/lib/components/Molecule2dViewer.react.js';
import React from 'react';
import {mount, render} from 'enzyme';
import data from './data/mol2d_buckminsterfullerene.json';


test('Mol2D renders', () => {
    const component = render(<Molecule2dViewer modelData={data} />);
    expect(component.html()).toBeDefined();
});

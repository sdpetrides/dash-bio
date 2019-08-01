import Molecule3dViewer from '../../src/lib/components/Molecule3dViewer.js';
import React from 'react';
import {mount, render} from 'enzyme';
import modelData from './data/mol3d_model_sample.json';


test('Mol3D renders', () => {
    const component = render(<Molecule3dViewer modelData={modelData} />);
    expect(component.html()).toBeDefined();
});

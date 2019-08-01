import SequenceViewer from '../../src/lib/components/SequenceViewer.react.js';
import React from 'react';
import {mount, render} from 'enzyme';
import seq from './data/sequence_viewer_P01308.fasta';


test('SequenceViewer renders', () => {
    const component = render(<SequenceViewer sequence={seq} />);
    expect(component.html()).toBeDefined();
});

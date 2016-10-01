import React from "react"
import { render } from "react-dom"

import SampleApp2Container from "./containers/SampleApp2Container"

class SampleApp2 extends React.Component {
  render() {
    return (
      <SampleApp2Container />
    )
  }
}

render(<SampleApp2 />, document.getElementById('SampleApp2'))

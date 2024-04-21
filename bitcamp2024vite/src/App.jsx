import './styles.css'
import Hello from './components/hello'
import Textbox from './components/Text'
/*import Keywords from './components/Keywords'
import Definitions from './components/Definitions'*/

function App() {

  return (
    <div className="App">
      <Textbox />
      {/*<div className = "keywords"><Keywords /></div>
      <div className = "textbox"><Textbox /></div>
      <div className = "def"><Definitions /></div>*/}
    </div>
  )
}

export default App

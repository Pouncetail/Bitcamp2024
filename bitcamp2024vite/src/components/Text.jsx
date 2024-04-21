import {useState} from 'react'
import axios from 'axios'

export default function TextBox(){
    const [text, setText] = useState("");
    const [stringl, setString] = useState("");
    const [defs, setDefs] = useState("")
    var dict = {}
    const getapi = async() => {
        dict = {}
        const response = await axios.get("http://localhost:8080/pythonreturn")
        setString(response.data[0])
        for (var word in response.data[1]){
            dict[word] = response.data[1][word]
            /*setDict({...dict,
                word: response.data[1][word]})*/
            console.log(dict)
            console.log(dict[word])
        }
        setDefs(JSON.stringify(dict))
    }
    const checkdict = async() => {
        console.log(dict)
    }
    
    return (
        /*<div>
            <form>
                <textarea onChange={(e) => setText(e.target.value)} cols = "70"
                rows = "10"></textarea>
            </form>
            <button type="button" id="form1"
            onClick = {getapi}>Submit</button>
            <div className="content" dangerouslySetInnerHTML={{__html: stringl}}></div>
            <div id = "definitions"></div>
        </div>*/
        <main>
        <div className="flexcont">
          <div className="middle">
            <h1 className="title">Cramberry bot</h1>
            <div className="textbox">
              <p> Put your text here! </p>
            </div>
  
            <form>
              <textarea
                onChange={(e) => setText(e.target.value)}
                type="text"
                id="blacktext"
                cols={70}
                rows={10}
              ></textarea>
              <p></p>
              <button type="button" id="form1" onClick = {getapi}>
                Submit
              </button>
            </form>
            <p>{stringl}</p>
            <div id="output"></div>
          </div>
          <div className="left" id="left">
            <p>{text}</p>
          </div>
          <div className="right" id="right">
            <p>{defs}</p>
          </div>
        </div>
      </main>
    )
}
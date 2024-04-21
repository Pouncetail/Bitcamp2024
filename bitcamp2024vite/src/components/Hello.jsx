const name = "rob";

function displayMessage(props){
    return props.name;
}

function Hello(props){
    return (
        <div>
            <h1>hello from here {displayMessage(props)}</h1>
            <p> kekekek </p>
        </div>);
}

export default Hello
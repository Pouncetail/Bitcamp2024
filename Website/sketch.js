const text1 = document.getElementById("blacktext");
const btn1 = document.getElementById("form1");
const out1 = document.getElementById("output");
const left = document.getElementById("left");
const right = document.getElementById("right");

function fun1() {
    out1.textContent = text1.value;
    left.textContent = text1.value;
    right.textContent = text1.value;
}

btn1.addEventListener("click", fun1);
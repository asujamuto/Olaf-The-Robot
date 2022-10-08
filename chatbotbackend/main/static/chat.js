



const message = document.getElementById("text");
const menu = document.querySelector('#chat-menu');
const button = document.querySelector("#submit");

let count = 0




function createMenuItem(name) 
{
    let li = document.createElement('li');
    li.textContent = name;
    if(count % 2 == 0) 
    { 
        li.className = "user-message message" 
    }
    else if(count % 2 != 0) 
    { 
        li.className = "message"
    }

    count++;

    return li;
}


let tab = Array()

button.addEventListener("click", () => {

    let val = document.getElementById('text').value;

    window.localStorage.setItem("messages", val)

    /*
    tab = JSON.parse(window.localStorage.getItem("messages"));

    tab.push(val)

    window.localStorage.setItem("messages", JSON.stringify(tab));
    
    //localStorage.clear();
    */
});




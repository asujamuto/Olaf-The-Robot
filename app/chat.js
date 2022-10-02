




let message = document.getElementById("text")
const menu = document.querySelector('#chat-menu');
let button = document.querySelector("#submit");
let count = 0


function createMenuItem(name) 
{
    let li = document.createElement('li');
    li.textContent = name;
    if(count % 2 == 0) 
    { 
        li.className = "chatbot-message" 
    }
    else if(count % 2 != 0) 
    { 
        li.className = "your-message"
    }

    count++;

    return li;
}



button.addEventListener("click", () => {

    let val = document.getElementById('text').value;
    console.log(val);

    //node.js zmienna val jako data sent
    let new_val = () =>
    {
        return val;
    }
    module.exports = new_val;

    menu.appendChild(createMenuItem(val))
});




const spawner = require('child_process').spawn

//object
const data_to_pass_in = {
    data_sent: 'Send this to python script',
    data_returned: undefined
};



const python_process = spawner('python', ['./python.py', JSON.stringify(data_to_pass_in)]);


python_process.stdout.on('data', (data) => {
    //console.log('Data received from python script:', JSON.parse(data.toString()));
    python_answ = JSON.parse(data.toString());
    python_answ = python_answ.data_returned
    
    console.log('')
    console.log(data_to_pass_in.data_sent)
    console.log(python_answ)
    console.log('')
   
});




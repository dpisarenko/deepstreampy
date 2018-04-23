var deepstream = require('deepstream.io-client-js')
const client = deepstream('localhost:6021')

client.on('error', (error,event,topic) => {
  console.log(error, event, topic);
})

client.on('connectionStateChanged', connectionState => {
  console.log(connectionState);
})

client.login({username: 'userA', password: 'password'}, (success, data) => {
  if (success) {
    console.log("Login successful");
  } else {
    console.log(data);
  }
})

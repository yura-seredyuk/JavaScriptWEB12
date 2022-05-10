// Ajax

// Client to server -> Server select data from DataBase -> Server working with selected data and send it -> Client get data and represent it


// Request -> Select -> Response -> Webbrowser 

// console.log('Client: want to get todo list data')
// console.log('...')
// console.log('Server: select data fron DB')
// console.log('...')
// console.log('DB: working!')
// console.log('...')
// console.log('Server: transform data and sent for client')
// console.log('...')
// console.log('Client: get response and show it')

// console.log('-----------------')
// console.log('Client: want to get todo list data')
// console.log('...')
// setTimeout(()=>{
//     console.log('Server: select data fron DB')
//     console.log('...')
//     setTimeout(()=>{
//         console.log('DB: working!')
//         console.log('...')
//         setTimeout(()=>{
//             console.log('Server: transform data and sent for client')
//             console.log('...')
//             setTimeout(()=>{
//                 console.log('Client: get response and show it')        
//             },1000)
//         },1000)
//     },1000)
// },2000)

// let i = 0;
// setInterval(()=>{
//     console.log(i)
//     i++
// }, 1000)

// // Promise
// console.log('-----------------')
// console.log('Client: want to get todo list data')
// console.log('...')
// let promise = new Promise(function(resolve, reject){
//     setTimeout(()=>{
//         console.log('Server: select data from DB')
//         console.log('...')
//         resolve('Server...')
//     },2000)
// })
// promise.then(function(){
//     console.log('THEN')
//     return new Promise(function(resolve, reject){
//         setTimeout(()=>{
//             console.log('DB: working!')
//             console.log('...')
//             let todos = [
//                 {'date': '22.04.2022', 'text':'clean room'},
//                 {'date': '23.04.2022', 'text':'cook eggs'}
//             ]
//             // resolve(todos)
//             reject('DataBase is not working!')
//         },1000)
//     })
// }).then(function(DBResponse){
//     return new Promise(function(resolve, reject){
//         setTimeout(()=>{
//             console.log('Server: transform data and sent for client')
//             console.log('...')
//             let response = DBResponse.map(todo=>{
//                 return {
//                     'date': todo.date,
//                     'message': todo.text,
//                     'style':todo.date=='21.04.2022'?'red':'green'
//                 }
//             })
//             resolve(response)
//         },1000)
//     })
// }).then(function(todoList){
//     setTimeout(()=>{
//         for(item of todoList){
//             console.log(item)
//         }
//     },1000)
// }).catch(function(error){
//     console.log('Catch: ',error)
// }).finally(function(){
//     console.log('The end')
// })


// function load(){
//     fetch('https://jsonplaceholder.typicode.com/todos/')
//     .then(response => response.json())
//     .then(json => {
//       console.log(json)
//       document.getElementById('todoList').innerHTML=''
//       for(item of json){
//           let li = document.createElement('li')
//           li.textContent = `${item.id} -- ${item.title}`
//           li.classList.add(item.completed?'completed':'incompleted')
//           todoList.append(li)
//       }
//     })
// }

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Host': 'community-open-weather-map.p.rapidapi.com',
		'X-RapidAPI-Key': '0a92c9c109msh31bcf7e8cb7b25dp1cb78fjsn1504a6c7a6ac'
	}
};

fetch('https://community-open-weather-map.p.rapidapi.com/weather?q=London%2Cuk&lat=0&lon=0&callback=test&id=2172797&lang=null&units=imperial&mode=xml', options)
	.then(response => response.json())
	.then(response => console.log(response))
	.catch(err => console.error(err));  
            
    


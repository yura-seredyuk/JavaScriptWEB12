// let person = {
//     'first_name': 'Bob',
//     'last_name': 'Marli',
//     'age':50
// }

// console.log(person)
// console.log(person.age)

// function hideSequredFields(key,value){
//     if(key==='age' || key==='last_name'){
//         return undefined
//     }
//     else {
//         return value
//     }
// }

// // JSON
// json = JSON.stringify(person,hideSequredFields)

// console.log(json)

// response = JSON.parse(json)
// console.log(response)

//         XMLHttpRequest
// const url = 'https://swapi.dev/api/people/1/'

// let swapi = new XMLHttpRequest()

// console.log(swapi.readyState) // 0

// swapi.open('GET',url)

// console.log(swapi.readyState) // 1

// swapi.send()
// console.log(swapi.readyState) //1
// swapi.onreadystatechange = function(){
//     if(swapi.readyState===4){
//         console.log(swapi.readyState) //4
//         // console.log(JSON.parse(swapi.response))
//     } 
//     else {
//         console.log(swapi.readyState) //2 // 3
//     }
// }
// swapi.onload = function(){
//     console.log(swapi.readyState) //4
//     // console.log(swapi.status, swapi.statusText)
//     if(swapi.status !== 200){
//         console.log(`SWAPI Error! Status ${swapi.status}.`)
//     } else {
//         let person = JSON.parse(swapi.response)
//         console.log(person)
//     }
// }
// const url = 'https://swapi.dev/api/people/1/'


// let $person = document.querySelector('#person') 

// function loadData(url,target){
//     let server = new XMLHttpRequest()
//     server.open('GET',url)
//     server.send()
//     server.onload = function(){
//         if(server.status !== 200){
//             console.log(`SWAPI Error! Status ${server.status}.`)
//         } else {
//             let person = JSON.parse(server.response)
//             showData(person, target)
//         }
//     }
// }

// function showData(obj, target='person'){
//     console.log(obj)
//     for(key in obj){
//         // console.log(key, obj[key])
//         if(!Array.isArray(obj[key]) && !obj[key].includes('http') && !obj[key].includes('2014')){
//             let title = key.replace('_', ' ').split('')
//             title[0] = title[0].toUpperCase()
//             let html = `<b>${title.join('')}</b> <i>${obj[key]}</i><br/>`
//             document.querySelector(`#${target}`).insertAdjacentHTML('beforeend',html)    
//         }
//         else if (key == 'homeworld'){
//             let title = key.split('')
//             title[0] = title[0].toUpperCase()
//             let html = `<h4>${title.join('')}:</h4>`
//             document.querySelector('#homeworld').insertAdjacentHTML('beforeend',html)
//             loadData(obj[key], 'homeworld')
//         }
//         else if (key == 'starships'){
//             let title = key.split('')
//             title[0] = title[0].toUpperCase()
//             let html = `<h4>Starships:</h4>`
//             document.querySelector('#starships').insertAdjacentHTML('beforeend',html)
//             for( url of obj['starships']){
//                 loadData(url, 'starships')
//             }
//         }
//     }
//     // setTimeout(()=>{
//     //     if (Object.keys(obj).indexOf('starships')>0){
//     //         let title = key.split('')
//     //         title[0] = title[0].toUpperCase()
//     //         let html = `<h4>Starships:</h4>`
//     //         document.querySelector('#starships').insertAdjacentHTML('beforeend',html)
//     //         for( url of obj['starships']){
//     //             loadData(url, 'starships')
//     //         }
//     //     }
//     // }, 100);
    
// } 

// loadData('https://swapi.dev/api/people/1/')
// // loadData('https://swapi.dev/api/people/2/')


// let url = 'https://pixabay.com/api/?key=17057678-b4c4954d8c62e2cb084b2680c&q=white+dogs&image_type=photo&pretty=true&per_page=5'

let url = 'https://pixabay.com/api/videos/?key=17057678-b4c4954d8c62e2cb084b2680c&q=yellow+flowers&pretty=true'
let img_gallery = document.querySelector('.img_gallery')

function loadData(url){
    let server = new XMLHttpRequest()
    server.open('GET',url)
    server.send()
    server.onload = function(){
        if(server.status !== 200){
            console.log(`SWAPI Error! Status ${server.status}.`)
        } else {
            let response = JSON.parse(server.response)
            console.log(response)
            buildGallery(response)
        }
    }
}
function buildGallery(data){
    img_gallery.innerHTML=''
    for(item of data['hits']){
        // let img = document.createElement('img')
        // img.setAttribute('src', item['webformatURL'])
        // img_gallery.append(img)
        let img = document.createElement('iframe')
        img.setAttribute('src', item['videos']['medium']['url'])
        img_gallery.append(img)
    }   
}

loadData(url)
searchForm.submit.addEventListener('click',(event)=>{
    event.preventDefault()
    let q = searchForm.query.value.replace(' ','+'),
        per_page=searchForm.count.value

    console.log(q)
    let url = `https://pixabay.com/api/?key=17057678-b4c4954d8c62e2cb084b2680c&q=${q}&image_type=photo&pretty=true&per_page=${per_page}`
    loadData(url)
})
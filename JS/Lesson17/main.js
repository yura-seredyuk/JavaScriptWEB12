// console.log(mainForm.firstname.value)
// console.log(mainForm.color.value)
// cb = document.querySelectorAll('input[name="ch"]')
// rb = document.querySelectorAll('input[name="radio"]')
// console.log(cb)
// mainForm.submit.addEventListener('click', (event)=>{
//     event.preventDefault()
//     console.log(mainForm.color.value)
//     for(item of cb){
//         if(item.checked){
//             console.log(item.nextSibling.textContent)
//         }
        
//     }
//     for(item of rb){
//         if(item.checked){
//             console.log(item.nextSibling.textContent)
//             console.log(item.value)
//         }
        
//     }
// })

// local storage
// localStorage.setItem('myItem', '{"key":"value"}')
// localStorage.setItem('myItem2', '{"key":"value"}')

// data = JSON.parse(localStorage.getItem('myItem'))
// console.log(data)
// // localStorage.removeItem('myItem')
// // localStorage.clear()


// // session storage
// sessionStorage.setItem('myItem', '{"key":"value"}')
// sessionStorage.setItem('myItem2', '{"key":"value"}')

// data = JSON.parse(sessionStorage.getItem('myItem'))
// console.log(data)
// localStorage.removeItem('myItem')
// sessionStorage.clear()

dataBase = [
    {'login':'admin',
    'email':'admin@mail',
    'password':'admin'},
    {'login':'user',
    'email':'user@mail',
    'password':'user'}
]
function hideSequredFields(key,value){
    if(key==='password'){
        return undefined
    }
    else {
        return value
    }
}

LogIn.addEventListener('click', (event)=>{
    
    console.log('LogIn')
    if(regForm.login.value.trim() && regForm.password.value.trim()){
        login = regForm.login.value.trim()
        password = regForm.password.value.trim()
        let flag = false
        for(user of dataBase){
            if(login === user.login && password === user.password){
                alert('Logged in')
                flag = true
                data = JSON.stringify(user, hideSequredFields)
                console.log(data)
                localStorage.setItem('loggedUser', data)
                break
            }
        }
        if(!flag){
            event.preventDefault()
            alert('Wrong email or password!')
        }
    }
    else {
        event.preventDefault()
        alert('Incorrect data!')
    }
})
regForm.SignIn.addEventListener('click', (event)=>{
    event.preventDefault()
    console.log('SignIn')
    if(regForm.login.value.trim() 
        && regForm.password.value.trim() 
        && regForm.email.value.trim()){
            login = regForm.login.value.trim()
            email = regForm.email.value.trim()
            password = regForm.password.value.trim()
            let flag = false
            for(user of dataBase){
                if(login === user.login){
                    alert('This login is already exist!')
                    flag = true
                    break
                }
            }
            if(!flag){
                dataBase.push({'login': login,
                                'email': email,
                                'password': password})
                alert('You are registered!')
            } 
    }
    else {
        alert('Incorrect data!')
    }
    console.log(dataBase)
})
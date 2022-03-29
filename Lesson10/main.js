// let x = 10
// function name(param){
//     param++
//     // return param
// }

// function name(x){
//     x++
// }

// name(x)
// console.log(name(10))
// console.log(x)
// (param)=>{
//     param++
//     return param
// }
// let x = 0
// function* gen(){
//     yield ++x
// } 

// console.log(gen().next().value)
// console.log(gen().next().value)
// console.log(gen().next().value)
// console.log(gen().next().value)

// function inc(add){
//     let x = 10
//     return x + add
// }

// console.log(inc(5))

// function up(param){
//     function down(arg){
//         return arg + 2
//     }
//     return down(param)
// }

// console.log(up(2))


// text = "Some text   "

// console.log(text[0])
// console.log(text.trim())
// console.log(text.length)

// email = 'mymail@gmail.com'
// domen_list = ['gmail', 'itstep']
// console.log(email.includes('@'))
// console.log(email.indexOf('@'))
// console.log(email.split('@')[1].split('.'))
// if(domen_list.includes(email.split('@')[1].split('.')[0])){
//     console.log(true)
// }

// let $li = document.getElementsByTagName('li')
// console.log($li)

// const $PAR = document.getElementById('par')
// console.log($PAR)

// console.log(par)

// let $text = document.getElementsByClassName('text')
// console.log($text)

// let $title_2  = document.querySelector('p#par + h3')
// console.log($title_2)

// let $buttons = document.querySelectorAll('button')
// console.log($buttons)

// let border_width = 3
// let color_list = ['red', 'green', 'yellow']

// $buttons[0].addEventListener('click',()=>{
//     $title_2.style.border = `${border_width}px solid red`
// })

// $buttons[1].addEventListener('click',()=>{
//     $title_2.style.border = `${border_width}px solid green`
// })

// function  make_border(border_width, color){
//     $title_2.style.border = `${border_width}px solid ${color}`
// }

// for(let i = 0; i < $buttons.length; i++){
//     $buttons[i].addEventListener('click',()=>{
//         $title_2.style.border = `${border_width}px solid ${color_list[i]}`
//     })
// }

// let $p = document.getElementsByTagName('p')
// console.log($p)
// let flag
// for(let i = 0; i < $p.length; i++){
//     flag = true
//     $p[i].addEventListener('click',clicker)
// }

// function clicker(){
//     this.style.color = flag?'red':'black'
//     flag = !flag
// }
// console.log(this)


// function fact(n){
//     f = 1
//     for(let i = 1; i <= n; i++){
//         f *= i
//     }
//     return f
// }

// console.log(fact(5))

    // n   i   f   
    // 5       1
    // 5   1   1
    // 5   2   2
    // 5   3   6
    // 5   4   24
    // 5   5   120
    // 5   6

// function fact_r(n){
//     if(n == 0) return 1
//     return fact_r(n-1) * n
// }

// console.log(fact_r(5))

    // n  fact_r 
    // 5   (4) * 5
    // 4   (3) * 4
    // 3   (2) * 3
    // 2   (1) * 2
    // 1   (0) * 1
    // 0   1

    config = [
        {
            "color": "black",
            "border": "5px solid red",
            "border-radius": "0",
            "background-color": "orange",
            "font-family": "'Courier New', Courier, monospace",
            "font-size": "20px",
            "font-weight": "normal",
            "font-style": "italic",
            "width": "700px",
            "height": "300px",
        },
        { "color": "black",
            "border": "5px solid orange",
            "border-radius": "0",
            "background-color": "orange",
            "font-family": "'Courier New', Courier, monospace",
            "font-size": "20px",
            "font-weight": "normal",
            "font-style": "italic",
            "width": "700px",
            "height": "300px",},
        {  "color": "black",
            "border": "5px solid blue",
            "border-radius": "0",
            "background-color": "orange",
            "font-family": "'Courier New', Courier, monospace",
            "font-size": "20px",
            "font-weight": "normal",
            "font-style": "italic",
            "width": "700px",
            "height": "300px",},
        { "color": "black",
            "border": "5px solid yellow",
            "border-radius": "0",
            "background-color": "orange",
            "font-family": "'Courier New', Courier, monospace",
            "font-size": "20px",
            "font-weight": "normal",
            "font-style": "italic",
            "width": "700px",
            "height": "300px",},
        { "color": "black",
            "border": "5px solid green",
            "border-radius": "0",
            "background-color": "orange",
            "font-family": "'Courier New', Courier, monospace",
            "font-size": "20px",
            "font-weight": "bold",
            "font-style": "italic",
            "width": "700px",
            "height": "300px",}
    ]
    
    let $buttons = document.querySelectorAll('button')

    // function box_cofig(conf_obj){
    //     style = ''
    //     target = document.getElementById('par')
    //     for (key in conf_obj){
    //         style += `${key}: ${conf_obj[key]}; `
    //     }
    //     // target.style.color = conf_obj.color
    //     // target.style.border = conf_obj.border
    //     // target.style.fontWeight = conf_obj['font-weight']

    //     target.style = style
    //     // target.setAttribute('style',"border: 5px solid green;")
    // }
    // // box_cofig(config[4])
    // for(let i = 0; i < $buttons.length; i++ ){
    //     $buttons[i].addEventListener('click', ()=>{
    //         box_cofig(config[i])
    //     })
    // }
    
    target_element = document.getElementById('par')

    for(let i = 0; i < $buttons.length; i++ ){
        $buttons[i].addEventListener('click', ()=>{
            class_list = target_element.classList
            if (class_list.contains('default')){
                class_list.remove('default')
            }
            for(item of class_list){
                if(item.slice(0,2) == 'st'){
                    class_list.remove(item)
                    break
                }
            }
            class_list.add(`st${i+1}`)
        })
    }


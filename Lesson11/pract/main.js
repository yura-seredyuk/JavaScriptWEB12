// import {data_base} from './data_base'

// let db = data_base
// console.log(db)
let data_base = [
    ["1 - Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos consequuntur, ratione excepturi quos ad placeat ullam libero eaque blanditiis neque. Aliquam iusto fugit error voluptas repudiandae soluta molestias corrupti itaque?", 'https://static.vecteezy.com/system/resources/previews/001/204/380/large_2x/shield-png.png'],
    ["2 - Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos consequuntur, ratione excepturi quos ad placeat ullam libero eaque blanditiis neque. Aliquam iusto fugit error voluptas repudiandae soluta molestias corrupti itaque?",'https://static.vecteezy.com/system/resources/previews/001/204/380/large_2x/shield-png.png'],
    ["3 - Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos consequuntur, ratione excepturi quos ad placeat ullam libero eaque blanditiis neque. Aliquam iusto fugit error voluptas repudiandae soluta molestias corrupti itaque?",'https://static.vecteezy.com/system/resources/previews/001/204/380/large_2x/shield-png.png'],
    ["4 - Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos consequuntur, ratione excepturi quos ad placeat ullam libero eaque blanditiis neque. Aliquam iusto fugit error voluptas repudiandae soluta molestias corrupti itaque?",'https://static.vecteezy.com/system/resources/previews/001/204/380/large_2x/shield-png.png'],
    ["5 - Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos consequuntur, ratione excepturi quos ad placeat ullam libero eaque blanditiis neque. Aliquam iusto fugit error voluptas repudiandae soluta molestias corrupti itaque?",'https://static.vecteezy.com/system/resources/previews/001/204/380/large_2x/shield-png.png'],
    ["6 - Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos consequuntur, ratione excepturi quos ad placeat ullam libero eaque blanditiis neque. Aliquam iusto fugit error voluptas repudiandae soluta molestias corrupti itaque?", 'https://i.pinimg.com/originals/d1/6e/65/d16e656b8d40f345d574cf3485ffeb00.jpg']
]

let close_btn = document.querySelector('span.close'),
    overlay = document.querySelector('div.overlay'),
    info = document.querySelector('div.info'),
    main_menu_li = document.querySelectorAll('ul.main-menu>li'),
    sub_menu = document.querySelectorAll('ul.sub-menu'),
    sub_menu_li = document.querySelectorAll('ul.sub-menu>li')
// console.log(sub_menu)

close_btn.addEventListener('click', ()=>{
    overlay.style.display = 'none' 
})

overlay.addEventListener('click', ()=>{
    overlay.style.display = 'none' 
})

info.addEventListener('click', (event)=>{
    event.stopPropagation()
})

for(let i = 0; i < main_menu_li.length; i++){
    main_menu_li[i].addEventListener('click', (event)=>{
        sub_menu[i].style.display = sub_menu[i].style.display == 'block'?'none':'block'
    })
}
for(let i = 0; i < sub_menu_li.length; i++){
    sub_menu_li[i].addEventListener('click', (event)=>{
        event.stopPropagation()
        overlay.style.display = 'flex'
        if(info.children[0].tagName === 'P'){
            info.children[0].textContent = data_base[i][0]
        }
        info.style.backgroundImage = `url(${data_base[i][1]})`
    })
    sub_menu_li[i].addEventListener('mouseover', (event)=>{
        event.target.style.marginLeft = '10px'
    })
    sub_menu_li[i].addEventListener('mouseout', (event)=>{
        event.target.style.marginLeft = '0px'
    })
}

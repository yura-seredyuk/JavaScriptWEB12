let img_list = document.querySelectorAll('.gallery ul>li>img'),
    slider = document.querySelector('.gallery .slider'),
    leftArrow = document.querySelector('.gallery .left-arrow'),
    rightArrow = document.querySelector('.gallery .right-arrow')


// console.log(img_list)

let flag = false,
    prew = 0

function load_image(ind){
    img_list[ind].classList.add('active_image')
        console.log(img_list[ind].getAttribute('src'))
        slider.style.backgroundImage = `url(${img_list[ind].getAttribute('src')})`
        if(ind !== prew){
            img_list[prew].classList.remove('active_image')
        }
        prew = ind
}

function big(node_list, ind){
    node_list[ind].style.opacity = '1'
    node_list[ind].style.transform = 'scale(1.5)'
    node_list[ind].style.zIndex = '999'
}
function big_(target){
    target.style.opacity = '1'
    target.style.transform = 'scale(1.5)'
    target.style.zIndex = '999'
}

function small(node_list, ind){
    node_list[ind].style.opacity = '0.5'
    node_list[ind].style.transform = 'scale(1)'
    node_list[ind].style.zIndex = '0'
}

load_image(0)

for(let i=0; i<img_list.length; i++){
    img_list[i].addEventListener('click', (event)=>{
        load_image(i)
    })
    // img_list[i].addEventListener('mouseover', (event)=>{
    //     // big(img_list, i)
    //     big_(event.target)
    // })
    img_list[i].addEventListener('mouseover', function(){
        // big(img_list, i)
        big_(this)
    })
    img_list[i].addEventListener('mouseout', (event)=>{
        small(img_list, i)
    })
}

leftArrow.addEventListener('click',(event)=>{
    if(prew == 0){
        load_image(img_list.length-1)
    } else {
        load_image(prew-1)
    }
})

p.remove()

rightArrow.addEventListener('click',(event)=>{
    if(prew == img_list.length-1){
        load_image(0)
    } else {
        load_image(prew+1)
    }
})

// document.body.addEventListener('mousemove', (event)=>{
//     console.log(event.offsetX)
// })
// window.addEventListener('mousemove', (event)=>{
//     console.log(event.offsetX)
// })

// let x = document.body.getBoundingClientRect().bottom = 10
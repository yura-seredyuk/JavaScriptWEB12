// create elements
let gallery = document.createElement('DIV'),
    bigSlider = document.createElement('DIV'),
    bigLeftArr = document.createElement('SPAN'),
    bigRightArr = document.createElement('SPAN'),
    smallSlider = document.createElement('DIV'),
    smallLeftArr = document.createElement('SPAN'),
    imgList = document.createElement('UL'),
    smallRightArr = document.createElement('SPAN')

// imgItem selectedImg
// add class
gallery.classList.add('gallery')
bigSlider.classList.add('bigSlider'),
bigLeftArr.classList.add('bigLeftArr')
bigRightArr.classList.add('bigRightArr')
smallSlider.classList.add('smallSlider')
smallLeftArr.classList.add('smallLeftArr')
imgList.classList.add('imgList')
smallRightArr.classList.add('smallRightArr')

// add global elements into html
document.body.insertAdjacentElement('afterbegin',gallery)
gallery.append(bigSlider,smallSlider)
bigSlider.append(bigLeftArr,bigRightArr)
smallSlider.append(imgList,smallLeftArr,smallRightArr)

// fill arrows
bigLeftArr.textContent="➤"
bigRightArr.textContent="➤"
smallLeftArr.textContent="➤"
smallRightArr.textContent="➤"

// load gallery
let url = `https://pixabay.com/api/?key=17057678-b4c4954d8c62e2cb084b2680c&q=yellow+flowers&image_type=photo&pretty=true`

function loadImages(url){
    let server = new XMLHttpRequest()
    server.open('GET', url);
    server.send();
    server.onload = function(){
        if (server.status !== 200){
            console.log("Error!")
        } else {
            response = JSON.parse(server.response).hits
            // console.log(response)
            showImages(response)
        }
    }
}
function showImages(list){
    // console.log(list)
    for(item of list){
        // console.log(item.webformatURL)
        let li = document.createElement('LI')
        li.classList.add('imgItem')
        li.style.backgroundImage = `url(${item.webformatURL})`
        imgList.append(li)
    }
    // calculate width of the imgList block
    imgListWidth = list.length * 150
    imgList.style.width = imgListWidth+'px'
    imgListLeft = 0
    let imgItems = document.querySelectorAll('li.imgItem')
    // load first image and remember prew position
    let prew = loadImg(list, imgItems, 0)
    // add click methods for all small pictures
    for(let i = 0; i < imgItems.length; i++){
        imgItems[i].addEventListener('click', ()=>{
            prew = loadImg(list, imgItems, i, prew)
        })
    }
    // arrows
    smallLeftArr.addEventListener('click', ()=>{
        imgListLeft = moveLeft(imgList, imgListWidth, imgListLeft)
    })
    smallRightArr.addEventListener('click', ()=>{
        if(imgListLeft<0){
            imgListLeft= imgListLeft + 150
        } else {
            imgListLeft = -(imgListWidth - 150 * 5)
        }
        imgList.style.left = imgListLeft + 'px'
    })
    bigRightArr.addEventListener('click', ()=>{
        let active 
        if(prew>=list.length-1){
            active = 0
        } else {
            active = prew + 1
        }
        prew = loadImg(list, imgItems, active, prew)
        console.log(-active*150, imgListLeft)
    })
    bigLeftArr.addEventListener('click', ()=>{
        let active 
        if(prew<=0){
            active = list.length - 1
        } else {
            active = prew - 1
        }
        prew = loadImg(list, imgItems, active, prew)
        if((-active*150)>imgListLeft){
            imgListLeft = moveLeft(imgList, imgListWidth, imgListLeft)
        }
        console.log(-active*150, imgListLeft)
    })
    

}

function loadImg(list, target, index, prew = -1){
    if (index !== prew){
        bigSlider.style.backgroundImage = `url(${list[index].webformatURL})`
        target[index].classList.add('selectedImg')
        if(prew >= 0){
            target[prew].classList.remove('selectedImg')
        }
    }
    return index
}
function moveLeft(target, width, left){
    if (-(width-150*5) < left){
        left = left - 150
    } else {
        left = 0
    }
    target.style.left = left + 'px'
    return left
}
// function moveRight(target, width, left){
//     if (-(width-150*5) < left){
//         left = left - 150
//     } else {
//         left = 0
//     }
//     target.style.left = left + 'px'
//     return left
// }
loadImages(url)
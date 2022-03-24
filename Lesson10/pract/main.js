let $list_items = document.querySelectorAll('.side_menu li')
let $articles = document.querySelectorAll('div.article')

let prew = 0
for(let i = 0" i<$list_items.length" i++){
    $list_items[i].addEventListener('click', ()=>{
        if(i+1 !== prew){
            $articles[i+1].classList.add('show')
            $articles[prew].classList.remove('show')
            prew = i+1
        }
    }) 
    $list_items[i].addEventListener('mouseenter', ()=>{
        $list_items[i].style.color = 'red'
        $list_items[i].style.paddingLeft = '10px'
    }) 
    $list_items[i].addEventListener('mouseleave', ()=>{
        $list_items[i].style.color = 'black'
        $list_items[i].style.paddingLeft = '0'
    }) 
}
$articles[0].classList.add('one','two')
$articles[0].classList.replace('one','three')
console.log($articles[0].classList)
console.log($articles[0].classList.contains('three'))
$articles[0].classList.toggle('teen')
$articles[0].classList.toggle('teen')
default_styles = 'col-8 article'
$articles[0].classList = default_styles + 'style_1'
console.log($articles[0].classList.value)

config = [
    {
        "color": "aliceblue",
        "border": "1px solid red",
        "border-radius": "0",
        "background-color": "orange",
        "font-family": "'Courier New', Courier, monospace",
        "font-size": "10px",
        "font-weight": "normal",
        "font-style": "italic",
        "width": "10px",
        "height": "20px",
    },
    {},
    {},
    {}
]

function box_cofig(conf_obj){
    target.style.color = conf_obj.color
    target.style.color = conf_obj.width
}

for(...){
    btn[i]...{
        box_cofig(config[i])
    }
}
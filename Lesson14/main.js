// // ------ 1
// let obj = new Object()

// obj.bar = 'bar'
// obj.foo = 'foo'

// console.log(obj)

// // ------ 2
// let obj2 = {'foo':1, 'bar':2}
// console.log(obj2)

// // ------ 3
// let obj3 = function(foo, bar){
//     return{
//         'foo':foo, 
//         'bar':bar
//     }
// }
// console.log(obj3(55))
// console.log(obj3(foo=1, bar=555))
// console.log(obj3(1,333))
// console.log(obj3(bar=555, foo=555444))

// let arr  = ['foo', 'bar']
// console.log(arr)


// let person = function(name='unnamed', 
//                     job='undefined', 
//                     gender='undefined',
//                     brd=new Date()){
//     return {
//         'person_name':name,
//         'job':job,
//         'gender':gender,
//         'brd':new Date(brd),
//         'age': function(){
//             return new Date().getFullYear() - this.brd.getFullYear()
//         },
//         'birth_date':function(){return this.brd.toLocaleDateString()}
//     }
// }    

// p1 = person('Bob', 'worker', 'male', '2000-01-01')
// console.log(p1)
// console.log(p1.age())
// console.log(p1.birth_date())

// p2 = person('John', 'programmer', 'male', '2005-10-01')
// console.log(p2)
// console.log(p2.age())
// console.log(p2.birth_date())


// rez = Object.assign({}, p1, {'name':"Rob"})
// console.log(rez)

// let dog = (name, age, color)=>{
//     return {
//         name, age, color,
//         'voice': ()=>console.log('Woof!'),
//         'info': function(){
//             console.log(`\tname: ${this.name},\n\tage: ${this.age},\n\tcolor: ${this.color}`)
//         }
//     }
// }

// let bobik = dog('Bobbik', 2, 'brown')
// console.log(bobik)
// bobik.voice()
// bobik.info()

// game elements
// play_zone = document.querySelector('.play_zone')

// let item = function(width, height, top=0, left, color, id){
//     return{
//         width, height, top, left, color, id,
//         draw:function(){
//             figure = document.createElement('div')
//             figure.classList.add('item')
//             figure.setAttribute('id','id'+id)
//             figure.style.width = this.width + 'px'
//             figure.style.height = this.height + 'px'
//             figure.style.top = this.top + 'px'
//             figure.style.left = this.left + 'px'
//             figure.style.backgroundColor = this.color
//             play_zone.append(figure)
//         },
//         moveLeft:function(){
//             if (this.left>=20){
//                 this.left = this.left-20
//                 document.getElementById('id'+id).style.left = this.left + 'px'}
//         },
//         moveRight:function(){
//             if (this.left<=500-this.width){
//                 this.left = this.left+20
//                 document.getElementById('id'+id).style.left = this.left + 'px'}
//         },
//         moveUp:function(){
//             if (this.top>=20){
//                 this.top = this.top-20
//                 document.getElementById('id'+id).style.top = this.top + 'px'}
//         },
//         moveDown:function(){
//             if (this.top<300-this.height){
//                 this.top = this.top+20
//                 document.getElementById('id'+id).style.top = this.top + 'px'}
//         }
//     }
// }



// item1 = item(20, 20, 100, 90, 'green')
// item1.draw()

// function down(){
//     item1.moveDown()
// }

// setInterval(down,1000)

// document.querySelector('.left').addEventListener('click',()=>{
//     item1.moveLeft()
// })
// document.querySelector('.right').addEventListener('click',()=>{
//     item1.moveRight()
// })
// document.querySelector('.up').addEventListener('click',()=>{
//     item1.moveUp()
// })
// document.querySelector('.down').addEventListener('click',()=>{
//     item1.moveDown()
// })


// arr = [
//     [1,2],
//     [3,4],
//     [8,[5,[6,[7]]]]
// ]
// console.log(arr)
// console.log(arr[0][0])
// console.log(arr[2][1][1][1][0])

// library
let books = []
book = function(title, authors, year, language, image, description){
    return{
        title, authors, year, language, image, description
    }
}

book1 = book(
        'Книга Java. Script. Сильні сторони.',
        'Дуглас Крокфорд (Пітер)',
        2010,
        'ukrainian',
        'https://images.zakupka.com/i3/firms/27/5321/5321345/pic_304c24d158c2b6a_300x300.webp',
        `На жаль, цей товар відсутній 
        Можливо, вас зацікавлять схожі товари`
)
books.push(book1)

let addButton = document.querySelector('.add-button'),
    target = document.querySelector('.books')

addButton.addEventListener('click', (event)=>{
    event.preventDefault()
    book_item = book(
        addItem.title.value,
        addItem.authors.value,
        addItem.year.value,
        addItem.language.value,
        addItem.image.value,
        addItem.description.value
    )
    books.push(book_item)
    template = `<div class="col-12 col-md-6 book">
    <img src="${book_item.image}" alt="${book_item.title}">
    <h4>${book_item.title}</h4>
    <p><b>${book_item.authors}</b> <i>${book_item.year}</i> <u>${book_item.language}</u></p>
    <p>${book_item.description}</p>
</div>`
    target.insertAdjacentHTML('beforeend', template)
})

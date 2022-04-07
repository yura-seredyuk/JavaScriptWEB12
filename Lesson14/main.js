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
play_zone = document.querySelector('.play_zone')

let item = function(width, height, top=0, left, color, id){
    return{
        width, height, top, left, color, id,
        draw:function(){
            figure = document.createElement('div')
            figure.classList.add('item')
            figure.setAttribute('id','id'+id)
            figure.style.width = this.width + 'px'
            figure.style.height = this.height + 'px'
            figure.style.top = this.top + 'px'
            figure.style.left = this.left + 'px'
            figure.style.backgroundColor = this.color
            play_zone.append(figure)
        },
        moveLeft:function(){
            if (this.left>=20){
                this.left = this.left-20
                document.getElementById('id'+id).style.left = this.left + 'px'}
        },
        moveRight:function(){
            if (this.left<=500-this.width){
                this.left = this.left+20
                document.getElementById('id'+id).style.left = this.left + 'px'}
        },
        moveUp:function(){
            if (this.top>=20){
                this.top = this.top-20
                document.getElementById('id'+id).style.top = this.top + 'px'}
        },
        moveDown:function(){
            if (this.top<300-this.height){
                this.top = this.top+20
                document.getElementById('id'+id).style.top = this.top + 'px'}
        }
    }
}

item1 = item(20, 20, 100, 90, 'green')
item1.draw()

document.querySelector('.left').addEventListener('click',()=>{
    item1.moveLeft()
})
document.querySelector('.right').addEventListener('click',()=>{
    item1.moveRight()
})
document.querySelector('.up').addEventListener('click',()=>{
    item1.moveUp()
})
document.querySelector('.down').addEventListener('click',()=>{
    item1.moveDown()
})
// // document.addEventListener('click',(event)=>{
// //     console.log(event)
// // })

// // OOP
// // abstraction - будівля(стіни, дах, двері, вікна, підлога), креслення()
// // inheritance - будинок(к-сть поверхів, балкони),      завод, магазиг ,банк
// //                 -> однопорховий, багатоповерховий    -> військовий, автомобільний, хімічний
// // encapsulation - (цегла, блок) - набір прихованих елементів
// // polimorphism - (відкривання) -> вікно, двері, воду


// // function ShowMessage(text, color, container){
// //     let p = `<p style='background-color: ${color};'>${text}</p>`
// //     target = document.querySelector(container)
// //     target.innerHTML = p
// // }

// // ShowMessage('Message1', 'green', '.wrapper1')
// // ShowMessage('Message2', 'red', '.wrapper2')

// // class ShowMessage{
// //     constructor(container, text = 'Plain text', color = 'yellow'){
// //         this.text = text
// //         this.color = color
// //         this.container = container
// //     }
// //     show(){
// //         document.querySelector(this.container).innerHTML = `<p style='background-color: ${this.color};'>${this.text}</p>`
// //     }
// // }

// // class ShowMessageIcon extends ShowMessage{
// //     constructor(container, icon, text, color,){
// //         super(container, text, color)
// //         this.icon = icon
// //     }
// //     show(){
// //         document.querySelector(this.container).innerHTML = `<p style='background-color: ${this.color};'><i class="material-icons">${this.icon}</i> ${this.text}</p>`
// //     }

// // }

// // let msg1 = new ShowMessage(".wrapper1","Message1", "green")
// // msg1.show()
// // let msg2 = new ShowMessage(".wrapper2")
// // msg2.show()
// // let msg3 = new ShowMessageIcon(".wrapper3", 'cloud', 'Message3', 'blue')
// // msg3.show()

// // let data = function(x){
// //     let encapsulated_value = 10
// //     let enc = function(y){     
// //         return encapsulated_value + y
// //     }
// //     return enc(x)
// // }

// // console.log(data(4))

// class RootElement{
//     constructor(width, color = 'black', height = 0, margin = 5){
//         this.width = width 
//         this.color = color
//         this.height = height
//         this.margin = margin
//         this.element = document.createElement('DIV')
//     }
//     create(){
//         this.element.style.width = this.width + 'px'
//         this.element.style.height = this.height + 'px'
//         this.element.style.margin = this.margin + 'px'
//         this.element.style.backgroundColor = this.color
//         document.querySelector('.wrapper1').append(this.element)
//     }
//     hide(){
//         this.element.style.display = 'none'
//     }
//     show(){
//         this.element.style.display = 'block'
//     }
// }

// class Rectangle extends RootElement{
//     constructor(width, height, color, shadow, margin){
//         super(width, color, height, margin)
//         this.shadow = shadow
//     }
//     createEl(){
//         this.create()
//         this.element.style.boxShadow = this.shadow
//         return this
//     }
// }

// class Circle extends RootElement{
//     constructor(width, color, margin){
//         super(width, color, margin)
//         this.height = width
//     }
//     createEl(){
//         this.create()
//         this.element.style.borderRadius = '50%'
//         return this
//     }
// }

// class Triangle extends RootElement{
//     constructor(color = 'transparent', topB, rightB, bottomB, leftB){
//         super(color)
//         this.color = color
//         this.topB = topB
//         this.rightB = rightB
//         this.bottomB = bottomB
//         this.leftB = leftB
//     }  
//     createEl(borders){
//         this.create()
//         this.element.style.width = this.element.height = '0px';
//         this.element.style.backgroundColor = 'transparent'
//         this.element.style.borderTop = `${this.topB}px solid ${borders[0]?this.color:'transparent'}`
//         this.element.style.borderRight = `${this.rightB}px solid ${borders[1]?this.color:'transparent'}`
//         this.element.style.borderBottom = `${this.bottomB}px solid ${borders[2]?this.color:'transparent'}`
//         this.element.style.borderLeft = `${this.leftB}px solid ${borders[3]?this.color:'transparent'}`
//         return this
//     }
// }

// let rect1 = new Rectangle(100,100, 'red', '2px 2px 3px 3px gray').createEl().hide()

// let rect2 = new Rectangle(200,100, 'green', '2px 2px 3px 3px gray', 20).createEl().hide()

// let circle = new Circle(100, 'orange').createEl().hide()

// let tr = new Triangle('red', 50, 50, 50, 50).createEl([1,0,0,0])
// let tr1 = new Triangle('red', 50, 50, 50, 50).createEl([1,1,0,0])
// let tr2 = new Triangle('red', 50, 50, 50, 50).createEl([1,0,0,1])


const date1 = new Date('2022-05-02');
const date2 = new Date();
const diffTime = date2 - date1;
const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
console.log(diffDays + " days");
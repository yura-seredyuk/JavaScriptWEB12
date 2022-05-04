class Person{
    constructor(id,first_name, last_name, address, phone, email, photo){
        this.id = id
        this.first_name = first_name
        this.last_name = last_name
        this.address = address
        this.phone = phone
        this.email = email
        this.photo = photo
    }
    print(){
        console.log(`ID:${this.id}\nFirst name: ${this.first_name}\nLast name: ${this.last_name}`)
    }
    name(){
        return this.first_name + ' ' + this.last_name
    }
    edit(first_name, last_name, address, phone, email, photo){
        this.first_name = first_name
        this.last_name = last_name
        this.address = address
        this.phone = phone
        this.email = email
        this.photo = photo
    }
    delete(){

    }
}

class Contact{
    constructor(person){
        this.person = person
        this.contact = document.createElement('LI')
    }
    create(){
        this.contact.classList.add('list-group-item')
        this.contact.dataset.id = this.person.id
        this.contact.innerHTML = `<div class="col-xs-12 col-sm-3">
        <img src="${this.person.photo}" alt="${this.person.name()}" class="img-responsive img-circle" />
    </div>
    <div class="col-xs-12 col-sm-9">
        <span class="name">${this.person.name()}</span><br/>
        <span class="glyphicon glyphicon-map-marker text-muted c-info" data-toggle="tooltip" title="${this.person.address}"></span>
        <span class="visible-xs"> <span class="text-muted">${this.person.address}</span><br/></span>
        <span class="glyphicon glyphicon-earphone text-muted c-info" data-toggle="tooltip" title="${this.person.phone}"></span>
        <span class="visible-xs"> <span class="text-muted">${this.person.phone}</span><br/></span>
        <span class="fa fa-comments text-muted c-info" data-toggle="tooltip" title="${this.person.email}"></span>
        <span class="visible-xs"> <span class="text-muted">${this.person.email}</span><br/></span>
        <span class="fa fa-pencil text-muted c-info" data-toggle="tooltip" title="edit"></span>
        <span class="fa fa-trash-o text-muted c-info" data-toggle="tooltip" title="delete"></span>
    </div>
    <div class="clearfix"></div>`
        document.querySelector('#contact-list').append(this.contact)
    }
    edit(){
        // console.log(this.contact)
        let edit_bttn = this.contact.querySelector('span.fa-pencil')
        edit_bttn.addEventListener('click',(event)=>{
            edit_contact.closest('li').style.display = 'block'
            parent = this.contact.closest('li')
            let id = parent.dataset.id
            console.log(this.person.first_name)
            edit_contact.first_name.value = this.person.first_name
            edit_contact.last_name.value = this.person.last_name
            edit_contact.address.value = this.person.address
            edit_contact.phone.value = this.person.phone
            edit_contact.email.value = this.person.email
            edit_contact.photo.value = this.person.photo
            edit_contact.querySelector('img').setAttribute('src', this.person.photo)
            // console.log(img)
            edit_contact.submit.value = 'Edit'
            edit_contact.submit.addEventListener('click',(event)=>{
                console.log('edit')
                this.person.first_name = edit_contact.first_name.value 
                this.person.last_name = edit_contact.last_name.value
                this.person.address = edit_contact.address.value
                this.person.phone = edit_contact.phone.value
                this.person.email = edit_contact.email.value
                this.person.photo = edit_contact.photo.value 
                console.log(this.person)
                parent.querySelector('span.name').textContent = this.person.name()
                // ------
                edit_contact.reset()
                edit_contact.querySelector('img').setAttribute('src', 
                'assets/images/placeholder-image.png')
                edit_contact.closest('li').style.display = 'none'
            })

        })
    }
    delete(){
        let delete_bttn = this.contact.querySelector('span.fa-trash-o')
        delete_bttn.addEventListener('click',(event)=>{
            if(event.target.tagName == 'SPAN'){
                parent = this.contact.closest('li')
                let id = parent.dataset.id
                dataBase = dataBase.filter(person=>person.id != id)
                console.log(dataBase)
                parent.remove()
            }
            
        })
    }
}

function generateDB(count){
    let dataBase = []
    fetch(`https://api.randomuser.me/?results=${count}&nat=gb`)
    .then(response=>response.json())
    .then(data=>{
        for(person of data.results){
            p = new Person(
                Math.floor(Math.random() * 100000),
                person.name.first,
                person.name.last,
                person.location.street.number + ' ' + person.location.street.name,
                person.phone,
                person.email,
                person.picture.medium)
            // p.print()
            dataBase.push(p)
        }
    })
    return dataBase
}

let dataBase = generateDB(5)
setTimeout(() => {
    for(person of dataBase){
        // console.log("Person:",person)
        let contact = new Contact(person)
        contact.create()
        contact.edit()
        contact.delete()
    }
}, 700);


// Перевірити причину видалення даних при повторному редагуванні
// Додати зміни при редагуванні для всіх полів
// Додати функціонал створення нового контакту
// * створити фільтр для пошуку за вказаним іменем
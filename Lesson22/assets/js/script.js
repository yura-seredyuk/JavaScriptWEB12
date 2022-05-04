class Person{
    constructor(first_name, last_name, address, phone, email, photo){
        this.first_name = first_name
        this.last_name = last_name
        this.address = address
        this.phone = phone
        this.email = email
        this.photo = photo
    }
    print(){
        console.log(`First name: ${this.first_name}\nLast name: ${this.last_name}`)
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
}

class Contact{
    constructor(person){
        this.person = person
        this.contact = document.createElement('LI')
    }
    create(){
        console.log(this.person.first_name)
        this.contact.classList.add('list-group-item')
        this.contact.innerHTML = `<div class="col-xs-12 col-sm-3">
        <img src="${this.person.photo}" alt="Seth Frazier" class="img-responsive img-circle" />
    </div>
    <div class="col-xs-12 col-sm-9">
        <span class="name">${this.person.name()}</span><br/>
        <span class="glyphicon glyphicon-map-marker text-muted c-info" data-toggle="tooltip" title="${this.person.address}"></span>
        <span class="visible-xs"> <span class="text-muted">${this.person.address}</span><br/></span>
        <span class="glyphicon glyphicon-earphone text-muted c-info" data-toggle="tooltip" title="${this.person.phone}"></span>
        <span class="visible-xs"> <span class="text-muted">${this.person.phone}</span><br/></span>
        <span class="fa fa-comments text-muted c-info" data-toggle="tooltip" title="${this.person.email}"></span>
        <span class="visible-xs"> <span class="text-muted">${this.person.email}</span><br/></span>
    </div>
    <div class="clearfix"></div>`
        document.querySelector('#contact-list').append(this.contact)
    }
}

function generateDB(count){
    let dataBase = []
    fetch(`https://api.randomuser.me/?results=${count}&nat=gb`)
    .then(response=>response.json())
    .then(data=>{
        for(person of data.results){
            p = new Person(person.name.first,
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
        console.log("Person:",person)
        let contact = new Contact(person).create()
    }
}, 700);


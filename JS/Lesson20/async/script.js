// PROCESS -> TREAD -> alg

// MULTIPROCESSING | MULTITREADING | ASYNCHRONOUS | SYNCHRONOUS

// SYNCHRONOUS
//  1._______; 2.___; 3.______; 4:____________;

// MULTIPROCESSING | MULTITREADING
// 1._______; 4:____________;
// 2.___; 3.______;

// ASYNCHRONOUS
//  1._______; 
//  2.___;
//  3.______;
//  4.____________;

// let category_list = {
//     'general':'Всі',
//     'business':'Бізнес',
//     'health':'Здоров’я',
//     'science':'Наука',
//     'sports':'Спорт',
//     'technology':'Технології',
//     'entertainment':'Шоу-бізнес',

// }

// let category = 'general'

// let t1 = t2 = 0
// function getInfo(category){
//     let url = `https://newsapi.org/v2/top-headlines?country=ua&category=${category}&pageSize=100&apiKey=f210154948eb4e6e89d98eb5582468a7`
//     let start = new Date()
//     fetch(url)
//     .then(response=>response.json())
//     .then(obj=>{
//         let end = new Date()
//         // console.log(end-start)
//         // console.log(obj.articles)
//         t1+= end-start
//         console.log('SY:',t1, start.getMilliseconds())
//     })
// }

// async function asGetInfo(category){
//     let url = `https://newsapi.org/v2/top-headlines?country=ua&category=${category}&pageSize=100&apiKey=f210154948eb4e6e89d98eb5582468a7`
//     let start = new Date()
//     let response = await fetch(url)
//     let obj = await response.json()
//     let end = new Date()
//     t2+= end-start
//     console.log('AS:', t2, start.getMilliseconds())
//     // console.log(obj.articles)
// }

// getInfo('general')
// asGetInfo('general')

// let start = new Date().getMilliseconds()
// for(category in category_list){
//     // console.log(category)
//     getInfo(category)
    
// }
// let end = new Date().getMilliseconds()



// for(category in category_list){
//     // console.log(category)
//     asGetInfo(category)
    
// }

// getInfo('general') 
// getInfo('business')
// getInfo('health') 
// getInfo('science')
// getInfo('sports') 
// getInfo('technology')
// getInfo('entertainment')


// Promise.allSettled([asGetInfo('general'), 
// asGetInfo('business'),
// asGetInfo('health') ,
// asGetInfo('science'),
// asGetInfo('sports'), 
// asGetInfo('technology'),
// asGetInfo('entertainment')]).then(console.log).catch(console.log)


let category_list = {
    'general':'Всі',
    'business':'Бізнес',
    'health':'Здоров’я',
    'science':'Наука',
    'sports':'Спорт',
    'technology':'Технології',
    'entertainment':'Шоу-бізнес',

}
let news = document.querySelector('main.news')


function createArticle(category, articles){
    let section = document.getElementById(`news_${category}`)
    for(article of articles){
        let article_element = document.createElement('article')
        let header = document.createElement('header')
        let time = document.createElement('time')
            time.textContent = new Date(article.publishedAt).toLocaleString()
        let title = document.createElement('h4')
            title.textContent = article.title
        let hd_source = document.createElement('span')
            hd_source.textContent = `(${article.source.name})`
        let content = document.createElement('content')
        let img = document.createElement('img')
            img.setAttribute('src',article.urlToImage)
        let description = document.createElement('p')
            description.textContent = article.description
        let footer = document.createElement('footer')
        let author = document.createElement('span')
            author.textContent = article.author
        let ft_source = document.createElement('a')
            ft_source.textContent = article.source.name
            ft_source.setAttribute('href',article.url)
            ft_source.setAttribute('target','_blank')
        title.append(hd_source)
        header.append(time,title)
        content.append(img,description)
        footer.append(author,ft_source)
        article_element.append(header,content,footer)
        section.append(article_element)
    }
    article_list = document.querySelectorAll(`section[id="news_${category}"] article`)
    hideContent(article_list)
}

function hideContent(article_list){
    console.log(article_list)
    for(let i = 0; i< article_list.length; i++){
        content = article_list[i].getElementsByTagName('content')[0]
        content.style.display = 'none'
        footer = article_list[i].getElementsByTagName('footer')[0]
        footer.style.display = 'none'
        article_list[i].addEventListener('click',(event)=>{
            content = article_list[i].getElementsByTagName('content')[0]
            footer = article_list[i].getElementsByTagName('footer')[0]
            if(content.style.display == 'none'){
                content.style.display = 'flex'
                footer.style.display = 'flex'
            } else {
                content.style.display = 'none'
                footer.style.display = 'none'
            }
        })
    }

}

async function asGetInfo(category){
    let url = `https://newsapi.org/v2/top-headlines?country=ua&category=${category}&pageSize=10&apiKey=fa0e5c3c24544a2aaf760dbb24b971e3`
    let response = await fetch(url)
    let obj = await response.json()
    console.log(obj.articles)
    await createArticle(category, obj.articles)
}

for(category in category_list){
    let section = document.createElement('section')
    section.setAttribute('id',`news_${category}`)
    section.innerHTML = `<a href="#"><h3>${category_list[category]}</h3></a>`
    news.appendChild(section)  
}

for(category in category_list){
    asGetInfo(category)   
}


// Homework
//  1 add cursor pointer for header h4
//  2 show/hide only for event.target.tagName ==  'H4'
//  3 remowe seconds from time
//  4 add css styles

let category_list = {
    'general':'Всі',
    'business':'Бізнес',
    'health':'Здоров’я',
    'science':'Наука',
    'sports':'Спорт',
    'technology':'Технології',
    'entertainment':'Шоу-бізнес',

}


function article_html(article){
    published = new Date(article.publishedAt).toLocaleString()
    img = article.urlToImage?article.urlToImage:'assets/img/placeholder-image.png'
    return `<article class="row">
    <div class="col-4 image"><img src="${img}" alt="picture"></div>
    <div class="col-8 content d-flex flex-column">
        <h3>${article.title}</h3>
        <p><span class="author">${article.author?article.author:''}</span> <span class="published">${published}</span></p>
        <p class="description">${article.description?article.description:''}</p>
        <a href="${article.url}" class="btn btn-link align-self-end" target="_blank">Читати більше на ${article.source.name}"</a>
    </div>
    </article>`
}

function loadNews(category=''){
    let country = 'ua',
        country_q = ``,
        category_q = category?`&category=${category}`:''
    let url = `https://newsapi.org/v2/top-headlines?country=${country}${category_q}&pageSize=100&apiKey=f210154948eb4e6e89d98eb5582468a7`

    fetch(url)
    .then(response=>response.json())
    .then(data=>{
        console.log(data['articles'])
        let $news =  document.querySelector('main.news')
        $news.innerHTML=''
        for(article of data['articles']){
            $news.insertAdjacentHTML('beforeend', article_html(article))
        }
    })
    .catch(error=>{
        console.error('Error: ', error)
    })
}

function addButtons(){
    let $buttons = document.querySelector('.buttons')
    for(item in category_list){
        let btn = document.createElement('BUTTON')
        btn.classList.add('btn','btn-primary')
        btn.textContent = category_list[item].toUpperCase()   
        btn.dataset.category = item
        $buttons.append(btn)
    }
    let $button_list = document.querySelectorAll('.buttons button')
    for(let i=0; i<$button_list.length; i++){
        $button_list[i].addEventListener('click',()=>{
            loadNews($button_list[i].dataset.category)
        })
    }
}
addButtons()
loadNews('general')
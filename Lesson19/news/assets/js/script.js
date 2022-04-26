



function article_html(article){
    return `<article class="row">
    <div class="col-4 image"><img src="${article.urlToImage}" alt="picture"></div>
    <div class="col-8 content d-flex flex-column">
        <h3>${article.title}</h3>
        <p><span class="author">${article.author}</span> <span class="published">${article.published}</span></p>
        <p class="description">${article.description}</p>
        <p class="content">${article.content}</p>
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
        for(article of data['articles']){
            document.querySelector('main.news').insertAdjacentHTML('beforeend', article_html(article))
            
        }
    })
    .catch(error=>{
        console.error('Error: ', error)
    })
}

loadNews()
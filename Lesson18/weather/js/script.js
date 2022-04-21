let region_name = 'Рівне'

url = `https://api.openweathermap.org/data/2.5/weather?q=${region_name}&lang=ua&appid=47065cb9ab1a711c668427875a0d6e0e`

url_1 = `https://api.openweathermap.org/data/2.5/weather?q=${region_name}&cnt=7&lang=ua&appid=47065cb9ab1a711c668427875a0d6e0e`

fetch(url)
	.then(response => response.json())
	.then(response => {
        console.log(response)
        // region
        document.getElementById('region').textContent = region_name
        // temp
        document.getElementById('temp').textContent = (response.main.temp-273.15).toFixed(2)+'°C'
        // feel
        document.getElementById('feel').textContent = (response.main.feels_like-273.15).toFixed(2)+'°C'
        // weather_description
        let description =  response.weather[0].description
        document.getElementById('weather_description').textContent = description[0].toUpperCase()+description.slice(1)

    })
	.catch(err => console.error(err));  
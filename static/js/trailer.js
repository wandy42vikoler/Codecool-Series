console.log('hello')

let button = document.getElementsByTagName('button')[2]
console.log('button', button)

button.addEventListener('click', showTrailer)


function showTrailer(){
    let trailer_container = document.getElementById('trailer')
    let show_id = button.id
    let url = `/trailer/${show_id}`
    fetch(url)
        .then(function(response){
            return response.json()
        })
        .then(function(data){
            trailer_container.innerHTML +=
                `<h3> ${data[0]['trailer']} </h3>`
        })
        .catch(function (err){
            console.log('something went wrong', err)
        })
}
let shows = document.getElementsByTagName('li')
console.log('lol', shows)
for(let show of shows) {
    console.log('heya')
    show.addEventListener('click', seasons)
}

function seasons(e){
    let target = e.currentTarget
    let show_season_table = document.getElementById('table')
    show_season_table.innerHTML = ''
    let show_id = target.id
    console.log(show_id)
    let url = `/shows/${show_id}/`
    console.log(url, 'url')
    fetch(url)
        .then(function(response){
            return response.json();
        })
        .then(function(data){
            let innerHtml = `
            <table>
                <thead>
                <tr>
                    <th> Title </th>
                    <th> Overview </th>
                    <th> Episodes Number </th>
                </tr>
                </thead>`
            for (let show of data) {
                innerHtml += `
                <tbody>
                    <tr>
                        <td> ${show.title} </td>
                        <td> ${show["overview"]} </td>
                        <td> ${show["episode_n"]} </td>
                    </tr>
                </tbody>   `
            }
            innerHtml += `</table>`
            show_season_table.innerHTML += innerHtml
        })
        .catch(function(err){
            console.log('Something wrong', err)
        })
}
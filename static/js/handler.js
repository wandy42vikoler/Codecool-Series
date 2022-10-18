
let pagination = 0

let header = document.getElementsByTagName('th');
for (let headers of header) {
    let up = '⇧'
    if (headers.innerHTML != 'Genres' && headers.innerHTML != 'Trailer' && headers.innerHTML != 'Homepage') {
        /*headers.append(up)*/
        headers.addEventListener('click', sort);
        console.log('ss',headers)
    }
}


let urlString = window.location.href
    let paramString = urlString.split('?')[1];
    let queryString = new URLSearchParams(paramString);

function sort(e){
    let up = '⇧'
    let down = '⇩'
    let order_by = e.currentTarget.innerHTML;
    let desc;
    let string = !urlString.includes('?')
    console.log(string)

    if (string){
        desc = 'DESC';
        order_by.substring(0, order_by.length -1);
        e.currentTarget.append(up)
    }

    if (urlString.includes('?')) {
        desc = 'DESC'
        if (paramString.includes('DESC')) {
            desc = 'ASC';
            order_by.substring(0, order_by.length - 1);
            e.currentTarget.append(down)
        }
    } else {
        desc = 'DESC';
        order_by.substring(0, order_by.length -1);
        e.currentTarget.append(up)
    }

    if (order_by == 'Runtime (min)') {
        order_by = 'runtime';
    }
    const url = window.location.href;
    console.log(url)
    window.location.replace(`http://127.0.0.1:5000/shows/most-rated/${pagination}?order_by=${order_by}&desc=${desc}`);
}



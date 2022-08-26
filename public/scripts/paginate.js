//asset/js/paginate.js
var page = 0

function paginate(route){
    $('.load-more img').attr('src', '/static/images/loading.gif')
    page += 1
    
    $.get(`/admin/${route}/paginate/${page}`, function(data, status){
        appendItem(data.items, route)
    })
}

function appendItem(items, route){
    var html = ''
    
    if(items){
        for(var item in items){
            html += `<div class='item'>`
            html += `<a href="/${route}/${items[item]['id']}"><img class='thumb' src="${items[item]['thumb']}" />`
            if(('entries' in items[item]) && (items[item]['entries'] !== '')){
                html += `<img class='play-icon' src="/static/images/play.png" />`
            }
            html += `</a>`
            html += `<div class='wrapper'>`
            html += `<a href="/${route}/${items[item]['id']}">${items[item]['title']}</a>`
            html += `<p class='${items[item]['id']}'></p>`
            html += `<script>`
            html += `$('.items .item .${items[item]['id']}').html(new Date("${items[item]['datetime']}").toLocaleDateString())`
            html += `</script>`
            html += `</div>`
            html += `<div class='icon'>`
            html += `<a href='/admin/${route}/edit/${items[item]['id']}'><img src='/static/images/edit.png' /></a>`
            html += `<a href='/admin/${route}/delete/${items[item]['id']}'><img src='/static/images/delete.png' /></a>`
            html += `</div>`
            html += `</div>`
        }
    }
    $('.items').append(html)
    $('.load-more img').attr('src', '/static/images/load-more.png')
}
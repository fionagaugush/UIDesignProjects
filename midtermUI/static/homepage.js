$(function() {
for (let i = 1; i < 4; i++) {
     let this_popular = data[i];
     console.log(this_popular)
     this_id = this_popular.id

     $("#list_of_popular").append("<div class = 'col-md-4 thumbnail'> <a  href = 'view/" + this_popular.id + "'> <img src ='"+this_popular.image+"'class = 'clickable' alt = '"+this_popular.alt+"'> </a> <a  class = 'centered' data-id='" + this_popular.id + "'  href = 'view/" + this_popular.id + "'> " + this_popular.name + "</a>  </div>");
     $("#dept").append("<div class = 'col-md-4 '> <a  class = 'small' href = '/search?query=" + this_popular.department + "'> " + this_popular.department+"</a></div>")

}
})
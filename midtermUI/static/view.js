$(function() {

$("#name").append(data[id].name )

 for (let i = 0; i < data[id].genre.length; i++) {

 $("#genre").append("<br>"+data[id].genre[i] )

 }


 for (let i = 0; i < data[id].notable_works.length; i++) {

 $("#works").append("<br>"+data[id].notable_works[i] )

 }


$("#bio").append(data[id].biography)
$("#department").append("<a href = '/search?query="+ data[id].department + "'>" + data[id].department+ "</a>")

$("#artifacts").append("<a href = "+ data[id].performance + ">" + data[id].performance+ "</a>" )
$("#year").append("<a href = '/search?query="+ data[id].year + "'>" + data[id].year+ "</a>")



})
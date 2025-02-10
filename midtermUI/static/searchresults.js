$(function() {
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var query = $("#search").val()
    length  = ($("#search").val().trim()).length;
    if (length>0){
    $("#search_title").empty();
    $("#search").val("");

    window.location.href = '/search?query=' + encodeURIComponent(query);

    }
    else{
    $("#search").val("")
    $("#search").focus();
    }
})
});
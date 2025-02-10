

$(function() {



    $("#add_performer").click(function(){
    $("#add_name").removeClass("error");
    $("#add_image").removeClass("error");
    $("#add_bio").removeClass("error")
    $("#add_year").removeClass("error");
    $("#add_songs").removeClass("error")
      $("#add_department").removeClass("error");
       $("#add_genre").removeClass("error");
        $("#add_notes").removeClass("error");
        $("#add_alt").removeClass("error");
        $("#error_message").empty()





     $("#message").empty()
    let new_name =($("#add_name").val()).trim();
    if (new_name.length == 0 ){
    $("#add_name").addClass("error");
    $("#add_name").focus();
    }
    let new_image = ($("#add_image").val()).trim();
        if (new_image.length == 0 ){
        $("#add_image").addClass("error");
        $("#add_image").focus();
        }
    let new_bio  =($("#add_bio").val()).trim();
       if (new_bio.length == 0 ) {
    $("#add_bio").addClass("error");
    $("#add_bio").focus();
    }
    let new_year = ($("#add_year").val()).trim();
    if (new_year.length == 0 || isNaN(new_year) ) {
        $("#add_year").addClass("error");
         $("#add_year").focus();
        }
    let new_works = ($("#add_songs").val()).split(",");
    works_test = new_works[0].trim()
    if (works_test.length == 0 ) {
            $("#add_songs").addClass("error");
            $("#add_songs").focus();
            }


    let new_genre = ($("#add_genre").val()).split(",")
    genre_test = new_genre[0].trim()
        if (genre_test.length == 0 ) {
                $("#add_genre").addClass("error");
                $("#add_genre").focus();
                }
    let new_department = ($("#add_department").val()).trim();
    if (new_department.length == 0 ) {
                    $("#add_department").addClass("error");
                    $("#add_department").focus();
                    }
    let new_performance = $("#add_performance").val();
    let new_notes = $("#add_notes").val();

    let new_alt = ($("#add_alt").val()).trim();

  if (new_alt.length == 0 ) {
                    $("#add_alt").addClass("error");
                    $("#add_alt").focus();
                    }


    if (!isNaN(new_year)& new_alt.length > 0 & new_name.length>0 & new_image.length>0 & new_bio.length>0  & new_year.length>0 & works_test.length>0 & genre_test.length>0 & new_department.length>0){
    let artist_to_save = {

            "name": new_name,
            "image": new_image,
            "biography": new_bio,
            "year": new_year,
            "notable_works": new_works,
            "genre": new_genre,
            "department": new_department,
            "performance": new_performance,
            "notes": new_notes,
            "id": id,
            'alt': new_alt
    }





 $.ajax({

   type: "POST",
   url: "/submit",
   dataType : "json",
   contentType: "application/json; charset=utf-8",
   data : JSON.stringify(artist_to_save),
   success: function(result){
   valid = 1;
   console.log("New Result:", result.new_artist);
   let new_artist = result.new_artist
   data[new_artist.id] = new_artist;
   $("#message").append("<div class = 'grey'>Success!!!</div><br> <a class = 'new' href = '/view/" + new_artist.id + "'> GO TO NEW ENTRY </a>")
   $("#add_name").focus();


    $("#add_name").val("");

     $("#add_image").val("");
      $("#add_bio").val("");
      $("#add_year").val("");
       $("#add_songs").val("")
      $("#add_genre").val("")
      $("#add_department").val("");
      $("#add_performance").val("");
     $("#add_notes").val("");
        $("#add_alt").val("");

  },
   error: function(request, status, error){
   console.log("Error");
   console.log(request)
   console.log(status)
   console.log(error)
                            }
                        });



}
else{
valid = 0;
$("#error_message").append("There was an error. Please go back and revise your answers")

}
})
})








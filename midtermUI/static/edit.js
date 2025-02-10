 $(function() {
     $("#add_name").val(data[id].name);
      $("#add_image").val(data[id].image);
      $("#add_bio").val(data[id].biography);
      $("#add_year").val(data[id].year)
      $("#add_songs").val(data[id].notable_works)
      $("#add_genre").val(data[id].genre)
      $("#add_department").val(data[id].department)
      $("#add_performance").val(data[id].performance)
      $("#add_notes").val(data[id].notes)
       $("#add_alt").val(data[id].alt)






      $("#discard").click(function(){
        $("#dialog")[0].showModal()
      })
      $("#no").click(function(){
           $("#dialog")[0].close()
      })

      $("#yes").click(function(){
            window.location.href = '/view/'+id
      })

      $("#add_performer").click(function(){

      if (valid ==1){

      window.location.href = '/view/'+id
      }
      })





})


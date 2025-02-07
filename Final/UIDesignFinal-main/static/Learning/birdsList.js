$(document).ready(function() {

 $("#home_nav").removeClass("active")
  $("#quiz_nav").removeClass("active")
   $("#learn_nav").addClass("active")


    for (var key in birds) {
        var bird = birds[key];


        (function(bird) {
        var play = document.getElementById("listen" + bird.id);
         var audio = document.getElementById("audio" + bird.id);
            $("#listen" + bird.id).click(function() {

                if (audio.paused) {
                    audio.play();
                    play.textContent = 'Pause Sound';
                } else {
                    audio.pause();
                    play.textContent = 'Play Sound';
                }
            });




        audio.addEventListener("ended", function(){
               audio.currentTime = 0;
               play.textContent = 'Play Sound';

          });

        })(bird);
    }

    for (var key in birds) {
        var bird = birds[key];
        (function(bird) {
            var moreButton = document.getElementById("more" + bird.id);
            var currentURL = window.location.href;
            moreButton.addEventListener('click', function(event) {
                console.log(bird.id);
                var id = bird.id;
                var newURL = currentURL + '/' + id;
                window.location.href = newURL;
            });
        })(bird);
    }
     $("#compare_button").click(function(){
      var newURL =  '/compare/0/1';
       window.location.href = newURL;

     })
      $("#home_button").click(function(){
       var newURL =  '/';
       window.location.href = newURL;

          })



});
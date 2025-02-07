$(document).ready(function() {





 $("#home_nav").removeClass("active")
  $("#quiz_nav").removeClass("active")
   $("#learn_nav").addClass("active")

  var play = document.getElementById("listen_more");
var audio = document.getElementById("audio_more");
 $("#listen_more").click(function() {

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





         $("#list_button").click(function(){
              window.history.back();

             })
              $("#compare_button").click(function(){
               var newURL =  '/compare/0/1';
               window.location.href = newURL;

                  })

    })















$(document).ready(function() {



 $("#home_nav").removeClass("active")
  $("#quiz_nav").removeClass("active")
   $("#learn_nav").addClass("active")

var bird1 = document.getElementById('bird1');

var bird2 = document.getElementById('bird2');

var play_second = document.getElementById("listen_second");
var audio_second = document.getElementById("audio_second");

var play_first = document.getElementById("listen_first");
var audio_first = document.getElementById("audio_first");


bird1.value = first;

bird2.value = second;
  bird1.addEventListener('change', function() {

    var newFirst = this.value;

    var newURL = "/compare/"  + newFirst + "/" + second;

    window.location.href = newURL;
    })

    var bird2 = document.getElementById('bird2');
      bird2.addEventListener('change', function() {

        var newSecond = this.value;

        var newURL = "/compare/"  + first + "/" + newSecond;

        window.location.href = newURL;
        })








 $("#listen_first").click(function() {


              if (audio_first.paused) {
                    audio_first.play();
                    play_first.textContent = 'Pause Sound';
                } else {
                    audio_first.pause();
                    play_first.textContent = 'Play Sound';
                }

    });


$("#listen_second").click(function() {


              if (audio_second.paused) {
                    audio_second.play();
                    play_second.textContent = 'Pause Sound';
                } else {
                    audio_second.pause();
                    play_second.textContent = 'Play Sound';
                }

    });

 audio_first.addEventListener("ended", function(){
       audio_first.currentTime = 0;
       play_first.textContent = 'Play Sound';
       console.log("ended");
  });
 audio_second.addEventListener("ended", function(){
       audio_second.currentTime = 0;
       play_second.textContent = 'Play Sound';
       console.log("ended");
  });



 $("#list_button").click(function(){
                window.history.back();

             })
              $("#quiz_button").click(function(){
               var newURL =  '/quiz';
               window.location.href = newURL;

                  })

    })



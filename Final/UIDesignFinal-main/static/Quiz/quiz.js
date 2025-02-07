// Start quiz when start button is clicked
$(document).ready(function() {

 $("#home_nav").removeClass("active")
 $("#quiz_nav").addClass("active")
 $("#learn_nav").removeClass("active")

    if (current_question <= 1) {
        $("#continue-quiz-button").hide();
    }

    $("#start-quiz-button").click(function() {
        window.location.href = "/quiz/1";
    });

    // Option to continue quiz if user already started
    $("#continue-quiz-button").click(function() {
        window.location.href = "/quiz/" + current_question;
    });
});

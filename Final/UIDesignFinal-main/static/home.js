$(document).ready(function() {


 $("#home_nav").addClass("active")
 $("#quiz_nav").removeClass("active")
 $("#learn_nav").removeClass("active")

    $("#start-learning").click(function() {
        window.location.href = "/learn";
    });
    $("#quiz").click(function() {
            window.location.href = "/quiz";
        });
});
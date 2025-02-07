// Start quiz when start button is clicked
$(document).ready(function() {

 $("#home_nav").removeClass("active")
 $("#quiz_nav").addClass("active")
 $("#learn_nav").removeClass("active")

    display_choices();

    // Hide next question button until a choice is made
    $("#next-question-button").hide();

    if (question_number >= total_num_questions) {
        $("#next-question-button").text("View Results");
    }
    else {
        $("#next-question-button").text("Next Question");
    }

    // Go to next question or end of test
    $("#next-question-button").click(function() {

        if (question_number >= total_num_questions) {
            window.location.href = "/quiz_results";
        }

        else {
            window.location.href = "/quiz/" + (question_number + 1);
        }
    });

    //Render audio clip if one is provided
    if (question.hasOwnProperty("audioURL")) {
        let baseURL = "/static/"

        let audio = $("<audio controls></audio>");
        audio.attr("src", baseURL + question["audioURL"]);
        audio.attr("type", "audio/mpeg");
        $("#question-audio").append(audio);
    }

});

function display_choices() {
    $("#choices").empty();
    let choices = question["choices"];

    for (let i = 0; i < choices.length; i++) {

        let choice_button = $("<button></button>");
        choice_button.text(choices[i]);
        choice_button.addClass("btn choice-button");
        choice_button.attr("id", i);
        choice_button.click(handle_choice_click);


        $("#choices").append(choice_button);
        $("#choices").append("<br>");
    }
}

// Handle when a choice-button is clicked
function handle_choice_click() {
    let choice_id = $(this).attr("id");


    let correct_answer_id = question["correctAnswer"];
    let awarded_points = 0;

    // Correct answer
    if (choice_id == correct_answer_id) {
        $(this).addClass("correct");
        awarded_points = 1;

    } else {
        $(this).addClass("incorrect");
        let correct_choice = $("#" + correct_answer_id);
        correct_choice.addClass("correct");
    }

    // Disable all buttons after a choice is made
    $(".choice-button").prop("disabled", true);


    //Update User data
    let user_data = {
        "step": 2,
        "currentQuizQuestion": question_number + 1, // User is now on the next question
        "quizScore": parseInt($("#score-value").text()) + awarded_points
    };

    save_user_data(user_data);



    give_feedback($(this).text(), $("#" + correct_answer_id).text(), awarded_points);

    // Show next question button
    $("#next-question-button").show();
}

// Save user progress in backend
function save_user_data(user_data) {
    $.ajax({
        url: "/update_user_step",
        type: "POST",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(user_data),
        success: function(result) {
            console.log(result);
            console.log(user_data);
            $("#score-value").text(user_data["quizScore"]);
        },
        error: function(request, status, error) {
            console.log(error);
            console.log(request);
            console.log(status);
        }
    });
}

function give_feedback(choice, correct_answer, is_correct) {
    if (is_correct == 1){
        $("#feedback").html("<h3 class='feedback-success'>Correct! Good job!<h3>");
        $("#feedback").addClass("correct-text");
    }

    else {
        let header = $("<h3 class='feedback-fail'>Incorrect</h3>").addClass("incorrect-text");

        user_choice_bird_path = find_bird_path(choice, birds_list);
        correct_choice_bird_path = find_bird_path(correct_answer, birds_list);
        //if the correct answer is not a bird (true/false), the path will be "", do not make it linked
        if (user_choice_bird_path != "" ){
        user_choice_link = "<a href='" + user_choice_bird_path + "'>" + choice + "</a>";
        }
        if (correct_choice_bird_path != ""){
        correct_choice_link = "<a href='" + correct_choice_bird_path + "'>" + correct_answer + "</a>";
        }
        if(user_choice_bird_path == "" ) {
          user_choice_link = "<span>" + choice + "</span>";
        }
        if(correct_choice_bird_path == "" ) {
          correct_choice_link = "<span>" + correct_answer + "</span>"
        }

        let user_choice = $("<p> <span class='grey-text'> You selected: </span> " + user_choice_link + "</p>");
        let correct_choice = $("<p class='feedback-fail-2'> <span class='grey-text'> Correct answer: </span> " + correct_choice_link + "</p>");
        $("#feedback").append(header);
        $("#feedback").append(user_choice);
        $("#feedback").append(correct_choice);
    }
}

function find_bird_path(bird_name, birds) {
    let path = "";
    //manually accounting for the question with the 2 birds at once
    if (bird_name== "Mourning Dove + Cardinal"){
     path = "/compare/0/4"
     return path
    }
    if (bird_name == "Red Tailed Hawk + Cardinal"){
         path = "/compare/2/4"
         return path


    }

    if (bird_name == "House Sparrow + Mourning Dove"){
     path = "/compare/3/0"
     return path

    }

    for (var bird_id in birds) {
        let bird = birds[bird_id];
        if (bird["name"] == bird_name) {
            path = "/learn/" + bird["id"];

            console.log("Bird Path for " + bird_name + ": ", path);
            return path;
        }

    }

    return path;
}




// Start quiz when start button is clicked
$(document).ready(function() {




 $("#home_nav").removeClass("active")
 $("#quiz_nav").addClass("active")
 $("#learn_nav").removeClass("active")

    display_drag_drop_table();

    // Hide next question button until a choice is made
    $("#next-question-button").hide();

    if (question_number >= total_num_questions) {
        $("#next-question-button").text("View Results");
    }
    else {
        $("#next-question-button").text("Next Question");  
    }

    $("#next-question-button").click(function() {

        if (question_number >= total_num_questions) {       
            window.location.href = "/quiz_results";
        }
        else {
            window.location.href = "/quiz/" + (question_number + 1);   
        }
    });

    $("#submit-button").click(function() {
        
        $("#error-message").text("");

        // Keep track of mistakes
        let mistakes = [];
        let canSubmit = true;
        let correct = []

        // Loop over all droppables
        $(".ui-droppable").each(function() {
            var droppable = $(this);
            
            if (droppable.data('hasItems') === undefined || droppable.data('hasItems') == false) {
                canSubmit = false;
                $('#error-message').text("Please fill in all drop zones");
                 
            }

            else {
                // Get the id of the dropped item (after the 'draggable' prefix)
                let droppedItem_id = parseInt(droppable.data('droppedItem_id').substring(9));
                let correct_id =  question['correctAnswer'][parseInt(droppable.attr('id').substring(9))]

                
                // Incrrect Answer
                if (droppedItem_id != correct_id) {
                    console.log("User selected: " + droppedItem_id, "Correct answer: " + correct_id);
                    mistakes.push([droppedItem_id, correct_id]);       
                }
                else {
                    correct.push(droppedItem_id);
                }
            }    
        });


        // Can submit only if all drop zones are filled with a choice
        if (canSubmit) {
            let awarded_points = (mistakes.length == 0) ? 1 : 0;

            //Update User data
            let user_data = {        
                "step": 2,
                "currentQuizQuestion": question_number + 1,
                "quizScore": parseInt($("#score-value").text()) + awarded_points
            };
            
            save_user_data(user_data);

            console.log("Mistakes Array: " , mistakes);
            give_feedback(mistakes, correct);

            // Show next question or view results button
            $("#next-question-button").show();
            $("#submit-button").hide();


        }

    });

});


function display_drag_drop_table() {
    let sounds = question["sounds"];

    let bird_order = question["correctAnswer"];

    // Arrange drop boxes in correct order
    for (let i = 0; i < bird_order.length; i++) {
        let row = $("<div></div>");
        row.addClass("drag-drop-row");



        let audio_box = $("<div></div>");

        audio_box.text("Audio " + (i + 1));
        audio_box.addClass("mapping-box-drag");
        audio_box.addClass("mapping-box-default-color")
        audio_box.attr("id", "draggable"+i);
        audio_box.draggable({
            });

        // Add the audio to the audio box
        let baseURL = "/static/"
        let audio = $("<audio controls></audio>");
        audio.attr("src", baseURL + sounds[i]);
        audio.attr("type", "audio/mpeg");
        audio_box.append(audio);
        
        row.append(audio_box);

        let drop_zone = $("<div></div>");
        drop_zone.text("Place correct audio here");
        drop_zone.addClass("mapping-box-drop");
        drop_zone.attr("id", "droppable"+i);
        drop_zone.droppable({
            drop: function(event, ui) {
                // Lock the draggable in the droppable
                ui.draggable.position({
                  my: "center",
                  at: "center",
                  of: $(this),
                  using: function(pos) {
                    $(this).animate(pos, "fast", "linear");
                  }
                });
                // Keep track if the droppable has an item
                $(this).data('hasItems', true);
                $(this).data('droppedItem_id', ui.draggable.attr('id'));
              },

            out: function(event, ui) {
                $(this).data('hasItems', false);
                $(this).removeData('droppedItem_id');
            }
        });

        $(row).append(drop_zone);
        
        //Display bird image 
        let bird_container = $("<div></div>");
        bird_container.addClass("bird-container");


        let bird_image = $("<img></img>");
        bird_image.attr("src", baseURL + question["images"][bird_order[i]]);
        $(bird_container).append(bird_image);

        let caption = $("<div></div>");
        caption.addClass("image-caption");
        caption.text(question["birds"][question["correctAnswer"][i]])
        //caption.text(question["correctOrder"][i]);
        $(bird_container).append(caption);

        $(row).append(bird_container);

        $("#drag-drop-table").append(row);
    }
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

function give_feedback(mistakes, correct) {
    $("#feedback").empty();
    
    if (mistakes.length == 0){
        $("#feedback").html("<h3 class='feedback-success'>Correct! Good job!<h3>");
        $("#feedback").addClass("correct-text");
    }

    else {

        let header = $("<h3>Incorrect</h3>").addClass("incorrect-text feedback-fail");
        $("#feedback").append(header);

        mistakes.forEach(function(mistake_group) {
            let droppedItem_id = mistake_group[0];
            let correct_id = mistake_group[1];

            let user_choice = question["birds"][droppedItem_id];
            let correct_choice = question["birds"][correct_id];

            user_choice_bird_path = "/learn/" + find_bird_id(user_choice);
            correct_choice_bird_path = "/learn/" + find_bird_id(correct_choice);

            user_choice_link = "<a href='" + user_choice_bird_path + "'>" + user_choice + "</a>";
            correct_choice_link = "<a href='" + correct_choice_bird_path + "'>" + correct_choice + "</a>";

            
            feedback_row = $("<p class='compare-feedback'></p>");
            feedback_row.addClass("feedback-fail-2");
            let mistake_text = $("<span class='grey-text'> You confused </span> " + user_choice_link + "<span class='grey-text'> with </span> " + correct_choice_link);
            feedback_row.append(mistake_text);

            feedback_row.click(function() {
                window.location.href = "/compare/" + find_bird_id(user_choice) + "/" + find_bird_id(correct_choice);
            });
        
            $("#feedback").append(feedback_row);


            // Highlight incorrect choices
            $(".ui-draggable#draggable"+ droppedItem_id).removeClass("mapping-box-default-color");
            $(".ui-draggable#draggable"+ droppedItem_id).addClass("incorrect");

            console.log($(".ui-draggable#"+ droppedItem_id))
            console.log(".ui-draggable#"+droppedItem_id)
        
        });

        correct.forEach(function(correct_id) {
            $(".ui-draggable#draggable"+ correct_id).removeClass("mapping-box-default-color");
            $(".ui-draggable#draggable"+ correct_id).addClass("correct");
        });

    }   
}

function find_bird_id(bird_name) {
    let id = -1;

    for (var bird_id in birds_list) {
        let bird = birds_list[bird_id];
        if (bird["name"] == bird_name) {
            id = bird["id"];

            console.log("Bird id for " + bird_name + ": ", id);
            return id
        }
    }

    return id;
}



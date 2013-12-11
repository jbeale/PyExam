$(document).ready(function() {
    $("#nextQuestionBtn").hide();
    $("#checkAnswerBtn").click(function() {
        grade();
    });
});

function grade() {
    $("input:radio[name=answer]").attr('disabled', 'disabled');
    var type = $("#qtype").val();
    var ans = "";
    if (type == "mc") {
        ans = $("input:radio[name=answer]:checked").val()
    } else if (type=="fitb") {
        ans = $("input:text[name=answer]").val()
    }
    var request = $.ajax({
        url: "answercheck",
        type: "GET",
        data: { guess: ans },
        dataType: "json"
    });
    request.done(function(data) {
        handleResponse(data)
    });
}

function handleResponse(data) {
    if (data.correct == "true") {
        $("#feedback").addClass("correct");
        $("#feedback").html("<strong>Correct!</strong>");
    } else {
        $("#feedback").addClass("incorrect");
        $("#feedback").html("<strong>Incorrect!</strong> " + data.feedback);
    }
    $("#feedback").slideDown();
    $("#checkAnswerBtn").hide();
    $("#nextQuestionBtn").show();
}
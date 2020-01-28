$(".fa-ticket-alt").click(function () {
    // Hide this one.
    // Show the other ones.
    var ticketIcon = $(this);
    ticketIcon.siblings().attr("hidden", false);
    ticketIcon.attr("hidden", true);
    // ticketIcon.hide();
    // var ticketControl = ticketIcon.parent();
    // var name = ticketControl.data("name");
    // var session = ticketControl.data("session");
    // alert("Clicked! " + name + " " + session);
});

$(".fa-check").click(function () {
    // Send the number of tickets to the API.
    // Hide this and the number input./
    // Show the ticket thing again.
    var checkIcon = $(this);
    checkIcon.siblings("i").attr("hidden", false);
    var numberInput = checkIcon.siblings("input");
    var numberOfTicketsToAward = numberInput.val();
    numberInput.attr("hidden", true);
    numberInput.val("1");
    checkIcon.attr("hidden", true);


    ticketControl = checkIcon.parent();
    var name = ticketControl.data("name");

    var session = ticketControl.data("session");

    // Send the request!
    csrfToken = $("input[name=csrfmiddlewaretoken]").val();

    // $.post("/raffle/api/tickets/", {"user": name, "session": session, "quantity": numberOfTicketsToAward});
    $.ajax({
        url: "/raffle/api/tickets/",
        type: "post",
        data: {"user": name, "session": session, "quantity": numberOfTicketsToAward},
        headers: {"X-CSRFToken": csrfToken},
        success: function(data) {
            console.log("Made the tickets!");
            location.reload();
        }
    });
    // console.log("Posting! " + numberOfTicketsToAward + " tickets to " + name + " for session: " + session);
});

gender = "female";
pronouns = {
    female: {
        "he": "she", "him": "her", "his": "her",
        "He": "She", "Him": "Her", "His": "Her"
    },
    male: {
        "he": "he", "him": "him", "his": "his",
        "He": "He", "Him": "Him", "His": "His",
    },
}

$('.quote-picker').change(function() {
    refreshQuoteOutput();
});

$('#name-input').change(function() {
    refreshQuoteOutput();
})

$('#name-input').on('input', function() {
    refreshQuoteOutput();
})

$('#target-grade-input').change(function() {
    refreshQuoteOutput();
})

$('#target-grade-input').on('input', function() {
    refreshQuoteOutput();
})

$('#achieved-grade-input').change(function() {
    refreshQuoteOutput();
})

$('#achieved-grade-input').on('input', function() {
    refreshQuoteOutput();
})

function refreshQuoteOutput() {
    quotes = collectQuotes()
    var template = Handlebars.compile(quotes);

    context = {name: getName(), ...getGrades()}
    p = pronouns[gender];
    context = {...context, ...p};
    console.log("context:", context);

    output = template(context);
    $("textarea#quote-output").val(output);
}

function getName() {
    return $("#name-input").val()
}

function getGrades() {
    return {
        target_grade: $("#target-grade-input").val(),
        achieved_grade: $("#achieved-grade-input").val(),
    }
}

function collectQuotes() {
    qs = $('.quote-picker:checkbox:checked').map(function() {
        return this.value;
    }).get();
    return qs.join(" ");
}

function copyToClipboard() {
    console.log("Copying!")
    $("#quote-output").select();
    document.execCommand("copy");
    // Un-select again
    // document.getSelection().removeAllRanges();
}



$('input[type=radio][name=gender-check]').change(function() {
    gender = this.value;
    refreshQuoteOutput();
});

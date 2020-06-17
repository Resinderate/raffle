$('.quote-picker').change(function() {
    refreshQuoteOutput();
});

$('#name-input').change(function() {
    refreshQuoteOutput();
})

$('#name-input').on('input', function() {
    refreshQuoteOutput();
})

function refreshQuoteOutput() {
    quotes = collectQuotes()
    var template = Handlebars.compile(quotes);
    output = template({name: getName()});
    $("textarea#quote-output").val(output);
}

function getName() {
    return $("#name-input").val()
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
    document.getSelection().removeAllRanges();
}

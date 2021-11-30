$("#start_button").click(function () {
    let data = {};
    $.ajax({
        type: "POST",
        url: window.location.pathname,
        data: JSON.stringify(data),
        contentType: "application/json;charset=UTF-8",
        success(msg) {
            $("#result").html(msg)
        }
    })
});
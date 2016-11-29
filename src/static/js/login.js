$('#login_a').click(function () {
    $("#loginModal").load(window.loginURL, function () {
        $('#loginModal').modal('toggle')
    }).ready();
});



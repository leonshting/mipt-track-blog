function onlike(e) {

    $.post($(e.target).attr('action'), $(e.target).serialize(), function (res) {
        console.log(res);
    });
    $(e.target).find('#likeblabel').text(parseInt($(e.target).find('#likeblabel').text()) + 1);
    $(e.target).find("#likeb").prop('disabled', true);

}
function result_getlike(data) {
    $("div.media-bottom").find('#likeblabel').text(data.postlike);
}

$(document).ready(
    function () {
        $(document).on("submit", "form[name=like_form]", function (e) {
            e.preventDefault();
            onlike(e);
        });


        window.setInterval(function () {
            id = $('form[name=like_form]').find(".comment-box").attr("id");
            var param = jQuery.param({id: id});
            $.get(window.location.pathname + "getlike/", result_getlike);
        });
    });


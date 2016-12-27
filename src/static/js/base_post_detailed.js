function onlike(e) {

    $.post($(e.target).attr('action'), $(e.target).serialize(), function (res) {
        console.log(res);
    });
    $(e.target).find('#likeblabel').text(parseInt($(e.target).find('#likeblabel').text()) + 1);
    $(e.target).find("#likeb").prop('disabled', true);

}

function result_getlike(data) {
    $("div.media-bottom").find('#likeblabel').text(data.postlike);
    var ids = $("div.comment-box");
    for (i = 0; i < ids.length; i++) {
        $(ids[i]).find('#likeblabel').text(data.commentlikes[parseInt($(ids[i]).attr("id"))]);
    }
}

function insert_comment(htmlString) {
    var comments = $('.comments-list');
    comments.prepend(htmlString);
    /*$(comments.children()[0]).find('form[name=like_form]').submit(function (e) {
     e.preventDefault();
     onlike(e)
     });*/
    console.log(htmlString);
}

function result_getcomms(result) {
    for (var key in result.commenttext) {
        insert_comment(result.commenttext[key]);
    }
}

$(document).ready(
    function () {
        $(document).on("submit", "form[name=like_form]", function (e) {
            e.preventDefault();
            onlike(e);
        });

        $('form[name=comment_form]').submit(function (e) {
            e.preventDefault();
            $.post($(e.target).attr('action'), $(e.target).serialize(), function (res) {
                console.log(res);
                id = $($(".comments-list").children()[0]).find(".comment-box").attr("id");
                var param = jQuery.param({id: id});

                $.get(window.location.pathname + "getcomms/?" + param, result_getcomms);
            });
            $(e.target).find('#id_text').val('');
        });


        window.setInterval(function () {
            id = $($(".comments-list").children()[0]).find(".comment-box").attr("id");
            var param = jQuery.param({id: id});
            $.get(window.location.pathname + "getlike/", result_getlike);
            $.get(window.location.pathname + "getcomms/?" + param, result_getcomms);
        }, 5000);

    });



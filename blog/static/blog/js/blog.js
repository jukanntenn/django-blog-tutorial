/**
 * Created by xueguang on 2016/8/4.
 */
/*
 extend the template js code
 */

/*
 * for archive
 *
 * */
var randomSize = [15, 16, 17, 18, 19, 20, 21, 22];
$(
    $('.widget-archives .icon').click(function () {
        $(this).next().slideToggle(500);

        // any more elegent way?
        if ($(this).hasClass('icon ion-minus')) {
            $(this).removeClass();
            $(this).addClass('icon ion-plus');
        } else {
            $(this).removeClass();
            $(this).addClass('icon ion-minus');
        }
    }),

    $('.comment-panel .ion-chatbox-working').click(function () {
        $(this).parent().siblings('.inner-panel , .comment-form').slideToggle(400);
        $(this).parent().siblings(':last').children(':button').click(function () {
            $(this).parent().parent().children('.inner-panel , form').slideUp(400);
        });

        $($(this).parent().siblings('.inner-panel').children('a')).click(function () {

            $(this).parent().siblings(':last').children('textarea').val(
                '@' + $(this).parent().children('span').first().text() + ':'
            );
            return false
        });
        return false;
    }),


    $.each($('.widget-tag > a'), function () {
        var size = randomSize[Math.floor(Math.random() * randomSize.length)];
        $(this).css('font-size', size);
    })
);

//window.onload = function () {
//    var widget = document.getElementsByClassName('.widget-tag')[0];
//
//    var tags = widget.getElementsByTagName('a');
//    var randomSize = [15, 17, 19, 21];
//    for (var i = 0; i < tags.length; i++) {
//        tags[i].style.fontSize =
//            randomSize[Math.floor(Math.random() * randomSize.length)]
//    }
//};
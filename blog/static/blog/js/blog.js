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
        $(this).parent().siblings('.inner-panel , form').slideToggle(400);
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
    })
);
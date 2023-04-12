(function ($) {
    "use strict";

    //jQuery to collapse the navbar on scroll
    $(window).scroll(function() {
        if ($(".navbar").offset().top > 100) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
        } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
        }
    });

    /* -----------------------------------------
        fact counter
    ----------------------------------------- */
    $('.counter').counterUp({
        delay: 15,
        time: 2000
    });

    /*-------------------------------------------------
        wow js init
    --------------------------------------------------*/
    new WOW().init();


    /*--------------------------------------------------------
        video popup 
    --------------------------------------------------------*/
    $('.video-play-btn,.video-popup,.small-vide-play-btn').magnificPopup({
            type: 'iframe',
            removalDelay: 260,
            mainClass: 'mfp-zoom-in',
        });
        $.extend(true, $.magnificPopup.defaults, {
            iframe: {
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: 'v=',
                        src: 'https://www.youtube.com/embed/Wimkqo8gDZ0'
                    }
                }
            }
        });
    
    /*------------------
        back to top
    ------------------*/
    var btn = $('#back-to-top');

    $(window).scroll(function() {
    if ($(window).scrollTop() > 300) {
        btn.addClass('show');
    } else {
        btn.removeClass('show');
    }
    });

    btn.on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0}, '300');
    });

})(jQuery);

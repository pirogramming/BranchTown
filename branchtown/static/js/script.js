
// scrollHandler();
// $(window).on('scroll', scrollHandler);
//
//
// $('.to-top-btn').on('click', totop);
//
// function totop(){
// 	$('html, body').animate({scrollTop: '0px'}, 1000);
//
// }


        $(document).ready(function(){
        $(".dropdown").hover(
            function() {
                $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideDown("400");
                $(this).toggleClass('open');
            },
            function() {
                $('.dropdown-menu', this).not('.in .dropdown-menu').stop(true,true).slideUp("400");
                $(this).toggleClass('open');
            }
        );
    });
    $(document).ready(function()
    {
        /* smooth scrolling for scroll to top */
        $('.to-top-btn').bind('click', function()
        {
            $('body,html').animate({
                scrollTop: 0},
                1000);
        });
        //Easing Scroll replace Anchor name in URL and Offset Position
        $(function(){
            $('a[href*=#]:not([href=#])').click(function()
            {
                if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
                    var target = $(this.hash);
                    target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                    if (target.length) {
                        $('html,body').animate({
                            scrollTop: target.offset().top -420
                        }, 2500, 'easeOutBounce');
                        return false;
                    }
                }
            });
        });
    });

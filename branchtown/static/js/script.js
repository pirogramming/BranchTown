
scrollHandler();
$(window).on('scroll', scrollHandler);

// function scrollHandler(){
// 	var showlist = $('.playlists .playlist');
// 	var windowBottom = $(window).height() + $(window).scrollTop();
// 	$(showlist).each(function(){
// 		var listBottom = $(this).height()/2 + $(this).offset().top;
// 		if(windowBottom >= listBottom){
// 			$(this).animate({opacity : '1'}, 1000);
// 			}
// 		})
// 	};

//
// $(window).on('scroll', function() {
// 	var showlist = $('.playlists');
//     if($(window).scrollTop() >= $(showlist).offset().top + $(showlist).outerHeight() - window.innerHeight) {
//         $('.to-top-btn').fadeIn(500);
//     }else{
//     	$('.to-top-btn').fadeOut(500);
//     }
// });


$('.to-top-btn').on('click', totop);

function totop(){
	$('html, body').animate({scrollTop: '0px'}, 1000);

}


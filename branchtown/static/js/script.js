
scrollHandler();
$(window).on('scroll', scrollHandler);


$('.to-top-btn').on('click', totop);

function totop(){
	$('html, body').animate({scrollTop: '0px'}, 1000);

}



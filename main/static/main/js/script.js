$(document).ready(function(){
	$(window).scroll(function(){
		$('.main-image').css("opacity", 1 - $(window).scrollTop() / 800)
	})
});

$(document).ready(function(){
	$(window).scroll(function(){
		$('.right-box').css("opacity", 1 - $(window).scrollTop() / 800)
	})
});

$(document).ready(function(){
	$(window).scroll(function(){
		$('.left-box').css("opacity", 1 - $(window).scrollTop() / 800)
	})
});
// $(function() {
//     var slides = $('#isolated-tree');
//     var slideCount = 0;
//     var totalSlides = slides.length;
//     var slideCache = [];
//
//     (function preloader() {
//         if (slideCount < totalSlides) {
//             slideCache[slideCount] = new Image();
//             slideCache[slideCount].src = slides.eq(slideCount).find('img').attr('src');
//             slideCache[slideCount].onload = function () {
//                 slideCount++;
//                 preloader();
//             }
//         } else {
//             slideCount = 0;
//             SlideShow();
//         }
//     }());
//
//     function SlideShow() {
//         slides.eq(slideCount).fadeIn(1000).delay(2000).fadeOut(1000, function () {
//             slideCount < totalSlides - 1 ? slideCount++ : slideCount = 0;
//             SlideShow();
//         });
//     }
// });

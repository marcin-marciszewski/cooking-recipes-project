$(document).ready(function() {
//     $('#mainNav').mouseenter(function(){
//         $('#mainNav').addClass("bg-white");
//     });

//     $('#mainNav').mouseleave(function(){
//         $('#mainNav').addClass("bg-white");
//     // // });

    // // $(window).scroll(function() {
    // //   $('.navbar').addClass("bg-white");  
    // // });

    // var position = function() {
    //     return (Math.floor(screenY))
    // }



    

    

    var isInViewport = function(elem) {
        var bounding = elem.getBoundingClientRect();
        return (
            bounding.top >= 0 &&
            bounding.left >= 0 &&
            bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    };

   

    var image = document.querySelector('#one');
    window.addEventListener('scroll', function(event) {
        if (isInViewport(image)) {
            var element = document.getElementById("mainNav");
             element.classList.add(".bg-white");
            console.log("test")
        }
    }, false);
    
    
});

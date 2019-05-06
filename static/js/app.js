$(document).ready(function() {

    $('#add').click(function() {
        $('#ingredients-group').append(`<div class="flex"><input  type="text" class="form-control my-2 " name="ingredient" id="ingredient" placeholder="Ingredient" required/><input type="button" value="Delete" id="delete" class="btn btn-outline-danger btn-radius  my-2 ml-1"/></div>`);

    });

    $('body').on('click','#delete', function() {
        $(this).parent('div').remove()
    })





    // var isInViewport = function(elem) {
    //     var bounding = elem.getBoundingClientRect();
    //     return (
    //         bounding.top >= 0 &&
    //         bounding.left >= 0 &&
    //         bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    //         bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
    //     );
    // };



    // var image = document.querySelector('#one');
    // window.addEventListener('scroll', function(event) {
    //     if (isInViewport(image)) {
    //         var element = document.getElementById("mainNav");
    //          element.classList.add(".bg-white");
    //         console.log("test")
    //     }
    // }, false);


});

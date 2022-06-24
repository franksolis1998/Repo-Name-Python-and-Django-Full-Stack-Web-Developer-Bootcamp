// $('h1').click(function(){
//     $(this).text("I was changed!")
// })

// $('li').click(function()){
//     console.log('any li was clicked')
// }


// key press


// $('input').eq(0).keypress(function(event){
//     if (event.which === 13) {
//         $('h3').toggleClass('turnblue');
//     }
// })


// on()
// $('h1').on('dbclick', function()){
//     $(this.toggleClass('turnBlue'));
// }

$('input').eq(1).on('click',function(){
    $('.container').fadeOut(3000)
})
$(function(){
    $('.bars li .bar').each(function(key, bar){
        let percentage = $(this).data('percentage');
        $(this).animate({
            'height': percentage + '%'
        }, 2000);
    });
});
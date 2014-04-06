        var bt = $('#box').position().top;

$(window).scroll(function() {
        var wst = $(window).scrollTop();

        (wst >= bt) ?
        $('#box').css({position: 'fixed', top: 15+'px' }) :  
        $('#box').css({position: 'absolute', top: bt+'px' })

});
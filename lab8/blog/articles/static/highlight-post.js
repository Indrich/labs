$(document).ready(function(){
    

    $('.one-post').on('mouseenter', function(event) {
        $(this).find('.one-post-shadow').stop().animate({ opacity: '0.1' }, 300);
    }).on('mouseleave', function(event) {
        $(this).find('.one-post-shadow').stop().animate({ opacity: '0' }, 300);
    });


    var $logo = $('img[src="/static/dpb-logo.png"]');
    
    if ($logo.length) {
        var initialWidth = $logo.width();   
        var initialHeight = $logo.height(); 
        
        var ratio = initialHeight / initialWidth; 
        
        $logo.on('mouseenter', function() {
            var newWidth = initialWidth + 20;
            var newHeight = initialHeight + (20 * ratio); 
            
            $(this).stop().animate({ 
                width: newWidth + 'px',
                height: newHeight + 'px'
            }, 200);
        }).on('mouseleave', function() {
            $(this).stop().animate({ 
                width: initialWidth + 'px',
                height: initialHeight + 'px'
            }, 200);
        });
    } 

}); 
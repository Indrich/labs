$(document).ready(function(){
    var yPosition;
    var scrolled = 0;
    
    var $parallaxElements = $('.icons-for-parallax img');
    

    var $mainLogo = $('.header-text-area img');

    $(window).scroll(function() {

        scrolled = $(window).scrollTop();


        for (var i = 0; i < $parallaxElements.length; i++) {

            yPosition = (scrolled * 0.15 * (i + 1));
            $parallaxElements.eq(i).css({ top: yPosition + 'px' });
        }


        if ($mainLogo.length) {
            var logoPosition = scrolled * 0.2;
            $mainLogo.css({ 
                position: 'relative', 
                top: logoPosition + 'px' 
            });
        }
    });
});
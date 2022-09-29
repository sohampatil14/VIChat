$(document).ready(function(){
    $(".ham-ico").hover(function(){
        $(".bar2").css("opacity", "0");
        $(".bar1").css("transform", "translate(0, 11px) rotate(-45deg)");
        $(".bar3").css("transform", "translate(0, -11px) rotate(45deg)");
    }, function(){
        $(".bar2").css("opacity", "100");
        $(".bar1").css("transform", "translate(0, -11px) rotate(0deg)");
        $(".bar3").css("transform", "translate(0, 11px) rotate(-0deg)");
    });
});
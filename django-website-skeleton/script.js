$(document).ready(function(){
    $(".ham-ico").click(function(){
        $(".bar2").css("opacity", "0");
        $(".bar1").css("transform", "translate(0, 11px) rotate(-45deg)");
        $(".bar3").css("transform", "translate(0, -11px) rotate(45deg)");
    });
});
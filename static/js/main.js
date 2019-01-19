
$(document).ready(function () {
    $(".toggle").click(function () {
        if (! $("input[type=checkbox]").prop("checked")) {
            $("div.sidebar").removeClass("col-md-8").removeClass("col-sm-8").addClass("col-md-1").addClass("col-sm-1");
            $("div.espace").removeClass("col-md-3").removeClass("col-sm-3")
                .removeClass("col-md-offset-9").removeClass("col-sm-offset-9")
                .removeClass("col-lg-offset-9").removeClass("col-lg-3").css("opacity", 0);
            $("div.social").removeClass("col-md-1").removeClass("col-sm-1")
                .removeClass("col-md-offset-8").removeClass("col-sm-offset-8")
                .removeClass("col-lg-offset-8").removeClass("col-lg-8").css("opacity", 0);
            $(".logo").removeClass('hide');
        } else {
            $("div.sidebar").removeClass("col-md-1").removeClass("col-sm-1").addClass("col-md-8").addClass("col-sm-8");
            $("div.espace").addClass("col-md-3").addClass("col-sm-3")
                .addClass("col-md-offset-9").addClass("col-sm-offset-9")
                .addClass("col-lg-offset-9").addClass("col-lg-3").css("opacity", 0.25);
            $("div.social").addClass("col-md-1").addClass("col-sm-1")
                .addClass("col-md-offset-8").addClass("col-sm-offset-8")
                .addClass("col-lg-offset-8").addClass("col-lg-1").css("opacity", 1);
            $(".logo").addClass("hide");
        }
    });
});
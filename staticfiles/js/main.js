
$(document).ready(function () {
    $(".toggle").click(function () {
        if (! $("input[type=checkbox]").prop("checked")) {
            $("div.sidebar").removeClass("col-md-7").removeClass("col-sm-7").addClass("col-md-1").addClass("col-sm-1")
                .css("background-color", "transparent");
            $("div.espace").removeClass("col-md-4").removeClass("col-sm-4")
                .removeClass("col-md-offset-8").removeClass("col-sm-offset-8")
                .removeClass("col-lg-offset-8").removeClass("col-lg-4").css("opacity", 0);
            $("div.social").removeClass("col-md-1").removeClass("col-sm-1")
                .removeClass("col-md-offset-7").removeClass("col-sm-offset-7")
                .removeClass("col-lg-offset-7").removeClass("col-lg-7").css("opacity", 0);
            $(".sidebar-container").css("opacity", 0).css("right", "25vw");
        } else {
            $("div.sidebar").removeClass("col-md-1").removeClass("col-sm-1").addClass("col-md-7").addClass("col-sm-7")
                .css("background-color", "#000");
            $("div.espace").addClass("col-md-4").addClass("col-sm-4")
                .addClass("col-md-offset-8").addClass("col-sm-offset-8")
                .addClass("col-lg-offset-8").addClass("col-lg-4").css("opacity", 1);
            $("div.social").addClass("col-md-1").addClass("col-sm-1")
                .addClass("col-md-offset-7").addClass("col-sm-offset-7")
                .addClass("col-lg-offset-7").addClass("col-lg-1").css("opacity", 1);
            $(".sidebar-container").css("opacity", 1).css("right", 0);
        }
    });
    $("#about").hover( function () {
        $('#sidebar-menu').html('<ul class="sidebar-list">' +
            '<li><a href=google.com">Our motivation</li></a>' +
            '<li><a href="google.com">About this website</li></a>'+
            '<li><a href="google.com">Meet the team</li></a>' +
            '<li><a href="google.com">Achievements</li></a>' +
            "</ul>");
        $("#about").addClass("hover");
        $("#departments").removeClass("hover");
        $("#logique").removeClass("hover");
        $("#events").removeClass("hover");
        $("#gallery").removeClass("hover");
        $("#projects").removeClass("hover");
    }, function () {});
    $("#departments").hover(function () {
        $('#sidebar-menu').html('<ul class="sidebar-list">' +
            '<li><a href="google.com">Competitive Programming</li></a>' +
            '<li><a href="google.com">Development and Creative</li></a>'+
            '<li><a href="google.com">Robotics</li></a>' +
            "</ul>");
        $("#about").removeClass("hover");
        $("#departments").addClass("hover");
        $("#logique").removeClass("hover");
        $("#events").removeClass("hover");
        $("#gallery").removeClass("hover");
        $("#projects").removeClass("hover");
    }, function () {});

    $("#logique").hover(function () {
        $('#sidebar-menu').html('<ul class="sidebar-list">' +
            '<li><a href="google.com">About</li></a>' +
            '<li><a href="google.com">Upcoming</li></a>' +
            '<li><a href="google.com">Gallery</li></a>'+
            '<li><a href="google.com">2018</li></a>' +
            '<li><a href="google.com">Apply for Invitation</li></a>' +
            "</ul>");
        $("#about").removeClass("hover");
        $("#departments").removeClass("hover");
        $("#logique").addClass("hover");
        $("#events").removeClass("hover");
        $("#gallery").removeClass("hover");
        $("#projects").removeClass("hover");
    }, function () {});

    $("#events").hover(function () {
        $('#sidebar-menu').html('<ul class="sidebar-list">' +
            '<li><a href="google.com">Upcoming</li></a>' +
            '<li><a href="google.com">Running</li></a>'+
            '<li><a href="google.com">Past</li></a>' +
            "</ul>");
        $("#about").removeClass("hover");
        $("#departments").removeClass("hover");
        $("#logique").removeClass("hover");
        $("#events").addClass("hover");
        $("#gallery").removeClass("hover");
        $("#projects").removeClass("hover");
    }, function () {});

    $("#gallery").hover(function () {
        $('#sidebar-menu').html('<ul class="sidebar-list">' +
            '<li><a href="google.com">Events in school</li></a>' +
            '<li><a href="google.com">Events outside school</li></a>'+
            '<li><a href="google.com">Projects</li></a>' +
            "</ul>");
        $("#about").removeClass("hover");
        $("#departments").removeClass("hover");
        $("#logique").removeClass("hover");
        $("#events").removeClass("hover");
        $("#gallery").addClass("hover");
        $("#projects").removeClass("hover");
    }, function () {});

    $("#projects").hover(function () {
        $('#sidebar-menu').html("");
        $("#about").removeClass("hover");
        $("#departments").removeClass("hover");
        $("#logique").removeClass("hover");
        $("#events").removeClass("hover");
        $("#gallery").removeClass("hover");
        $("#projects").addClass("hover");
    }, function () {});

    $("a").hover(function(){
        $(".social").toggleClass("color-"+ this.className );
    });
});
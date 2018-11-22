
const IP = "http://172.20.10.2:5000";
const USERS_ENDPOINT = "/api/v1/users/search_users";
const EVENTS_ENDPOINT = "/api/v1/events/search_events";
var url = IP+USERS_ENDPOINT;
var url2 = IP+EVENTS_ENDPOINT;

const urlParams = new URLSearchParams(window.location.search);
const f_username = urlParams.get('userload');

$( document ).ready(function() {
    loadMyEvents();
    loadMyRecommendedEvents();
});

function loadMyEvents(){
    var data_to_send = {
        "type" : "GET_PARAMETER",
        "username": f_username,
        "param": "events"
    }
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": url,
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache",
      },
      "processData": false,
      "data": JSON.stringify(data_to_send)
    };

    $.ajax(settings).done(function (response) {
      console.log(response);
      if(0 >= response.users.length){
          response.users.forEach(function(element) {
            var img = $('<img />').attr({
                  'id': 'myImage'+element.name,
                  'src': '../FrontEnd/img/gallery/' + element.image,
                  'width': "200px",
                  'title': "Name: " + element.name + "\nPlace: " + element.event_location + "\nDate: " + element.event_date
              }).appendTo('#myEvents');
          });

          // Gallery carousel (uses the Owl Carousel library)
          $(".gallery-carousel").owlCarousel({
            autoplay: true,
            dots: true,
            loop: true,
            center:true,
            responsive: { 0: { items: 1 }, 768: { items: 3 }, 992: { items: 4 }, 1200: {items: 5}
            }
          });
      }else{
          $( "#myEvents" ).removeClass( "owl-carousel gallery-carousel" );
          // $("#myEvents").children('.owl-stage-outer').remove();
          $( "#gallery" ).removeClass( "wow fadeInUp" );
          $( "<p>You have not registered to an event D:</p>" ).appendTo('#myEvents');
      }
    });
}

function loadMyRecommendedEvents(){
    var data_to_send = {
        "type" : "GET_USER_RECOMMENDATIONS",
        "username": f_username
    }
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": url,
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "cache-control": "no-cache",
      },
      "processData": false,
      "data": JSON.stringify(data_to_send)
    };

    $.ajax(settings).done(function (response) {
      console.log(response);
      if(0 <= response.users.length){
          response.users.forEach(function(element) {
            var img = $('<img />').attr({
                  'id': 'myImage'+element.name,
                  'src': '../FrontEnd/img/gallery/' + element.image,
                  'width': "200px",
                  'title': "Name: " + element.name + "\nPlace: " + element.event_location + "\nDate: " + element.event_date
              }).appendTo('#myRecommendedEvents');
          });

          // Gallery carousel (uses the Owl Carousel library)
          $(".gallery-carousel").owlCarousel({
            autoplay: true,
            dots: true,
            loop: true,
            center:true,
            responsive: { 0: { items: 1 }, 768: { items: 3 }, 992: { items: 4 }, 1200: {items: 5}
            }
          });
      }else{
          $( "#myRecommendedEvents" ).removeClass( "owl-carousel gallery-carousel" );
          $( "#gallery2" ).removeClass( "wow fadeInUp" );
          $( "<p class='text-center'>You have not registered to an event D:</p>" ).appendTo('#myRecommendedEvents');
      }
    });
}

function goToMyProfile(){
     window.location.href = './userprofile.html?userload='+f_username+'';
}

function goToMyPreferences(){
     window.location.href = './userpreferences.html?userload='+f_username+'';
}

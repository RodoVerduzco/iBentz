
const URL = "http://localhost:5000/api/v1/events/search_events";
//var URL = "http://172.20.10.2:5000/api/v1/users/search_users";

jQuery(document).ready(function($) {
  "use strict";

  //Contact
  $('#add-events-form').submit(function() {
    var nombre = $("#event-name").text();
    var date = $("#event-date").text();
    var num = $("#event-participants").text();
    var location = $("#event-location option:selected").val();
    var image = $("#event-img").text();
    var desc = $("#event-desc").text();
    var info = $("#event-info").text();
    var org = $("#event-org").text();
    var cat = $("input[type='radio'][name='gridRadios']:checked").val();

    var data_to_send = {
        "type" : "INSERT",
        "name": nombre,
        "image": image,
        "event_date": date,
        "max_participants": num,
        "event_location": location,
        "description": desc,
        "info": info,
        "category": cat,
        "organizer": org,
        "status": "ACTIVE"
    };

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": URL,
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache",
        },
        "processData": false,
        "data": JSON.stringify(data_to_send)
    };

    $.ajax(settings).done(function (response) {
      console.log(data_to_send);
      console.log(response);

    });

  });

});

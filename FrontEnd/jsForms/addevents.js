
//const EVENTS_ENDPOINT = "/api/v1/events/search_events";

jQuery(document).ready(function($) {
  "use strict";

  //Contact
  $('#add-events-form').submit(function() {
    var nombre = $("#event-name").val();
    var date = $("#event-date").val();
    var num = $("#event-participants").val();
    var location = $("#event-location option:selected").val();
    var image = $("#event-img").val();
    var desc = $("#event-desc").val();
    var info = $("#event-info").val();
    var org = $("#event-org").val();
    var cat = $("input[type='radio'][name='gridRadios']:checked").val().toUpperCase();

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
        "url": IP + EVENTS_ENDPOINT,
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
       alert("Evento Agregado");
     });

  });


  $('#add-organizer-form').submit(function(e) {

    var nombre = $("#org-name").val();
    var pass = $("#org-password").val();
    var mail = $("#org-mail").val();
    var location = $("#org-loc option:selected").val();

    var data_to_send = {
        "type" : "INSERT_USER",
        "username": nombre,
        "password": pass,
        "email": mail,
        "age": 0,
        "user_type": "ORG",
        "first_name": nombre.toUpperCase(),
        "last_name": "NONE",
        "sex": "M",
        "birthday": "0-0-0",
        "location": location
    };

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": IP + USERS_ENDPOINT,
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
       alert("Organizador Agregado");
     });

  });



});

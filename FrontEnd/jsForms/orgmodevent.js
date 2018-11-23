

//const IP = "http://0.0.0.0:5000";
// const IP = "http://0.0.0.0:5000"
// const EVENTS_ENDPOINT = "/api/v1/events/search_events";
var url = IP+EVENTS_ENDPOINT;

const urlParams = new URLSearchParams(window.location.search);
const f_getID = localStorage.getItem('userload');

function setValuesOnLoad( jQuery ) {
    // Code to run when the document is ready.

    // Get ID of user:
    // Test ID: 5bf03ffd43172e1f783de20b
    var data_to_send = {
        "type" : "SEARCH_ID",
        "event_id": f_getID
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
    }

    $.ajax(settings).done(function (response) {
      console.log(data_to_send);
      console.log(response);

      $("#name").val(response["events"].name);
      $("#date").val(response["events"].event_date);
      $("#imageurl").val(response["events"].image);
      $("#location").val(response["events"].event_location);
      $("#max_participants").val(response["events"].max_participants);
      $("#first_name").val(response["events"].first_name);
      $("#last_name").val(response["events"].last_name);
      $("input[name=radiocat][value='"+response["events"].category+"']").prop('checked', true);
      $("#description").val(response["events"].description);
      $("#addinfo").val(response["events"].ext_info);

      // "name": f_name,
      // "image": f_imageurl,
      // "event_date": f_date,
      // "max_participants": f_max_participants,
      // "event_location": f_location,
      // "description": f_desc,
      // "info": f_addinfo,
      // "category": f_cat,
      // "status": "f_status",
      // "num_registered": "num_registered"

  });
}


jQuery(document).ready(function($) {
  "use strict";

 setValuesOnLoad();

  //Contact
  $('form.orgmodeventForm').submit(function() {
    var f = $(this).find('.form-group'),
      ferror = false,
      dateExp = /^(\d{4})\-(\d{1,2})\-(\d{1,2})$/i,
      imageurlExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;
      // Reference: https://www.the-art-of-web.com/javascript/validate-date/
      // dateExp = /^(\d{1,2})\-(\d{1,2})\-(\d{4})$/i;

    f.children('input').each(function() { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;

          case 'imageurl':
            if (!imageurlExp.test(i.val())) {
              ferror = ierror = true;
            }
            break;

            case 'date':
              if (!dateExp.test(i.val())) {
                ferror = ierror = true; // true = Yes, there's an error with the input
            }else{
                  // if(1){
                  //     ferror = ierror = true;
                  // }
              }
              break;

          case 'checked':
            if (!i.attr('checked')) {
              ferror = ierror = true;
            }
            break;

          case 'regexp':
            exp = new RegExp(exp);
            if (!exp.test(i.val())) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validation').html((ierror ? (i.attr('data-msg') !== undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });

    f.children('textarea').each(function() { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validation').html((ierror ? (i.attr('data-msg') != undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });
    if (ferror) return false;
    else var str = $(this).serialize();

    // Here starts the Login Query to Python Server.
    var f_name = $("#name").val();
    var f_date = $("#date").val();
    var f_imageurl = $("#imageurl").val();
    var f_location = $("#location").val();
    var f_max_participants = $("#max_participants").val();
    // var f_status = $('input[name=radiostatus]:checked').val();
    var f_cat = $('input[name=radiocat]:checked').val();
    var f_desc = $("#description").val();
    var f_addinfo = $("#addinfo").val();

    // var f_password = $("#password").val();

    var data_to_send = {
        "type" : "UPDATE_EVENT",
        // "organizer": f_username,
        "event_id": f_getID,
        "name": f_name,
        "image": f_imageurl,
        "event_date": f_date,
        "max_participants": f_max_participants,
        "event_location": f_location,
        "description": f_desc,
        "info": f_addinfo,
        "category": f_cat,
        // "status": "f_status",
        // "num_registered": "num_registered"
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
    }

    $.ajax(settings).done(function (response) {
      console.log(data_to_send);
      console.log(response);
      // // alert(response);
     // if(response["users"] === "user inserted successfully"){
     //     console.log("Good");
     //     // Success message
     $("#sendmessage").addClass("show");
     $("#errormessage").removeClass("show");
     $('.contactForm').find("input, textarea").val("");
     //    // Redirect to User Interface...
     //    window.location.replace("userprofile.html?userload="+f_username);
     // }else {
     //     // You shouldn't get here...
     //    console.log("No estas registrado");
     //    // alert("ploxsignup");
     // }
    });

    // Refer to contactform.js to know the basic structure provided by the template.

    return false;
  });

});

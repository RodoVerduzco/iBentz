

//var url = "http://0.0.0.0:5000/api/v1/users/search_users";
//var url = "http://0.0.0.0:5000/api/v1/users/search_users";
var url = IP + USERS_ENDPOINT

const urlParams = new URLSearchParams(window.location.search);
const f_username = localStorage.getItem('userload');

// Passing a named function instead of an anonymous function.

function setValuesOnLoad( jQuery ) {
    // Code to run when the document is ready.

    // Get ID of user:
    var data_to_send = {
        "type" : "GET_PARAMETER",
        "username": f_username,
        "param": "preferences"
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
      for (var i = 0; i < response["users"]["user"].length; i++) {
          console.log(response["users"]["user"][i]);
          $("input[name='mypreferences'][value='"+response["users"]["user"][i]+"']").prop('checked',true);
      }
  });
}


jQuery(document).ready(function($) {
  "use strict";

 setValuesOnLoad();

  //Contact
  $('form.profileForm').submit(function() {
    // Here starts the Login Query to Python Server.
    // var f_username = $("#username").val();
    var mypreferences = [];

    $.each($("input[name='mypreferences']:checked"), function(){
        mypreferences.push($(this).val());
    });
    // // alert("My favourite sports are: " + mypreferences.join(", "));
    console.log(mypreferences.join(", "));

    var data_to_send = {
        "type" : "UPDATE_PREFERENCES",
        "username": f_username,
        "preferences": mypreferences
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
     //    // Here you should stablish your ID session.
     //    // Maybe hardcore cookie in js, but that's not correct in terms of formal development.
     //
     //
     //    // Redirect to User Interface...
     //    window.location.replace("userpreferences.html?userload="+f_username);
     // }else {
     //     // You shouldn't get here...
     //    console.log("You shouldn't get here...");
     //    // // alert("ploxsignup");
     //    // Error Message
     //    // $("#sendmessage").removeClass("show");
     //    // $("#errormessage").addClass("show");
     //    // $('#errormessage').html("Usuario no registrado o password incorrecto.");
     // }
    });

    // Refer to contactform.js to know the basic structure provided by the template.

    return false;
  });

});

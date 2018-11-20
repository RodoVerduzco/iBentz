
// var url = "http://localhost:5000/api/v1/users/search_users?type=INSERT_USER";
var url = "http://172.20.10.2:5000/api/v1/users/search_users";

const urlParams = new URLSearchParams(window.location.search);
const f_username = urlParams.get('userload');

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

      // var favorite = [];
      //       $.each($("input[name='sport']:checked"), function(){
      //           favorite.push($(this).val());
      //       });
      //       alert("My favourite sports are: " + favorite.join(", "));
      //   });
      // $("#preferences").val(response["user"].email);
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
    // alert("My favourite sports are: " + mypreferences.join(", "));
    console.log(mypreferences.join(", "));

    var data_to_send = {
        "type" : "ADD_PREFERENCES",
        "username": f_username,
        "preferences": mypreferences
        // "preferences": ""
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
      // alert(response);
     if(response["users"] === "user inserted successfully"){
         console.log("Good");
        // Here you should stablish your ID session.
        // Maybe hardcore cookie in js, but that's not correct in terms of formal development.


        // Redirect to User Interface...
        window.location.replace("userpreferences.html?userload="+f_username);
     }else {
         // You shouldn't get here...
        console.log("You shouldn't get here...");
        // alert("ploxsignup");
        // Error Message
        // $("#sendmessage").removeClass("show");
        // $("#errormessage").addClass("show");
        // $('#errormessage').html("Usuario no registrado o password incorrecto.");
     }
    });

    // Refer to contactform.js to know the basic structure provided by the template.

    return false;
  });

});

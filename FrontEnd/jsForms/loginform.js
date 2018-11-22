
// var url = "http://localhost:5000/api/v1/users/search_users?type=VALIDATE_USER";
var url = "http://172.20.10.2:5000/api/v1/users/search_users";

jQuery(document).ready(function($) {
  "use strict";

  //Contact
  $('form.loginForm').submit(function() {
    var f = $(this).find('.form-group'),
      ferror = false,
      emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;

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

          case 'email':
            if (!emailExp.test(i.val())) {
              ferror = ierror = true;
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
    var f_username = $("#email").val();
    var f_password = $("#password").val();

    var data_to_send = {
        "type" : "VALIDATE",
        "username" : f_username,
        "password" : f_password
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
      console.log(response);
      // alert(response);
     if(response["users"]["user_type"] === "INVALID"){
         console.log("No estas registrado");
         // Error Message
         $("#sendmessage").removeClass("show");
         $("#errormessage").addClass("show");
         $('#errormessage').html("Usuario no registrado o password incorrecto.");
          alert(response);
     }else {
         console.log("Good");
         console.log(response["users"]["user_type"]);
         // Success message
         // $("#sendmessage").addClass("show");
         // $("#errormessage").removeClass("show");
         // $('.contactForm').find("input, textarea").val("");
         // alert(response);
         // alert(response["users"]["user_type"]);

         // Here you should stablish your ID session.
         // Maybe hardcore cookie in js, but that's not correct in terms of formal development.

         // Redirect to User Interface...
         if(response["users"]["user_type"]==="USER"){
             window.location.replace("./userinterface.html?userload="+f_username);
         }else if(response["users"]["user_type"]==="ORG"){
             console.log("You are a ORG");
             // alert(response["users"]["user_type"]);
             window.location.replace("./orginterface.html?userload="+f_username);
         }else{
              console.log("What are you?");
         }
     }
    });

    // Refer to contactform.js to know the basic structure provided by the template.

    return false;
  });

});

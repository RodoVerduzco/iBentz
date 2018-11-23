

//var url = "http://localhost:5000/api/v1/users/search_users";
//var url = "http://localhost:5000/api/v1/users/search_users";

jQuery(document).ready(function($) {
  "use strict";

  //Contact
  $('form.signupForm').submit(function() {
    var f = $(this).find('.form-group'),
      ferror = false,
      dateExp = /^(\d{4})\-(\d{1,2})\-(\d{1,2})$/i,
      emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;
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

          case 'email':
            if (!emailExp.test(i.val())) {
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
    var f_username = $("#username").val();
    var f_email = $("#email").val();
    var f_password = $("#password").val();
    // var f_user_type = $("#user_type").val();
    var f_age = $("#age").val();
    var f_first_name = $("#first_name").val();
    var f_last_name = $("#last_name").val();
    // var f_sex = $("#sex").val();
    var f_sex = $('input[name=radiosex]:checked').val();
    var f_birthday = $("#birthday").val();
    var f_location = $("#location").val();

    var data_to_send = {
        "type" : "INSERT_USER",
        "username": f_username,
        "email": f_email,
        "password":f_password,
        "user_type": "USER",
        "age": f_age,
        "first_name": f_first_name,
        "last_name": f_last_name,
        "sex": f_sex,
        "birthday": f_birthday,
        "location": f_location,
        "preferences": ""
    }
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
    }

    $.ajax(settings).done(function (response) {
      console.log(data_to_send);
      console.log(response);
      // alert(response);
     if(response["users"] === "user inserted successfully"){
         console.log("Good");
         // Success message
         // alert("Plox");
         $("#sendmessage").addClass("show");
         $("#errormessage").removeClass("show");
         $('.contactForm').find("input, textarea").val("");

        // Here you should stablish your ID session.
        // Maybe hardcore cookie in js, but that's not correct in terms of formal development.
        localStorage.setItem("userload", f_username);
        localStorage.getItem("logged","true");

        // Redirect to User Interface...
        window.location.replace("userinterface.html?userload="+f_username);
     }else {
         // You shouldn't get here...
        console.log("No estas registrado");
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

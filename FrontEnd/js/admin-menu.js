// const IP = "http://0.0.0.0:5000";
// const USERS_ENDPOINT = "/api/v1/users/search_users";

function users_table() {
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": IP + USERS_ENDPOINT,
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "cache-control": "no-cache"
    },
    "processData": false,
    "data": "{\n\t\"type\": \"READ_ALL\"\n\n}"
  };

  $.ajax(settings).done(function (response) {
    response.users.forEach(function (element) {
      var events="";
      var eventos = element.events;

      if (!element.events || element.events=="")
        events = "Sin Eventos";
      else{
        eventos.forEach(function (elements){
          events += elements.name + "-" + elements.date + "| ";
        });
      }

      var row = "<tr><td>"+ element.first_name +"</td>"+
      "<td>"+ element.last_name + "</td>  "+
      "<td>"+ element.email + "</td> "+
      "<td>"+ element.preferences + "</td>"+
      "<td>"+ events + "</td></tr>";
      $('#users-table').append(row);

    });
  });
}
$( "#add-organizer-form" ).submit(function( event ) {
  //alert( "Handler for .submit() called." );
  event.preventDefault();
  createOrg();
});

function createOrg(){
  var data_to_send={
    "type":"INSERT_USER",
    "user_type":"ORG",
    "age":"30",
    "birthday":"2000-12-12",
    "email":$("#org_mail").val(),
    "first_name":$("#org_name").val(),
    "last_name":"",
    "location":$("#org_loc").val(),
    "username":$("#org_name").val(),
    "password":$("#org_password").val(),
    "sex":"C"
  };
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": IP + USERS_ENDPOINT,
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "cache-control": "no-cache",
      "Postman-Token": "49efbc9e-d034-46d0-a1a6-4f2de1acf5cd"
    },
    "processData": false,
    "data": JSON.stringify(data_to_send)
  };

  $.ajax(settings).done(function (response) {
    console.log(response);
    if(response.users == "user inserted successfully"){
      alert("ORG created successfully");
    }
    else {
      alert("ERROR creating user");
    }
  });
}

users_table();

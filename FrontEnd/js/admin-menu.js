const IP = "http://0.0.0.0:8080";
const USERS_ENDPOINT = "/api/v1/users/search_users";

function users_table() {
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": IP + USERS_ENDPOINT,
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "cache-control": "no-cache",
      "Postman-Token": "5db49bd8-9a43-4222-ae4f-8096b9ed924d"
    },
    "processData": false,
    "data": "{\n\t\"type\": \"READ_ALL\"\n\n}"
  };

  $.ajax(settings).done(function (response) {
    response.users.forEach(function (element) {
      var eventos = element.events;
      if (!element.events)
      eventos = "Sin Eventos";

      var row = "<tr><td>"+ element.first_name +"</td>"+
      "<td>"+ element.last_name + "</td>  "+
      "<td>"+ element.email + "</td> "+
      "<td>"+ element.preferences + "</td>"+
      "<td>"+ eventos + "</td></tr>";

      $('#users-table').append(row);
    });
  });
}

users_table();

const IP = "http://172.20.10.2:5000";
const EVENTS_ENDPOINT = "/api/v1/users/search_users";
var url = IP+EVENTS_ENDPOINT;

const urlParams = new URLSearchParams(window.location.search);
const f_username = urlParams.get('userload');

$( document ).ready(function() {
    loadActiveUsers();
});

function loadActiveUsers(){

    deleteChildsElement("eventsActiveLista");
    var data_to_send = {
        "type" : "GET_ORG_EVENTS",
        "username": f_username,
        "status": "ACTIVE"
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
        var html = "";
        for (var i = 0; i < response["users"].length; i++) {
           var idEvent = response["users"][i].id;
           var imageurl = response["users"][i].image;
           var name = response["users"][i].name;

            html += "<div class='row'><div class='span4'>";
            html += "<img class='img-left' width='auto' height='150px' src='../FrontEnd/img/gallery/"+imageurl+"'/>";

            html += "<div class='content-heading'><h3>"+name+"</h3></div>";
            // html += "<div class='text-center'>";
			html +=	"<button type='button' class='myButton' onclick='location.href='./userprofile.html''>Modify</button>";
			html +=	"<button type='button' class='myButton' onclick='location.href='./userpreferences.html''>Inactive</button>";
			// html += "</div>";
            html += "</div></div>";
            html += "</br></br></br>";
        }
        $("#eventsActiveLista").append(html);
    });
}

function loadInactiveUsers(){
    deleteChildsElement("eventsInactiveLista");
    var data_to_send = {
        "type" : "GET_ORG_EVENTS",
        "username": f_username,
        "status": "INACTIVE"
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


        $("#eventsInactiveLista").append(html);
    });
}

function modifyEvent(){
    location.href='./userprofile.html;
}

function deleteEvent(){
    deleteChildsElement("eventsActiveLista");
    deleteChildsElement("eventsInactiveLista");

    var data_to_send = {
        "type" : "GET_ORG_EVENTS",
        "username": f_username,
        "status": "INACTIVE"
    }

    loadActiveUsers();
    loadInactiveUsers();
}

function deleteChildsElement(nombre){
  var element = document.getElementById(nombre);
  while (element.hasChildNodes()) {
      element.removeChild(element.lastChild);
  }
}

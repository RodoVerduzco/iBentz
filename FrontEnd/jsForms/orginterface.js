
//const IP = "http://0.0.0.0:5000";
// const IP = "http://0.0.0.0:5000";
// const USERS_ENDPOINT = "/api/v1/users/search_users";
// const EVENTS_ENDPOINT = "/api/v1/events/search_events";
var url = IP+USERS_ENDPOINT;
var url2 = IP+EVENTS_ENDPOINT;

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
           var desc = response["users"][i].description;
           var date = response["users"][i].event_date;

            html += "<div class='d-flex justify-content-center flex-row'>";
                html += "<div class='d-flex align-items-stretch col'>";
                    html += "<img class='img-left' width='auto' height='150px' src='../FrontEnd/img/gallery/"+imageurl+"'/>";
                html += "</div>";
                html += "<div class='d-flex align-items-start flex-column col-6'>";
                    html += "<div class='p-2'><h3>"+name+"</h3></div>";
                    html += "<div class='p-2'>"+desc+"</div>";
                    html += "<div class='p-2'>"+date+"</div>";
                html += "</div>";
                html += "<div class='d-flex align-items-center col'>";
                    // html += "<div class='text-center'>";
        			html +=	"<button type='button' class='myButton' value='"+idEvent+"' onclick='modifyEvent(this.value)'>MODIFY</button>";
                html += "</div>";
                html += "<div class='d-flex align-items-center'>";
        			html +=	"<button type='button' class='myButton' value='"+idEvent+"' onclick='deleteEvent(this.value)'>SET INTACTIVE</button>";
    			html += "</div>";
            html += "</div>";
            html += "</br>";
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
        console.log(response);
        var html = "";
        for (var i = 0; i < response["users"].length; i++) {
           var idEvent = response["users"][i].id;
           var name = response["users"][i].name;
           var desc = response["users"][i].description;
           var ext_info = response["users"][i].ext_info;

           var date = response["users"][i].event_date;
           var imageurl = response["users"][i].image;

           var category = response["users"][i].category;
           var event_location = response["users"][i].event_location;
           var max_participants = response["users"][i].max_participants;
           var num_registered = response["users"][i].num_registered;

            html += "<div class='d-flex justify-content-center flex-row'>";
                html += "<div class='d-flex align-items-stretch col'>";
                    html += "<img class='img-left' width='auto' height='150px' src='../FrontEnd/img/gallery/"+imageurl+"'/>";
                html += "</div>";
                html += "<div class='d-flex align-items-start flex-column col'>";
                    html += "<div class='p-2'><h3>"+name+"</h3></div>";
                    html += "<div class='p-2'>"+desc+"</div>";
                    html += "<div class='p-2'>"+ext_info+"</div>";
                    html += "<div class='p-2'>EVENTO TERMINADO</div>";
                html += "</div>";
                html += "<div class='d-flex align-items-center col'>";
                    html += "<div class='p-2'>Fecha: <br>"+date+"</div>";
                    html += "<div class='p-2'>Categoría: "+category+"</div>";
                html += "</div>";
                html += "<div class='d-flex align-items-center col'>";
                    html += "<div class='p-2'>Limite de Participantes: "+max_participants+"</div>";
                    html += "<div class='p-2'>Participantes registrados: "+num_registered+"</div>";
    			html += "</div>";
            html += "</div>";
            html += "</br>";
        }
        $("#eventsInactiveLista").append(html);
    });
}

function modifyEvent(idEvent){
    // alert(idEvent);
     window.location.href = 'orgmodevent.html?userload='+idEvent+'';
}

function deleteEvent(idEvent){
    deleteChildsElement("eventsActiveLista");
    deleteChildsElement("eventsInactiveLista");

    var data_to_send = {
        "type" : "DELETE",
        "id": idEvent,
        // "status": "INACTIVE"
    }
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": url2,
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
        loadActiveUsers();
        loadInactiveUsers();
    });
}

function createEvent(){
     window.location.href = './orginsevent.html?userload='+f_username+'';
}

function deleteChildsElement(nombre){
  var element = document.getElementById(nombre);
  while (element.hasChildNodes()) {
      element.removeChild(element.lastChild);
  }
}

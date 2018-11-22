const IP2 = "http://172.20.10.2:5000";
const EVENTS_ENDPOINT2 = "/api/v1/events/search_events";
var id=getParameterByName('event_id');
var usern;
var url_users = "http://localhost:5000/api/v1/users/search_users"

$( document ).ready(event_info()// {

);

function event_info(){
    
  var usr = getParameterByName('usr');
        usern = usr;
  
  var settings = {
    "async": true,
    "crossDomain": true,
    "url": IP2 + EVENTS_ENDPOINT2,
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "cache-control": "no-cache"

    },
    "processData": false,
    "data": "{\"type\": \"SEARCH_ID\"\n,\n\t\"event_id\": \""+id+"\"\n}"
  }

  

 $.ajax(settings).done(function (response) {
      console.log(response);
        $("#name").text(response['events']['name']);
        var img2="./img/gallery/"+response['events']['image'];
        $("#img1").text(img2);
        $("#img1").prop("src",img2);
        $("#date").text(response['events']['event_date']);
        $("#location").text(response['events']['event_location']);
        $("#description").text(response['events']['description']);
        $("#info").text(response['events']['ext_info']);
        $("#max_reg").text(response['events']['max_participants']);
        $("#status").text(response['events']['status']);
        $("#num_registered").text(response['events']['num_registered']);

        $('#addEvent').text("REGISTER");
        $('#addEvent').show();
        if(usr == "visit_0123" || $('#status').text() == "INACTIVE"){
          $('#addEvent').hide();
        }
        else if(response['events']['num_registered'] == response['events']['max_participants'] ){

        }
        check_reg();
        
      //window.location.replace("./event.html?name="+name+"&image="+image+"&date="+date+"&location="+location+"&description="+description+"&info="+info+"&category="+category+"&status="+status+"&num_registered="+num_registered+"\n");
  });
}

function check_reg(){
  var data_check={
    "type":"CHECK_IF_REGISTERED",
    "event_id":id,
    "username": usern
  }

  var settings_check = {
    "async": true,
    "crossDomain": true,
    "url": url_users,
    "method": "POST",
    "headers": {
      "Content-Type": "application/json",
      "cache-control": "no-cache"

    },
    "processData": false,
    "data": JSON.stringify(data_check)
  }
  

  $.ajax(settings_check).done(function (response_check) {
    console.log(response_check);
    if(response_check['users'] == "REGISTERED"){
      $('#addEvent').text("REGISTERED");
    }
  });
}

function register_event(){
  if ($("#addEvent").text()== "REGISTER"){
        var data_to_send ={
          "type":"ADD_EVENT",
          "username":usern,
          "event_id": id
        }

        var settings = {
          "async": true,
          "crossDomain": true,
          "url": url_users,
          "method": "POST",
          "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"

          },
          "processData": false,
          "data": JSON.stringify(data_to_send)
        }

      $.ajax(settings).done(function (response) {
        console.log(">>>>>")
            console.log(response['users']);
            if(response['users']== "EVENT_ADDED"){
              alert("Event Added");
              window.location.replace("./userinterface.html?userload="+usern);
            }
            else{
              alert("An error occured, please try again!");
            }
            //window.location.replace("./event.html?name="+name+"&image="+image+"&date="+date+"&location="+location+"&description="+description+"&info="+info+"&category="+category+"&status="+status+"&num_registered="+num_registered+"\n");
        });
      }
      else{}
}

function getParameterByName(id, url) {
  if (!url) url = window.location.href;
  id= id.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + id + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

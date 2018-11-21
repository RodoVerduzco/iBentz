const IP2 = "http://172.20.10.2:5000";
const EVENTS_ENDPOINT2 = "/api/v1/events/search_events";


$( document ).ready(event_info()// {

);

$( window ).on( "load", event_info()

);

function event_info(){
//  var id=id_evento;
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
    "data": "{\"type\": \"SEARCH_ID\"\n,\n\t\"event_id\": \"5bf03ffd43172e1f783de20b\"\n}"
  }

 $.ajax(settings).done(function (response) {
      console.log(response);
      //for (var i = 0; i < response.length; i++) {
        //alert(response['events']['name']);
        $("#name").text(response['events']['name']);
        var img2="./img/gallery/"+response['events']['image'];
        console.log(img2);
        $("#img1").text(img2);
        $("#img1").prop("src",img2);
        $("#date").text(response['events']['event_date']);
        $("#location").text(response['events']['event_location']);
        $("#description").text(response['events']['description']);
        $("#info").text(response['events']['ext_info']);
        //$("#category").text(response['events']['category']);
        $("#status").text(response['events']['status']);
        $("#num_registered").text(response['events']['num_registered']);
          //var name = response[i].name;
          //var image = response[i].image;
          //var date = response[i].date;
          //var location = response[i].location;
          //var description = response[i].description;
          //var info = response[i].info;
          //var category = response[i].category;
          //var status = response[i].status;
          //var num_registered = response[i].num_registered;
        //}
      //window.location.replace("./event.html?name="+name+"&image="+image+"&date="+date+"&location="+location+"&description="+description+"&info="+info+"&category="+category+"&status="+status+"&num_registered="+num_registered+"\n");
  });
}

function llamada(){
  //alert("1413");
  var urlstring = window.location.href;
  var url = new URL(urlstring);
  var usr = localStorage.getItem("userload");
  //alert(usr);
  var username = usr;
  if(!usr || usr == "none")
      username="visit_0123";
  var queryString = "?event_id=" + id + "&user=" + username;
   window.location.href = "../FrontEnd/event.html"+queryString;
}


function filter(){
  var url = IP+EVENTS_ENDPOINT;
  jQuery(document).ready(function($) {
    var location = $('#loc').val();
    var categoria = $('#cat').val();
    if(location===null||location==0){
      location = 0;

    }
    if(categoria===null||categoria==0){
      categoria = 0;
    }
  //  alert(location); alert(categoria);
    if(location !==0 && categoria !==0){
      //filtrado por location y categoria
      var data_to_send = {
          "type" : "READ",
          "event_location" : location,
          "event_type": categoria
        };
    }
    else{
      if(location!==0){
        //filtrado por location
        var data_to_send = {
          "type" : "READ",
          "event_location" : location
        };
      }
      if(categoria!==0){
        //filtrado por categoría
        var data_to_send = {
          "type" : "READ",
          "event_type" : categoria
        };

      }
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
    };



    var empieza = "<div class=\"col-lg-3 col-md-6\" align=\"center\"><div class=\"speaker\"><a href='./event.html?event_id=";
     var empieza0 ="';\"><img style=\"width: 50%; height: 50%\" src='img/gallery/";
      var empieza1 = "' class=\"img-fluid\" title=\"";
      var title = "\"></a><div class=\"details\"><h3>";
      var empieza2 = "</h3><p><b>Lugar:</b> ";
      var empieza3 = "</br><b>Fecha: </b>";
      var empieza4 = "</p></div></div></div>"

  $.ajax(settings).done(function (response) {
      console.log(response);
        $('#resultados').empty();
        $.each(response.events, function(idx, value){
          $("#resultados").append(empieza+response['events'][idx]['id']+empieza0+response['events'][idx]['image'] +empieza1+"Name: " + response['events'][idx]['name'] + "\nPlace: " + response['events'][idx]['event_location'] + "\nDate: " + response['events'][idx]['event_date']+title+ response['events'][idx]['name']+empieza2 +response['events'][idx]['event_location']+
            empieza3+response['events'][idx]['event_date']+empieza4);
          alert($("#resultados").html());
        });

    });

  });
}




function search(){
var url = IP+EVENTS_ENDPOINT;
jQuery(document).ready(function($) {
      var bus = $("#search").val();
    if(bus !== null && bus !== ''){
       var data_to_send = {
        "type" : "READ",
        "name" : bus
      };
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
    };

    }
    else{
      var data_to_send = {
        "type" : "READ"
      };
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
    };
  }
     var empieza = "<div class=\"col-lg-3 col-md-6\" align=\"center\"><div class=\"speaker\"><a href='./event.html?event_id=";
     var empieza0 ="'><img style=\"width: 50%; height: 50%\" src='img/gallery/";
      var empieza1 = "' class=\"img-fluid\" title=\"";
      var title = "\"></a><div class=\"details\"><h3>";
      var empieza2 = "</h3><p><b>Lugar:</b> ";
      var empieza3 = "</br><b>Fecha: </b>";
      var empieza4 = "</p></div></div></div>";

  $.ajax(settings).done(function (response) {
      console.log(response);
        $('#resultados').empty();
        $.each(response.events, function(idx, value){
        //alert();
          $("#resultados").append(empieza+response['events'][idx]['id']+empieza0+response['events'][idx]['image'] +empieza1 +"Name: " + response['events'][idx]['name'] + "\nPlace: " + response['events'][idx]['event_location'] + "\nDate: " + response['events'][idx]['event_date']+title+ (response['events'][idx]['name']).substring(0, 14)+"..."+empieza2 +response['events'][idx]['event_location']+
            empieza3+response['events'][idx]['event_date']+empieza4);

        });

    });

  });
}

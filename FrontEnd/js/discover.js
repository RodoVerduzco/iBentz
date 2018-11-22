function llamada(id){
 
  var user="user";
  var queryString = "?id=" + id + "&user=" + user;
   window.location.href = "../FrontEnd/dummy.html"+queryString;
}


function filter(){
  var url = "http://172.20.10.2:5000/api/v1/events/search_events";
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
          }
    }
    else{
      if(location!==0){
        //filtrado por location
        var data_to_send = {
          "type" : "READ",
          "event_location" : location
          }
      }
      if(categoria!==0){
        //filtrado por categoría
        var data_to_send = {
          "type" : "READ",
          "event_type" : categoria
          }

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
    }



     var empieza = "<div class=\"col-lg-4 col-md-6\" style=\"padding:30px\"><div class=\"speaker\"><img src='img/gallery/7";
      var empieza1 = ".jpg' class=\"img-fluid\"><div class=\"details\"><h3>";
      var empieza2 = "</h3><p><b>Lugar:</b> ";
      var empieza3 = "</br><b>Fecha: </b>" 
      var empieza4 = "</p></div></div></div>"

  $.ajax(settings).done(function (response) {
      console.log(response);
      $('#resultados').empty();
        $.each(response.events, function(idx, value){      
          $("#resultados").append(empieza + empieza1 + 
            response['events'][idx]['name']+empieza2 +response['events'][idx]['event_location']+ 
            empieza3+response['events'][idx]['event_date']+empieza4);

        });

    }); 

  });
}




function search(){
var url = "http://172.20.10.2:5000/api/v1/events/search_events";
jQuery(document).ready(function($) {
      var bus = $("#search").val();
    if(bus !== null && bus !== ''){
       var data_to_send = {
        "type" : "READ",
        "name" : bus
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
      
    }
    else{
      var data_to_send = {
        "type" : "READ"
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
  }
     var empieza = "<div class=\"col-lg-4 col-md-6\" style=\"padding:30px\"><div class=\"speaker\"><a href=\"javascript:llamada('";
     var empieza0 ="');\"><img src='img/gallery/7";
      var empieza1 = ".jpg' class=\"img-fluid\"></a><div class=\"details\"><h3>";
      var empieza2 = "</h3><p><b>Lugar:</b> ";
      var empieza3 = "</br><b>Fecha: </b>" 
      var empieza4 = "</p></div></div></div>"

  $.ajax(settings).done(function (response) {
      console.log(response);
        $('#resultados').empty();
        $.each(response.events, function(idx, value){      
          $("#resultados").append(empieza +response['events'][idx]['id']+empieza0+empieza1 + response['events'][idx]['name']+empieza2 +response['events'][idx]['event_location']+ 
            empieza3+response['events'][idx]['event_date']+empieza4);

        });

    });  

  });
}


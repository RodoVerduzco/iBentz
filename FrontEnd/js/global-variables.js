const IP = "http://localhost:5000";
//const IP = "http://localhost:5000";
const USERS_ENDPOINT = "/api/v1/users/search_users";
const EVENTS_ENDPOINT = "/api/v1/events/search_events";

function check_logged() {
  console.log(" aaa")
    if(localStorage.getItem("logged") == "true") {
      var type = localStorage.getItem("type");
      $("#signup-btn").remove();
      $("#login-btn").remove();

        if(type == "user") {
          $("#nav-menu").append("<li id='profile-btn' class='buy-tickets'><a href='userinterface.html'>Profile</a></li>");
          $("#nav-menu").append("<li id='logout-btn' class='buy-tickets'><a href='index.html'>Log Out</a></li>");
          $("#logout-btn").on('click', function() {
            logout();
          });
        }
        else if (type == "org") {
          $("#nav-menu").append("<li id='profile-btn' class='buy-tickets'><a href='orginterface.html'>Profile</a></li>");
          $("#nav-menu").append("<li id='logout-btn' class='buy-tickets'><a href='index.html'>Log Out</a></li>");
          $("#logout-btn").on('click', function() {
            logout();
          });
        }
        else if (type == "admin") {
          $("#nav-menu").append("<li id='profile-btn' class='buy-tickets'><a href='admin-menu.html'>Profile</a></li>");
          $("#nav-menu").append("<li id='logout-btn' class='buy-tickets'><a href='index.html'>Log Out</a></li>");
          $("#logout-btn").on('click', function() {
            logout();
          });
        }
    }
}

function logout(){
  localStorage.setItem("logged", "false");
  localStorage.setItem("type", "none");
  localStorage.setItem("userload", "none");
}

check_logged();

function getCookie(name) {
  var cookieValue = null;
  var i = 0;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (i; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie("csrftoken");

$(document).ready(function () {
  $.ajaxSetup({
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
  });
});

console.log("hello");
$(document).on("submit", "#loginForm", function (e) {
  e.preventDefault();
  var action = $(this).attr("action");
  var login_data = $(this).serialize();

  $.ajax({
    method: "POST",
    url: action,
    data: login_data,
  })

    .done(function (response) {
      window.location.href = "";
    })
    .fail(function (response) {
      var error_template = "<br><ul><li> This Field is required </li></ul>";
      $(".error-login").html(error_template);
    });
  console.log("hello!");
});
// var url = "http://127.0.0.1:8000/";
// $("#slogin").click(function () {
//   $.ajax({
//     method: "POST",
//     url: "http://127.0.0.1:8000/account/login2/",
//     data: {
//       csrf_token: $("input[name=_token]").val(),
//       email: $("input[name=email]").val(),
//       password: $("input[name=password]").val(),
//     },
//     success: function (data) {
//       console.log("hello");
//       window.location = url;
//     },
//     error: function (data) {
//       console.log(data);
//     },
//   });
// });

var url = "http://127.0.0.1:8000/";
$("#logout").submit(function (event) {
  event.preventDefault();

  window.location.href = url;
});
$("#logout").click(function () {
  $.ajax({
    method: "POST",
    url: "http://127.0.0.1:8000/account/logout/",
    data: {
      csrf_token: $("input[name=_token]").val(),
    },
    success: function (data) {
      console.log("hello");
      window.location = url;
    },
    error: function (data) {
      console.log(data);
    },
  });
});

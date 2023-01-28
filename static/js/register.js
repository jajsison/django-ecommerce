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

$(function () {
  $.ajaxSetup({
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
  });
});

$("#register").click(function () {
  $.ajax({
    method: "POST",
    url: "http://127.0.0.1:8000/account/register/",
    data: {
      csrf_token: $("input[name=_token]").val(),
      email: $("input[name=email]").val(),
      first_name: $("input[name=first_name]").val(),
      last_name: $("input[name=last_name]").val(),

      password: $("select[name=password]").val(),
    },
    success: function (data) {
      location.reload();
    },
  });
});

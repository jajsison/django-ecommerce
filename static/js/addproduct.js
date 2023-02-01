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

  $(document).on("submit", "#add_product_form", function (e) {
    console.log("hello");

    e.preventDefault();
    var action = $(this).attr("action");
    var product_data = $(this).serialize();
    console.log($(this).serialize());

    $.ajax({
      method: "POST",
      url: action,
      data: product_data,
    })
      .done(function (response) {
        window.location.href = "";
      })

      .fail(function (response) {
        var error_template = "<br><ul><li> This Field is required </li></ul>";
        $(".error-add-product").html(error_template);
        console.log($(this).serialize());
      });
  });
});

// $("#product_submit").submit(function () {
//   $.ajax({
//     method: "POST",
//     url: "http://127.0.0.1:8000/account/api-product/",
//     data: {
//       csrf_token: $("input[name=_token]").val(),
//       email: $("input[name=email]").val(),
//       password: $("input[name=password]").val(),
//       password2: $("input[name=password2]").val(),
//     },
//     success: function (data) {
//       console.log("hello");
//       location.reload();
//     },
//     error: function (data) {
//       console.log(data);
//     },
//   });
// });

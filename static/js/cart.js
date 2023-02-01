$(document).ready(function () {
  $(document).on("click", "#addToCartBtn", function () {
    var _vm = $(this);
    var _qty = $(".product-qty-" + _index).val();
    var _productId = $(".product-id-" + _index).val();
    var _productImage = $(".product-image-" + _index).val();
    var _productTitle = $(".product-title-" + _index).val();
    var _productPrice = $(".product-price-" + _index).text();

    var url = "http://127.0.0.1:8000/add-to-cart/";

    //Ajax
    $.ajax({
      url: url,
      data: {
        id: _productId,
        image: _productImage,
        qty: _qty,
        title: _productTitle,
        price: _productPrice,
      },
      dataType: "json",
      beforeSend: function () {
        _vm.attr("disabled", true);
      },
      success: function (res) {
        $(".cart-list").text(res.totalitems);
        _vm.attr("disabled", false);
      },
    });
  });
});

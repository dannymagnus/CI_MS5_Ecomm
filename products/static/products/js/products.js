function disableOption(){
    $(".size-option").each(function(){
        console.log($(this).val());
        // Test if the div element is empty
        if($(this).attr("data-count") == 0){
            $(this).attr("disabled", "disabled");
            $(this).text($(this).attr("value")+" (Out of Stock)");
        }else{
            $(this).removeAttr('disabled');
            $(this).text($(this).attr("value"));
        }
    });
}

function populateAvailableQty(){
    ($('.qty-input').val(1));
    // ($('.qty-input').attr("max", $('option:selected').attr('data-count')));
    sessionQtyRaw = parseInt($('option:selected').attr('session-quantity'));
    console.log(sessionQtyRaw);
    if (Number.isNaN(sessionQtyRaw)){
        ($('.qty-input').attr("max", parseInt($('option:selected').attr('data-count'))));
    } else{
        ($('.qty-input').attr("max", parseInt($('option:selected').attr('data-count')) - parseInt($('option:selected').attr('session-quantity'))));
    }
}

function populateSku(){
    ($('#sku').val($('option:selected').attr('data-sku')));
}

$('.quantity-right-plus').click(function (e) {
    // Stop acting like a button
    e.preventDefault();
    console.log(this);
    // Get the field name
    var parent = $(this).closest('.input-group-append');
    console.log(parent);
    var quantityInput = parent.siblings('.input-number');
    console.log(quantityInput);
    var quantity = parseInt(quantityInput.val());

//         // If is not undefined
if (quantity < quantityInput.attr('max')) {
    quantityInput.val(quantity + 1);
}
//         // Increment


//         // $(this).siblings('.input-number').val();
});

$('.quantity-left-minus').click(function (e) {
    // Stop acting like a button
    e.preventDefault();
    console.log(this);
    // Get the field name
    var parent = $(this).closest('.input-group-prepend');
    console.log(parent);
    var quantityInput = parent.siblings('.input-number');
    console.log(quantityInput);
    var quantity = parseInt(quantityInput.val());

//         // If is not undefined

    // Increment
    if (quantity > 1) {
        quantityInput.val(quantity - 1);
    }
});


window.onload = function() {
    disableOption();
    populateAvailableQty();
    populateSku();
  };


$('select').on('change', function () {
    console.log('tried to run your function');
    disableOption();
    populateAvailableQty();
    populateSku();
});

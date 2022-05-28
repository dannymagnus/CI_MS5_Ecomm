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
    ($('.qty-input').attr("max", $('option:selected').attr('data-count')));
}

function populateSku(){
    ($('#sku').val($('option:selected').attr('data-sku')));
}

$('#decrement-qty').on('click', function (e){
    e.preventDefault();
    $('#id_qty').val( function(i, oldval) {
        return parseInt( oldval, 10) - 1;
    });
});

$('#increment-qty').on('click', function (e){
    e.preventDefault();
    $('#id_qty').val( function(i, oldval) {
        return parseInt( oldval, 10) + 1;
    });
});

$('.qty-input').on('change', function(){
    console.log($(this).val());
    if ($(this).val() >= $(this).attr("max")){
        $('#increment-qty').attr("disabled", "disabled");
    } else if ($(this).val() <= $(this).attr("min")){
        $('#decrement-qty').attr("disabled", "disabled");
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


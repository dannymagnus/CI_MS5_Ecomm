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
    ($('.qty-input').val("1"));
    ($('.qty-input').attr("max", $('option:selected').attr('data-count')));
}


window.onload = function() {
    disableOption();
    populateAvailableQty();
  };


$('select').on('change', function () {
    console.log('tried to run your function');
    disableOption();
    populateAvailableQty();
});
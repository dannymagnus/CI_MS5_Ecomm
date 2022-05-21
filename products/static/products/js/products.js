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


window.onload = function() {
    disableOption();
  };


$('select').on('change', function () {
    disableOption();
});
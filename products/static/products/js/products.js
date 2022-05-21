function disableOption(){
    $(".size-option").each(function(){
        console.log($(this).val());
        // Test if the div element is empty
        if($(this).attr("value") == 0){
            $(this).attr("disabled", "disabled");
            $(this).text($(this).attr("data-size")+" (Out of Stock)");
        }else{
            $(this).removeAttr('disabled');
            $(this).text($(this).attr("data-size"));
        }
    });
}


window.onload = function() {
    disableOption();
  };


$('select').on('change', function () {
    disableOption();
});
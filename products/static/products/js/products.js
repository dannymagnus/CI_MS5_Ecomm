function disableOption(){
    let options = Array.from(document.querySelectorAll('.size-options'));
    options.forEach(function(option){
        console.log(option);
        let qty = option.getAttribute('value');
        console.log(qty);
        if (qty == 0) {
            console.log("value is 0!!");
            option.setAttribute('disabled', '');
        }else{
            option.removeAttribute('disabled');
        }
    });
}
//     for (let option in options){
//         if (option.getAttribute('value') === 0) {
//             option.setAttribute('disabled',);
//         }else{
//             option.removeAttribute('disabled');
//         }
//     }
// }

window.onload = function() {
    disableOption();
  };

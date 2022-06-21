/*
 * Function to increase qty in bag and disable once max value reached
*/
    $('.quantity-right-plus').click(function (e) {
        e.preventDefault();
        var qtyform = $(this).closest('form');
        var parent = $(this).closest('.input-group-append');
        console.log(parent);
        var quantityInput = parent.siblings('.input-number');
        console.log(quantityInput);
        var quantity = parseInt(quantityInput.val());
        if (quantity < quantityInput.attr('data-inventory-count')) {
            quantityInput.val(quantity + 1);
        }
        qtyform.submit();
    });

/*
 * Function to decrease qty in bag and disable once max value reached
*/
$('.quantity-left-minus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        var qtyform = $(this).closest('form');
        // Get the field name
        var parent = $(this).closest('.input-group-prepend');
        console.log(parent);
        var quantityInput = parent.siblings('.input-number');
        console.log(quantityInput);
        var quantity = parseInt(quantityInput.val());
        if (quantity > 0) {
            quantityInput.val(quantity - 1);
        }
        qtyform.submit();
    });


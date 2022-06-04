
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
        if (quantity < quantityInput.attr('data-inventory-count')) {
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
        if (quantity > 0) {
            quantityInput.val(quantity - 1);
        }
    });


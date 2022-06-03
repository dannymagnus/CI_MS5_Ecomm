
    $('.quantity-right-plus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        console.log(this);
        // Get the field name
        var parent = $(this).closest('.input-group-btn');
        console.log(parent);
        var quantityInput = parent.siblings('.input-number');
        console.log(quantityInput);
        var quantity = parseInt(quantityInput.val());

//         // If is not undefined

        quantityInput.val(quantity + 1);


//         // Increment


//         // $(this).siblings('.input-number').val();
    });


$('.quantity-left-minus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        console.log(this);
        // Get the field name
        var parent = $(this).closest('.input-group-btn');
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


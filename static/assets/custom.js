$(document).ready(function(){
    $('.increment-btn').click(function(e){
        e.preventDefault();
        // alert("hi");

        var incvalue = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(incvalue,10);
        value = isNaN(value) ? 0 : value;
        if(value < 10)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }

    });
    $('.decrement-btn').click(function(e){
        e.preventDefault();
        // alert("hi");

        var decvalue = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(decvalue,10);
        value = isNaN(value) ? 0 : value;
        if(value > 1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    }); 
    $('.addToCartBtn').click(function(){
        var prod_id = $(this).closest('.product_data').find('.prod_id').val();
        var prod_quantity = $(this).closest('.product_data').find('.qty-input').val();
        var token= $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/addtocart",
            data:{
                'prod_id': prod_id,
                'prod_quantity': prod_quantity,
               'csrfmiddlewaretoken': token,
            },
            success: function (response) {
                console.log(response)  
                alertify.success(response.status)
            }
        });


    });  
});



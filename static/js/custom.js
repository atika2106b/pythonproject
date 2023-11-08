$(document).ready(function(){

    $('.increment-btn').click(function(e){
        e.preventDefault();
        // var inc_value = $(this).closest('.product_data').val();
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value,10);
        // console.log(value);


        value = isNaN(value) ? 0 : value;


        if(value < 10){
            value++;
            // console.log(value);
            $(this).closest('.product_data').find('.qty-input').val(value);
        }


    });

    $('.decrement-btn').click(function(e){
        e.preventDefault();
        // var inc_value = $(this).closest('.product_data').val();
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        // console.log(value);


        value = isNaN(value) ? 0 : value;


        if(value > 1){
            value--;
            // console.log(value);
            $(this).closest('.product_data').find('.qty-input').val(value);
        }


    });


    $('.addToCartBtn').click(function(){
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty_input').val();
        var token = $('.input[name=csrfmiddlewaretoken').val();
        $.ajax({
            type: "POST",
            url:"/add-to-cart",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token
            },
            success: function(reponse){
                alertify.success(response.status);
            }
        });

    });


});
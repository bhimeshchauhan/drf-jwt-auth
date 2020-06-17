var currentDocument = document.currentScript.ownerDocument;
currentDocument.querySelector('.img__btn').addEventListener('click', function() {
  currentDocument.querySelector('.cont').classList.toggle('s--signup');
});

$('#signup').submit(function(e){
    e.preventDefault();
    url = $(this).attr('action');
    data = $(this).serialize();

    $.ajax({
        url : url, // the endpoint
        type : "POST", // http method
        data : data, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr, errmsg, err)
            $('.error-msg').html('');
            for (const [key, value] of Object.entries(error.message)) {
                $('.error-msg').append('<i class="fa fa-times-circle"></i> '+value[0]);
                $('.error-msg').fadeIn('slow');
            }
            $('.error-msg').delay(5000).fadeOut('slow');
        }
    });
});
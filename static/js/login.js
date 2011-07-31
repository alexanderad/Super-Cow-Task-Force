jQuery(document).ready(function ($) {


// hide the form

    $('.login-form').hide();

// menu link events

    $('.login').click(function () {
        $('.shadow').show().css({
            'position': 'fixed',
            'height': '100%',
            'width': '100%',
            'z-index': '900',
            'opacity': '0.8'
        });

        $('.login-tab').addClass('active');
        $('.reg-tab').removeClass('active');
        $('.reg-f').css('display', 'none');
        $('.login-f').css('display', 'block');

        $('.login-form').show().animate({
            opacity: 1
        }, 300);

    });


    $('.register').click(function () {
        $('.shadow').show().css({
            'position': 'fixed',
            'height': '100%',
            'width': '100%',
            'z-index': '900',
            'opacity': '0.8'
        });


        $('.reg-tab').addClass('active');
        $('.login-tab').removeClass('active');
        $('.login-f').css('display', 'none');
        $('.reg-f').css('display', 'block');

        $('.login-form').show().animate({
            opacity: 1
        }, 300);

    });

// close form overlay

    $('.close').click(function () {
        $('.login-form, .shadow').animate({
            opacity: 0
        }, 300, function () {
            $('.shadow').css({
                'position': 'fixed',
                'height': '0',
                'width': '0',
                'z-index': '-100',
                'opacity': '0'
            });
            $(this).hide();
        });
    });

// overlay tabs behaviour

    $('.login-tab').click(function () {

        $(this).addClass('active');
        $('.reg-tab').removeClass('active');
        $('.reg-f').css('display', 'none');
        $('.login-f').css('display', 'block');

    });


    $('.reg-tab').click(function () {

        $(this).addClass('active');
        $('.login-tab').removeClass('active');
        $('.reg-f').css('display', 'block');
        $('.login-f').css('display', 'none');

    });
    
    $("#id_login_button").click(function() {        
        var request_data = {email: $("#id_login_email").val(),
                    password: $("#id_login_password").val(), 
                    csrfmiddlewaretoken: getCookie('csrftoken'),
        };
        $.post('/accounts/json/login', request_data, function(response_data) {                           
            switch(response_data.error) {
                case 1:
                    // validation errors
                    for(v in response_data.form_errors) {
                        $("#id_login_" + v).before('<ul class="errorlist"><li>' + response_data.form_errors[v] + '</li></ul>');
                    };
                    setTimeout(function() { $(".errorlist").fadeOut() }, 3500);
                    break;
                    
                case 403:
                    // wrong username and or password
                    $("#id_login_email").before('<ul class="errorlist"><li>' + response_data.non_field_error + '</li></ul>');
                    break;
                    
                case 0:
                    $('.close').click();
                    $(location).attr('href', '/');
                    break;
            };
        });        
    });
});
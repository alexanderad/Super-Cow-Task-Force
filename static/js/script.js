jQuery(document).ready(function($) {
	
	 //$("#id_login-f, #id_reg-f").validationEngine({promptPosition : "centerRight", scroll: false});
	
	
   $('.login-form').hide();
   

 $('.login').click(function() {
  $('.shadow').show().css({
    'position': 'fixed',
	'height':'100%',
	'width':'100%',
	'z-index': '900',
	'opacity': '0.8'
  });	
  
   $('.login-tab').addClass('active');
	  $('.reg-tab').removeClass('active'); 
	    $('.reg-f').css('display','none');
		   $('.login-f').css('display','block');
		    
  $('.login-form').show().animate({
    opacity: 1
  }, 300);
  
  
  
  
  
});


 $('.register').click(function() {
  $('.shadow').show().css({
    'position': 'fixed',
	'height':'100%',
	'width':'100%',
	'z-index': '900',
	'opacity': '0.8'
  });	 
  
  
		  $('.reg-tab').addClass('active');
		  $('.login-tab').removeClass('active');
		    $('.login-f').css('display','none');
		  $('.reg-f').css('display','block');
		  
  $('.login-form').show().animate({
    opacity: 1
  }, 300);
 
   });
   
   
  $('.close').click(function() {
	   $('.login-form, .shadow').animate({
    opacity: 0
  }, 300, function() { 
   $('.shadow').css({
    'position': 'fixed',
	'height':'0',
	'width':'0',
	'z-index': '-100',
	'opacity': '0'
  });	 
  $(this).hide();
  });  
  });
  
  
  $('.login-tab').click(function(){
	  
   $(this).addClass('active');
	  $('.reg-tab').removeClass('active'); 
	    $('.reg-f').css('display','none');
		   $('.login-f').css('display','block');  
	  
  });
  
  
    $('.reg-tab').click(function(){
	  
   $(this).addClass('active');
	  $('.login-tab').removeClass('active'); 
	    $('.reg-f').css('display','block');
		$('.login-f').css('display','none');  
	  
  });
 
});
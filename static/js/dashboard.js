jQuery(document).ready(function ($) {

//tooltips

$('.statusbar div[checkdate]').qtip({
content: { text: function(api) {
         return $(this).attr('checkdate');
            }
			},
position: {
	   target: 'mouse',
	   my: 'bottom center', 
       at: 'top center', 
	   adjust: {  
	    y: -5	  
	 }
  	 }

   });

//link row load   
   
$('.task-container .link-text').click(function(){
  if (!$('.task-container .link-text').hasClass('clicked')) {
  $(this).parents('tr').after('<tr class="status-explained"><td colspan="4"><div class="link-details" id="id_link-details"></div></td></tr>');
  $('#id_link-details').load('link_content.html');
  $(this).addClass('clicked');
  } else {
  $(this).removeClass('clicked');
  $(this).parents('tr').next('tr.status-explained').remove();
	  };
	  
	  
	  
	  
/*  $.ajax({
  url: 'link_content.html',
  dataType: "html",
  success: function (res) {
	  
     $(".link-details").html($(res).find("#content-to-load")).fadeIn('slow');

    } 
	
	});*/
	
});
  
});
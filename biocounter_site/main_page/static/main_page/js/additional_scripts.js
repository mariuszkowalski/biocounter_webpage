$(document).ready(
    function()
    	{
		if($("#comment_success").length != 0)
			{
        	window.setTimeout(
        	function()
        		{
            	$("#comment_success").fadeOut(3000);
            	}, 3000);
			}
        });
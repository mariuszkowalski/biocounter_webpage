$(document).ready(
	function()
		{
		var cookie_banner = document.getElementById("cookie_banner");
		var cookie_law_exists = checkCookie("cookie_law");
		var cookie_law_value = getCookie("cookie_law")

		if(cookie_law_exists == false || cookie_law_value == false)
			{
			cookie_banner.style.display = 'block';
			}
		else
			{
			cookie_banner.style.display = 'none';
			}
		});

function setCookie(cookie_name, cookie_value, expiration_interval)
	{
	var date = new Date()
	date.setTime(date.getTime() + (expiration_interval*24*60*60*1000));
	var expires = "expires=" + date.toUTCString();
	document.cookie = cookie_name + "=" + cookie_value + ";" + expires + ";path=/";
	}

function getCookie(cookie_name)
	{
	var name = cookie_name + "=";
	var decodedCookie = decodeURIComponent(document.cookie);
	var ca = decodedCookie.split(';');
	for(var i = 0; i < ca.length; i++)
		{
		var c = ca[i];
		while (c.charAt(0) == ' ')
			{
			c = c.substring(1);
			}
		if (c.indexOf(name) == 0)
			{
			return c.substring(name.length, c.length);
			}
		}
	return "";
	}

function checkCookie(cookie_name)
	{
	var cookie_value = getCookie(cookie_name);
	if (cookie_value == "")
		{
		return false;
		}
	else if(cookie_value == "true")
		{
		return true;
		}
	else
		{
		return "Something went wrong.";
		}
	}

function toggleVisibility(element_id)
	{	
	var current_element = document.getElementById(element_id);
	setCookie("cookie_law", true, 365);
	if(current_element.style.display != 'none')
		{
		current_element.style.display = 'none';
		}
	}
function validateForm()
{

	var fname=document.forms["register_form"]["fname"].value;
	if (fname==null || fname==""){
		alert("Please enter your first name");
		return false;
	}
	
	var lname=document.forms["register_form"]["lname"].value;
	if (lname==null || lname==""){
		alert("Please enter your last name");
		return false;
	}

	var email=document.forms["register_form"]["email"].value;
	var atpos=email.indexOf("@");
	var dotpos=email.lastIndexOf(".");
	if (atpos<1 || dotpos<atpos+2 || dotpos+2>=email.length){
	  alert("Please enter a valid email address");
	  return false;
	}
	
	var password=document.forms["register_form"]["password"].value;
	if (password.length < 6){
		alert("Password must be at least 6 characters long");
		return false;
	}
}

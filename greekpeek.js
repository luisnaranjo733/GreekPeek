// javascript file linked to greekpeek.html

var first = document.getElementById("first");
var last = document.getElementById("last");
var email = document.getElementById("email");
var number = document.getElementById("password2");
var password1 = document.getElementById("password1");
var password2 = document.getElementById("password2");

window.onload = function() {
}

function validate() {
	if (password1.value != password2.value) {
		alert("Passwords don't match.");
	}
}
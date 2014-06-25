"use strict";

var datag;
window.onload = function() {
	//var ajax = new XMLHttpRequest();
	//ajax.onload = buildList;
	//ajax.open("GET", "http://10.88.77.65/json/Phi%20Delta%20Theta/", true);
	//ajax.send();
	$.get("http://10.88.77.65/json/Phi%20Delta%20Theta/", function(data, status) {
		console.log(data);
		datag = data;
		for (var i = 0; i < data.length; i++) {
			var name = data[i].firstName;
		
			$('<label><input id="name + '+i+'" type="radio" name="name" onclick="changeData('+i+');" "value="name'+i+'">'+name+'</label><br />').appendTo("#subs");
		}
	}).fail(function(err) {
		console.log("get failed");
	});
};

function buildList() {
	data = this.responseText;
	for (var i = 0; i < data.length; i++) {
		$("#name" + i).text(data[i]["name"]);
	};
}

function changeData(event) {
	var allButtons = $("input");
	var name;
	for (var i = 0; i < allButtons.length; i++) {
		if(allButtons[i].checked) {
			name = $("inp").value;
		}
	}
	$("#name").text(name);
	var id = event;
	$("#year").text(datag[id]["grade"]);
	$("#phone").text(datag[id]["phone"]);
	$("#email").text(datag[id]["email"]);
	$("#major").text(datag[id]["major"]);	
}

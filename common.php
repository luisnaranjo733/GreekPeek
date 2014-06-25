<?php 
	// common HTML code used across all pages placed here

	function head() {
?>
<!DOCTYPE html> 
<html lang="en"> 
	<head>
        <meta charset='utf-8' />
        <meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1' />
        <meta name=viewport content='width=device-width, initial-scale=1'>
		<title>Greek Peek</title>
        <link rel='stylesheet' href='style.css' type='text/css' media='all' />
<?php
    }

    function banner() {
?>
	</head>

	<body>
		<div id="frame">
			<div id="banner">
                <div class="wrapper">
                    <div id="branding">
                        <div id="logo"></div>
                        <h1 id="title">GreekPeek</h1>
                    </div>
                    <div id="signin-box">
                        <a href="#" class="button2">Sign in</a>
                    </div>
                    <div class="clearfix"></div>
                </div>
            </div>

			<div id="navbar">
                <div class="wrapper">
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Fraternities</a></li>
                        <li><a href="#">Member Sign-Up</a></li>
                        <li><a href="#">Fraternity Sign-Up</a></li>
                    </ul>
                </div>
            </div>
<?php
	}

?>
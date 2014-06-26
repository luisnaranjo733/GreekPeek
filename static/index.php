<!-- Home page for Greek Peek -->
<?php
include 'common.php';
head();
banner();
?>
			<div id="content">
                <div id="cover-slideshow-area" style="background:#fcfcfc;position:relative;">
                    <link rel="stylesheet" href="js/slidejs/slidejs.css">
                    <script src="js/slidejs/jquery.slides.min.js"></script>
                    <div class="slide-container" style="max-width: 1050px;">
                        <div id="cover-slides" style="position:relative;">
                            <img src="images/chocolate run phi delts.jpg" alt="">
                            <img src="images/IMG_0047_small.jpg" alt="">
                        </div>
                    </div>
                    <script>
                        $(function() {
                          $('#cover-slides').slidesjs({
                            width: 650,
                            height: 278,
                            play: {
                              active: true,
                              auto: true,
                              interval: 4000,
                              swap: true
                            }
                          });
                        });
                    </script>
                    <style>
                    .slidesjs-navigation { display: none !important; }
                    .slidesjs-pagination {
                        position: absolute;
                        bottom: 0;
                        z-index: 50;
                        right: 0;
                        margin: 5px;
                    }
                    </style>
                    <div class="cover-slideshow-complement-container">
                        <div class="cover-slideshow-complement">
                            <h2>GreekPeek</h2>
                            <p>"GreekPeek is awesome" - Some guy</p>
                        </div>
                    </div>
                </div>
                <div class="content-bar">
                </div>
                
                <div class="wrapper">
                    <div id="main-content" role="main">
                        
                    </div>
                </div>
            </div>
            
			<div id="footer">
                <div class="wrapper">
                    &copy 2014 Greek Peek <br /> 
                    <a href="contact.html">Contact Us</a>
                </div>
            </div>
		</div>
	</body>

</html>
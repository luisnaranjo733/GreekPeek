      function initialize() {
        var mapOptions = {
          center: { lat: 47.6626582, lng: -122.3070346},
          zoom: 17
        };
        var map = new google.maps.Map(document.getElementById('map-canvas'),
            mapOptions);
            
        var myLatlng = new google.maps.LatLng(47.662836, -122.305180);
        var marker = new google.maps.Marker({
            position: myLatlng,
            map: map,
            title:"Hello World!",
            animation: google.maps.Animation.DROP,
        });
        
        google.maps.event.addListener(marker, 'click', function() {
          $('#myModal').modal('show')
        });
      }
      google.maps.event.addDomListener(window, 'load', initialize);

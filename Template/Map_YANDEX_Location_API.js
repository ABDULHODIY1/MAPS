//<!--        function initMap() {-->
//<!--            var map = new google.maps.Map(document.getElementById('map'), {-->
//<!--                zoom: 12,-->
//<!--                center: {lat: -34.397, lng: 150.644}  // Default center-->
//<!--            });-->
//
//<!--            {% if current_location %}-->
//<!--                var currentMarker = new google.maps.Marker({-->
//<!--                    position: {lat: {{ current_location.latitude }}, lng: {{ current_location.longitude }}},-->
//<!--                    map: map,-->
//<!--                    title: 'Current Location'-->
//<!--                });-->
//<!--                map.setCenter(currentMarker.getPosition());-->
//<!--            {% endif %}-->
//
//<!--            {% if destination %}-->
//<!--                var destinationMarker = new google.maps.Marker({-->
//<!--                    position: {lat: {{ destination.latitude }}, lng: {{ destination.longitude }}},-->
//<!--                    map: map,-->
//<!--                    title: 'Destination'-->
//<!--                });-->
//<!--                map.setCenter(destinationMarker.getPosition());-->
//<!--            {% endif %}-->
//<!--        }-->
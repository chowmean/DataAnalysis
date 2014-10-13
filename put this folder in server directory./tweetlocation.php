<html>
  <head>
    <meta charset="utf-8">
    <title>Analysis of tweets</title>
<div id="selector" style="position:absolute;top:20%;left:2%;width:10%;background:#bbb;box-shadow: 2px 2px 2px 2px #454545;border-radius:10px;padding:10px;">
<?php
foreach(glob('twitter_analysis/*', GLOB_ONLYDIR) as $dir) {
    $dir = str_replace('twitter_analysis/', '', $dir);
    echo '<a href="tweetlocation.php?id='.$dir.'"><button>'.$dir.'</button></a><br>';
}
?> 
</div>


 

    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
	background:#bbb;
      }
	body
	{background:#bbb;
	}	
      #panel {
        position: absolute;
        top: 5px;
        left: 50%;
        margin-left: -180px;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
      }
    </style>

<center>
<div id="head" style="width:100%;box-shadow: 10px 10px 10px 10px #454545; color:#454545;background-color:#bbb;">
<font size="6">Analysis of tweets</font><br>
<font size="4">Mapped according to their Geocodes</font></center><br><br></div>
 </center>   <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>


    <script>
// If you're adding a number of markers, you may want to
// drop them on the map consecutively rather than all at once.
// This example shows how to use setTimeout() to space
// your markers' animation.



 
var neighborhoods = [
  
  <?php


if(isset($_GET["id"]))
{$open=$_GET["id"];}
else
{$open='India';}
$string = file_get_contents("twitter_analysis/".$open."/location.json");
$json_a = json_decode($string, true);

foreach ($json_a as $person_name => $person_a) {
  echo "new google.maps.LatLng(".$person_a['latitude'].", ".$person_a['longitude']."),";
}
?> 
];


var berlin = neighborhoods[0];

var markers = [];
var iterator = 0;

var map;

function initialize() {
  var mapOptions = {
    zoom: 2,
    center:berlin };

  map = new google.maps.Map(document.getElementById('map-canvas'),
          mapOptions);
}

function drop() {
  for (var i = 0; i < neighborhoods.length; i++) {
    setTimeout(function() {
      addMarker();
    }, i * 100);
  }
}

function addMarker() {
  markers.push(new google.maps.Marker({
    position: neighborhoods[iterator],
    map: map,
    draggable: false,
    animation: google.maps.Animation.DROP
  }));
  iterator++;
}

google.maps.event.addDomListener(window, 'load', initialize);
 setTimeout(function() {
      drop();
    }, 500);




    </script>
  </head>
  <body>
   
    <div id="map-canvas" style="position:absolute;top:20%;left:55%; width:40%;height:75%;border:2px solid #454545;box-shadow: 2px 2px 2px 2px #454545;"></div>
 






<script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">


<?php
if(isset($_GET["id"]))
{$open=$_GET["id"];}
else
{$open='India';}
$string = file_get_contents("twitter_analysis/".$open."/Result.json");
$json_a = json_decode($string, true);


//print_r( $json_a); 
 echo 'var v=[["Reaction","Tweet Count"],["Positive",'.$json_a[1]['Positive'].'],["Negative",'.$json_a[2]['Negative'] .'],["Neutral",'.$json_a[3]['Neutral'].']];';

?> 

      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable(v);

        var options = {
          title: <?php echo '"Tweets Sentiment anslysis of '.$open.'"'; ?>,
          is3D: true,
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart_3d" style="width: 30%; height: 70%;border:2px solid #bbb;position:absolute;top:20%;left:20%;border:2px solid #454545;box-shadow: 2px 2px 2px 2px #454545;"></div>
  </body>











<div id="home" style="position:absolute;top:75%;left:2%;height:50px;width:200px;"><a href='index.php'><button style="height:50px;background:black;color:white"> Go back to home </button></a></div>
<div id="home" style="position:absolute;top:85%;left:2%;height:50px;width:200px;"><a href='live/index.php'><button style="height:50px;background:black;color:white"> News Analysis Section </button></a></div>



 </body>
</html>




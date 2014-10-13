

<center>
<div id="head" style="width:100%;box-shadow: 10px 10px 10px 10px #454545; color:#454545;background-color:#bbb;">
<font size="6">Analysis of twitter data and RSS Feeds</font></center><br><br></div>
 </center>


<div id="selector" style="position:absolute;top:20%;left:2%;width:15%;background:#bbb;box-shadow: 2px 2px 2px 2px #454545;border-radius:10px;padding:10px;">
<u>Analysis available</u>
<?php
foreach(glob('twitter_analysis/*', GLOB_ONLYDIR) as $dir) {
    $dir = str_replace('twitter_analysis/', '', $dir);
    echo '<a href="tweetlocation.php?id='.$dir.'"><button>'.$dir.'</button></a><br>';
    
}
?> 
</div>


<style>
body
{
background:url('live/android.jpg');
}

</style>
<?php
foreach(glob('twitter_analysis/*', GLOB_ONLYDIR) as $dir) {
    $dir = str_replace('twitter_analysis/', '', $dir);
   $string = file_get_contents("twitter_analysis/".$dir."/Result.json");
   $json_a = json_decode($string, true);
   //echo $json_a;	
}
?>


<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Topic', 'Positive', 'Negative','Neutral'],
          ['Bangladesh',  1000,      400,23],
          ['England',  1170,      460,23],
          ['Pakistan',  660,       1120,243],
          ['Ukraine',  1030,      540,123]
        ]);

        var options = {
          title: 'Analysis',
          vAxis: {title: 'Topics',  titleTextStyle: {color: 'Black'}}
        };

        var chart = new google.visualization.BarChart(document.getElementById('bar_chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="bar_chart_div" style="width: 65%; height: 80%;border:2px solid #bbb;position:absolute;top:18%;left:30%;box-shadow: 10px 10px 10px 10px #454545;border-radius:10px"></div>
  </body>
</html>
<div id="home" style="position:absolute;top:75%;left:2%;height:50px;width:200px;"><a href='suggestions.php'><button style="height:50px;background:black;color:white"> Suggestions </button></a></div>
<div id="home" style="position:absolute;top:85%;left:2%;height:50px;width:200px;"><a href='live/index.php'><button style="height:50px;background:black;color:white"> News Analysis Section </button></a></div>

  
  
  

  
  
  
  


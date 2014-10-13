<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title></title>
<link rel="stylesheet" href="jquery-ui.css">
<script src="jquery-1.10.2.js"></script>
<script src="jquery-ui.js"></script>
<script>
$(function() {
$( "#accordion" ).accordion({collapsible: true});
$( document ).tooltip();

});
</script>
</head>
<body style="background:url('android.jpg');background-size:100% 100%;background-attachment:fixed;font-family:verdana;background-opacity:0.6">
<center><div id="head" style="width:100%;box-shadow: 10px 10px 10px 10px #454545; color:#454545;background-color:#bbb;">
<font size="6">Most Prevailing News</font><br>
<font size="5">List of News and their Timeline</font></center><br><br></div>
<div id="wrap" style="width:80%;box-shadow: 20px 20px 20px 20px #454545;">
<div id="accordion">
<?php 

$handle = fopen("cleared.json", "r");
$i=1;
if ($handle) {
    while (($line = fgets($handle)) !== false && $i<=50 && $line!==" [ [") {
        echo '<h3 style="background:#57169A;color:#ddd;" title="Rank '.($i).' in Hot list "><center>'.$i.". ". ucfirst($line).'</center></h3>';
	echo '<div style="background:#008287;color:#91D100;">';
	$x="datastore/timeline_".$line.".json";
	$x = preg_replace('/\s+/','',$x);
	$string = file_get_contents($x);
	$json_a = json_decode($string, true);
	echo "<center>";
	$k=0;
	foreach ($json_a as $person_name => $person_a) {
    	echo "<div style='width:100%;background:#001940;border-radius:10px;border:1px solid grey'>" ;
	echo "<b><font size='2'>".$person_a['date']."</font></b><br>";
	echo "<font style='color:#FF981D;'><i>".$person_a['description']."</i></font><br>";
	echo "<font size='2'>".$person_a['source']."</font><br></div><br>";
	if($k<=25)
	$k++;
else break;	
	}
	echo "</center>";

	echo'</div>';$i++;
    }
} else {
    // error opening the file.
} 
fclose($handle);

?>

</div></div>
<div id="home" style="position:fixed;top:75%;right:2%;height:50px;width:200px;"><a href='../index.php'><button style="height:50px;background:black;color:white"> Go back to Home </button></a></div>
<div id="home" style="position:fixed;top:85%;right:2%;height:50px;width:200px;"><a href='../tweetlocation.php'><button style="height:50px;background:black;color:white"> Sentiment and Location analysis </button></a></div>

</body>

</html>

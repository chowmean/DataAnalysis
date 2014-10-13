<html>
  <head>
    <meta charset="utf-8">
    <title>Suggestions</title>
<style>
body
{
background:url('live/android.jpg');
}

</style>
<center>
<div id="head" style="width:100%;box-shadow: 10px 10px 10px 10px #454545; color:#454545;background-color:#bbb;">
<font size="6">Suggestions from tweets</font><br></center><br><br></div>
 </center>

<div id="selector" style="position:absolute;top:20%;left:2%;width:10%;background:#bbb;box-shadow: 2px 2px 2px 2px #454545;border-radius:10px;padding:10px;">
<?php
foreach(glob('twitter_analysis/*', GLOB_ONLYDIR) as $dir) {
    $dir = str_replace('twitter_analysis/', '', $dir);
    echo '<a href="suggestions.php?id='.$dir.'"><button>'.$dir.'</button></a><br>';
}
?> 
</div>
<div id="suggest" style="position:absolute;top:20%;left:30%;width:60%;background:#bbb;border:1px solid black;box-shadow: 2px 2px 2px 2px #454545;border-radius:20px;padding:50px;">
 <center><u><font size="4">SUGGESTIONS ON TOPIC
<?php
if(isset($_GET["id"]))
{$open=$_GET["id"];}
else
{$open='India';}
echo " <font color='blue'>".$open."</font>.</u></font></center><br>";
$string = fopen("twitter_analysis/".$open."/suggestion.json","r");
$i=1;
while (($line = fgets($string)) !== false)
{
print $i.". ".$line."<br>";
$i++;
}
?>
<br><br>
*** These Suggestions contains are not reliable. These are just a food for future work in suggestion field as if it can get better. It is one of the most important tools for any Government Organisation.

 

</div>







<div id="home" style="position:absolute;top:65%;left:2%;height:50px;width:200px;"><a href='index.php'><button style="height:50px;background:black;color:white"> Go back to home </button></a></div>
<div id="home" style="position:absolute;top:75%;left:2%;height:50px;width:200px;"><a href='live/index.php'><button style="height:50px;background:black;color:white"> News Analysis Section </button></a></div>
<div id="home" style="position:absolute;top:85%;left:2%;height:50px;width:200px;"><a href='tweetlocation.php'><button style="height:50px;background:black;color:white"> Tweets Analysis Section </button></a></div>



 </body>
</html>




<?php
$print=array();
$html="";
foreach(glob("store/*xml") as $filename) {
    $xml_file = file_get_contents($filename, FILE_TEXT);
   
    $xml=simplexml_load_file($filename);
	
	foreach ($xml->channel->item as $items){
		$title = "".$items->title;
		$description = $items->description;
		$arr["title"]=$title;
		$print[]=$arr;
		}
}
$print= json_encode($print);




$f = "parsed.json";

file_put_contents($f, $print) or die("Cannot write");
echo "success";

  // and proceed with your code
 





?>  

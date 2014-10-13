<?php 
$handle = @fopen("cleared.json", "r");
if ($handle) {
    $i=1;
    while (($buffer = fgets($handle, 4096)) !== false) {
        echo $i.". ".$buffer;$i++;
    }
    if (!feof($handle)) {
        echo "Error: unexpected fgets() fail\n";
    }
    fclose($handle);
}
?>

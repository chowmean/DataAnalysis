<?php
 class rss {
     var $feed;

  function rss($feed) 
    {   $this->feed = $feed;  }
 
  function parse() 
    {
    $rss = simplexml_load_file($this->feed);
    

    $rss_split = array();
    foreach ($rss->channel->item as $item) {

    $title = (string) $item->title; // Title
    $link   = (string) $item->link; // Url Link
    $description = (string) $item->description; //Description
    $rss_split[] = '<div>
        <a href="'.$link.'" target="_blank" title="" >
            '.$title.' 
        </a>
   <hr>
          </div>
';
    }
    return $rss_split;
  }
  function display($numrows,$head) 
  {
    $rss_split = $this->parse();

    $i = 0;
    $rss_data = '<div class="vas">
           <div class="title-head">
         '.$head.'
           </div>
         <div class="feeds-links">';
    while ( $i < $numrows ) 
   {
      $rss_data .= $rss_split[$i];
      $i++;
    }
    $trim = str_replace('', '',$this->feed);
    $user = str_replace('&lang=en-us&format=rss_200','',$trim);
    $rss_data.='</div></div>';
    return $rss_data;
  }
}
?>
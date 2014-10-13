<div>
  <?php
  include('rssclass.php');
  $feedlist = new rss('http://feeds2.feedburner.com/9lesson');
  echo $feedlist->display(9,"9lessons");
 
  $feedlist = new rss('http://feeds.feedburner.com/nettuts');
  echo $feedlist->display(9,"Nettuts");
 
  $feedlist = new rss('http://feeds.labnol.org/labnol');
  echo $feedlist->display(9,"Labnol");
  ?> 
  </div>
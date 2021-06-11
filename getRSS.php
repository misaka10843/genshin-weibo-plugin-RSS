<?php
/*********************
 * 
 * 解析xml
 * 
 *********************/
$xml = simplexml_load_file('rss.xml');


$title= $xml->channel->item[1]->title;

$description= $xml->channel->item[1]->description;

$link= $xml->channel->item[1]->link;

$pubDate= $xml->channel->item[1]->pubDate;

/*********************
 * 
 * 将获取的数据组合写入多个文件
 * 
 *********************/
$tAd = $title.'<br>'.$description;

echo $tAd.'<br>'.$time.'<br>'.$url;

$rss = fopen("rss.out", "w") or die("Unable to open file!");
$time = fopen("time.out", "w") or die("Unable to open file!");
$url = fopen("url.out", "w") or die("Unable to open file!");


fwrite($rss, $tAd);
fwrite($url, $link);
fwrite($time, $pubDate);

fclose($rss);
fclose($time);
fclose($url);

?>
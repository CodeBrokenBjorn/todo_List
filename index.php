<?php

$response = file_get_contents('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1&api_key=K9KmO0SRBkVjniWlCWU9ENjGbMFR5wQSnLqZ25n6');
$response = json_decode($response,true);
//var_dump($response);

foreach ($response['photos'] as $test) {
 echo '<p>Photo ID:'.$test['id'].'</p>';
 echo '<p>Camera Name :'.$test['camera']['full_name'].'</p>';
 echo '<p>Date Taken:'.$test['earth_date'].'</p>';
 echo '<p>Rover Name:'.$test['rover']['name'].'</p>';
 echo '<img src="'.$test['img_src'].'" width="200px" height="200px"/>';
 echo '<hr/>';
}
?>

 
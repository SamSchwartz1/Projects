<?php
$mysqli = new mysqli(localhost, php, php, mod3);

if($mysqli -> connect_errno){
    printf("Connection Failed: %s\n", $mysqli->connect_error);
    exit;
}

#All php files should require this!
#code flow: login/register page ---> main page

?>
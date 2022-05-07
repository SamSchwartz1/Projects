<?php
    session_start();
    require 'phpreq.php';
    $usernamer = $_SESSION['user_id'];
    $title = $_POST['title'];
    $body = $_POST['body'];
    $link = $_POST['link'];
    if(!hash_equals($_SESSION['token'], $_POST['token'])){
        die("Request forgery detected");
    }
    $stmt = $mysqli->prepare("insert into post (post_user, title, body, link) values (?,?,?,?)");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->bind_param('ssss', $usernamer, $title, $body, $link);
    $stmt->execute();
    $stmt->close();
    header('Location: mainpage.php');



?>
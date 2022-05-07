<?php
    session_start();
    require 'phpreq.php';
    $usernamer = $_SESSION['user_id'];  
    $comment_id = $_POST['post_id'];
    $comment_text = $_POST['comment'];
    if(!hash_equals($_SESSION['token'], $_POST['token'])){
        die("Request forgery detected");
    }
    $stmt = $mysqli->prepare("insert into comment (comment_id, comment_user, comment_text) values (?,?,?)");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->bind_param('iss', $comment_id, $usernamer, $comment_text);
    $stmt->execute();
    $stmt->close();
    header('Location: mainpage.php');




?>
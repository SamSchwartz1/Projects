<?php
    session_start();
    require 'phpreq.php';
    $titley = $_POST['titley'];
    $body = $_POST['new_text'];
    $link = $_POST['new_link'];
    $num = (int)$_POST['edit_post_num'];
    $usernamer = $_SESSION['user_id'];
    $stmt = $mysqli->prepare("UPDATE post SET title=?,body=?,link=? WHERE post_id=?");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    
    if(!hash_equals($_SESSION['token'], $_POST['token'])){
        die("Request forgery detected");
    }
    $stmt->bind_param('sssi',$titley, $body, $link, $num);
    $stmt->execute();
    $stmt->close();
    header("Location: mainpage.php");
    ?>


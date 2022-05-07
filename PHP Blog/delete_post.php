<?php
    session_start();
    require 'phpreq.php';
    $stmt8 = $mysqli->prepare("SELECT comment_user FROM comment WHERE comment_id=?");
    if(!$stmt8){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $usernamer = $_SESSION['user_id'];
    $stmt8->bind_param("i", $usernamer);
    $stmt8->execute();
    $stmt8->bind_result($usr1);
    $stmt8->fetch();
    echo $usr1;
    $id = (int)$_POST['delete_post_num'];
    $stmt8->close();
    if($usr1 != $usernamer){
        header("Location: mainpage.php");
    }
    $stmt6 = $mysqli->prepare("DELETE FROM comment WHERE comment_id=?");
    if(!hash_equals($_SESSION['token'], $_POST['token'])){
        die("Request forgery detected");
    }
    if(!$stmt6){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt6->bind_param('i',$id);
    $stmt6->execute();
    $stmt6->close();
    $stmt7 = $mysqli->prepare("DELETE FROM post WHERE post_id=?");
    if(!$stmt7){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt7->bind_param('i',$id);
    $stmt7->execute();
    $stmt7->close();
    header ("Location: mainpage.php");
    exit();
?>

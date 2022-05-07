<?php
    session_start();
    require 'phpreq.php';
    $id = (int)$_POST['like_id'];
    $like = (int)$_POST['like_button'];
    $stmt2 = $mysqli->prepare("SELECT likes FROM post WHERE post_id=?");
    $stmt2->bind_param('i', $id);
    $stmt2->execute();
    $stmt2->bind_result($likey);
    while($stmt2->fetch()){
        if ($like == 1) {
            $likeValue = $likey + 1;
        }
        if ($like == 2) {
            $likeValue = $likey - 1;
        }
    }
    $stmt2->close();
    $stmt = $mysqli->prepare("UPDATE post SET likes=? WHERE post_id=?");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->bind_param('ii', $likeValue, $id);
    $stmt->execute();
    $stmt->close();
    header("Location: mainpage.php");

    ?>




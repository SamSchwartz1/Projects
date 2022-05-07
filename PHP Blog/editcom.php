<?php
    session_start();
    require 'phpreq.php';
    $body = $_POST['newcom'];
    $num = (int)$_POST['com_post_num'];
    $stmt = $mysqli->prepare("UPDATE comment SET comment_text=? WHERE post_id=?");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->bind_param('si',$body, $num);
    $stmt->execute();
    $stmt->close();
    header("Location: mainpage.php");
    ?>

<?php
    session_start();
    require 'phpreq.php';
    $id = (int) $_POST['com_num'];
    $actualuser = $_SESSION["user_id"];
if(!hash_equals($_SESSION['token'], $_POST['token'])){
	die("Request forgery detected");
}
    $stmt2 = $mysqli->prepare("SELECT post_user FROM comment WHERE post_id=?");
    $stmt2->bind_param('i', $id);
    $stmt2->execute();
    $stmt2->bind_result($usercheck);
    $stmt = $mysqli->prepare("DELETE FROM comment WHERE post_id=?");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->bind_param('i',$id);
    $stmt->execute();
    $stmt->close();
    header("Location: mainpage.php");
?>
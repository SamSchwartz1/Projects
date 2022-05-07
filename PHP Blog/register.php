
<?php
    session_start();
    require 'phpreq.php';
    $newUser = $_POST['newUser'];
    $newPass= $_POST['newPass'];
    $phash = password_hash($newPass, PASSWORD_DEFAULT);
    $stmt = $mysqli->prepare("select username from userInfo");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->execute();
    $stmt->bind_result($username);
    while($stmt->fetch()){
        if($username === $newUser){
            echo 'Username taken, try again';
            header("Location: login.html");
            exit;
        }
    }
    $stmt = $mysqli->prepare("insert into userInfo (username, password1) values (?,?)");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->bind_param('ss', $newUser, $phash);
    $stmt->execute();
    $stmt->close();
    header("Location: mainpage.php");
    ?>

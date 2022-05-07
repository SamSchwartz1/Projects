<?php
// This is a *good* example of how you can implement password-based user authentication in your web application.
//
require 'phpreq.php';
session_start();

// Use a prepared statement
$stmt = $mysqli->prepare("SELECT COUNT(*), username, password1 FROM userInfo WHERE username=?");

// Bind the parameter
$stmt->bind_param('s', $user);
$user = $_POST['usery'];
$stmt->execute();

// Bind the results
$stmt->bind_result($cnt, $user_id, $pwd_hash);
$stmt->fetch();

$pwd_guess = $_POST['pass'];
// Compare the submitted password to the actual password hash
echo $pwd_hash;
echo $cnt;
echo $pwd_guess;
if($cnt == 1 && password_verify($pwd_guess, $pwd_hash)){
	// Login succeeded!
	$_SESSION["user_id"] = $user_id;
	$_SESSION['token'] = bin2hex(openssl_random_pseudo_bytes(32));
	header("Location: mainpage.php");
} else{
	session_destroy();
	header("Location: login.html");
}
 

?>

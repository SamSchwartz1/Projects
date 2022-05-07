<?php
    require 'phpreq.php';
    global $mysqli;
    header("Content-Type: application/json");
    session_start();
    $json_str = file_get_contents('php://input');

    $json_obj = json_decode($json_str, true);

    $username = $_SESSION["user_id"];
    $eventid = (int)$json_obj['eventid'];
    $title = $json_obj['title'];
    $date = (int)$json_obj['day'];
    $time = $json_obj['time'];
    $month = (int)$json_obj['month'];
    $year = (int)$json_obj['year'];

    $stmt = $mysqli->prepare("update events set title=?, date=?, time=?, month=?, year=? where event_id=?");
    if(!$stmt){
        printf("Query Prep Failed: %s\n", $mysqli->error);
        exit;
    }
    $stmt->bind_param('sisiii', $title, $date, $time, $month, $year, $eventid);
    if(!$stmt->execute()){
        echo json_encode(array(
            "success" => false,
            "message" => "Did not add Event"
        ));
        exit;
    }else{
        echo json_encode(array(
            "success" => true,
            "title" => $title,
		    "date" => $date,
		    "time" => $time,
            "month" => $month,
            "year" => $year
        ));
        exit;
    }
    exit;
?>

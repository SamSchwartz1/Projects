<!DOCTYPE html>
<?php session_start(); ?>
<html lang="en">
  <head>
      <title> Main Page </title>
  </head>
  <body>
      <div class = "post">
          <h1> Write a Post! </h1>
          <form name = "input" action = 'post.php' method = "POST">
              Title:
              <input type = 'text' name = 'title' id = 'title'>
              Body:
              <input type = 'text' name = 'body' id = 'body'>
              Link:
              <input type = 'text' name = 'link' id = 'link'>
              <input type = 'hidden' name = 'token' value = "<?php echo $_SESSION['token'];?>" >
              <input type = 'Submit' name = 'Post!'>
            </form>
        </div>
    <div class = "comment"> <!-- Post #s will make commenting on specific posts way easier !-->
            <h1> Comment on a post! </h1>
            <form name = "input" action = "comment.php" method = "POST">
                Post #:
                <input type = 'text' name = 'post_id' id = 'post_id'>
                Comment:
                <input type = 'text' name = 'comment' id = 'comment'>
                <input type = 'hidden' name = 'token' value = "<?php echo $_SESSION['token'];?>" >
                <input type = 'Submit' name = 'Comment!'>
            
            </form>
    </div>

    <div class = "newsreel">
        <h1> Posts by Users: </h1>
       
        
    </div>







<?php
    require 'phpreq.php';  
    $stmt = $mysqli->prepare("SELECT post.post_id, post.post_user, post.title, post.body, post.link, post.likes, comment.post_id, comment.comment_id, comment.comment_user, comment.comment_text from post left join comment on (comment.comment_id = post.post_id) order by post.post_id");
    if(!$stmt){
	    printf("Query Prep Failed: %s\n", $mysqli->error);
	    exit;
}
    $stmt->execute();
    $stmt->bind_result($post_id, $post_user, $title, $body, $link, $likes, $com, $comment_id, $comment_user, $comment_text);
     while($stmt->fetch()){
        printf("<br>");
        printf("Post #: %d<br>", $post_id); #this link helped witb formatting http://etutorials.org/Programming/PHP+MySQL+and+Apache+in+24+hours/Part+III+Getting+Involved+with+the+Code/Hour+13.+Working+with+Strings/Formatting+Strings+with+PHP/
        printf("Username: %s<br>", $post_user);
        printf("Title: %s<br>", $title);
        printf("Body: %s<br>", $body);
        echo "<a href = '$link'> $link</a>"; #not sure how to printf a link so i echoed
        printf("<br>");
        printf("Likes: %s<br>", $likes);
        printf("<br>");
        printf("<br>");
        if($comment_id == $post_id){
            printf("CommentId: %s<br>", $com);
            printf("Username: %s<br>", $comment_user);
            printf("Comment: %s<br>", $comment_text);
        }
        printf("<br>");
    }


    #add script to print out posts

    #add security stuff!!!


#post table should have user,title,body,link, post #

#comment table should have user, comment, # linking to post #

?>

<h2> Like/Dislike Post: </h2>
    <form name = "like" action = "like.php" method = "POST">
        <p>Enter the # of the post you would like to like/dislike:</p>
        <input type = "text" id = "like_id" name = "like_id"><br><br>
        <input type="radio" id="like" name="like_button" value="1">
        <label for="like">Like</label><br>
        <input type="radio" id="dislike" name="like_button" value="2">
        <label for="dislike">Dislike</label><br>
        <input type = "Submit" value = "Submit">    
    </form>

<h2> Edit Post: </h2>
    <form name = "edit_post" action = "edit_post.php" method = "POST">
        Enter the # of the post you would like to edit:
            <input type = "text" id = "edit_post_num" name = "edit_post_num">    
        Enter your new title:
            <input type = "text" id = "titley" name = "titley">
        Enter the text you'd like to replace in this post:
            <input type = "text" id = "new_text" name = "new_text">
        Enter the link you'd link to replace in this post:
            <input type = "text" id = "new_link" name = "new_link">
            <input type = 'hidden' name = 'token' value = "<?php echo $_SESSION['token'];?>" >
            <input type = "Submit" value = "Edit">
    </form>

<h2> Delete Post: </h2>
    <form name = "delete_post" action = "delete_post.php" method = "POST">
    Enter the # of the post you would like to delete:
            <input type = "number" id = "delete_post_num" name = "delete_post_num">    
            <input type = 'hidden' name = 'token' value = "<?php echo $_SESSION['token'];?>" >
            <input type = "Submit" value = "Delete">
    </form>

<h2> Delete Comment: </h2>
    <form name = "delete_comment" action = "deletecom.php" method = "POST">
    Enter the # of the comment you would like to delete:
            <input type = "number" id = "com_num" name = "com_num">    
            <input type = 'hidden' name = 'token' value = "<?php echo $_SESSION['token'];?>" >
            <input type = "Submit" value = "Delete">
    </form>

    <h2> Edit Comment: </h2>
    <form name = "edit_com" action = "editcom.php" method = "POST">
        Enter the # of the comment you would like to edit:
            <input type = "text" id = "com_post_num" name = "com_post_num">    
        Enter your new comment:
            <input type = "text" id = "newcom" name = "newcom">
<input type = 'hidden' name = 'token' value = "<?php echo $_SESSION['token'];?>" >
            <input type = "Submit" value = "Edit">
    </form>

<h2> Logout: </h2>
    <form name = "logout" action = "logout.php">
        <input type = "Submit" value = "Logout">
</form>




</body>
</html>

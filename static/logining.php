
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title>Login</title>
<style>
*
{
align-item:center;
}
body
{
display:flex;
justify-content:center;
align-items:center;
min-height:100vh;
background:url('background2.jpg');
background-size:cover;
background-position:center;
}
.box h2
{

font-family:cursive;
text-decoration:underline;
font-size:35px;
color:white;
}
.box
{
text-align:center;
font-size:25px;
font-family:cursive;
border:2px solid white ;
border-radius:6px;
justify-content:center;
padding:20px 35px;
width:400px;

color:white;
}
.box input
{
font-size:18px;
border-radius:6px;
font-family:cursive;
color:white;
}
.box button
{
margin-top:20px;
font-size:20px;
border-radius:6px;
padding:5px 40px;
cursor:pointer;
font-family:cursive;
}
.box a
{
cusror:pointer;
text-decoration:none;
margin-top:50px;
transition:transform 0.5s;
color:white;
}
.box a::hover
{
text-decoration:underline;
}

</style>
</head>
<body>
<div class="box">
<h2>Login</h2>
<form action="" method="post" autocomplete="off">
<label for="usernameemail">Username or Email:</label></br>
<input type="text" name="usernameemail" id="usernameemail" required value=""> <br>
<label for="password">Password</label></br>
<input type="password" name="password" id="password" required value=""> <br>
<button type="submit" name="submit">Login</button>
</form>
<br>
<p>If you have not register to Unifund website then</br></p>
<a href="registering.php">->Registration<-</a>
</div>
<?php
require 'config.php';
if(isset($_POST["submit"])) {
    $usernameemail = $_POST["usernameemail"];
    $password = $_POST["password"];

    $result = mysqli_query($conn, "SELECT * FROM tb_user WHERE username = '$usernameemail' OR email = '$usernameemail'");
    $row = mysqli_fetch_assoc($result);

    if(mysqli_num_rows($result) > 0) {
        if($password == $row["password"]) {
            $_SESSION["login"] = true;
            $_SESSION["id"] = $row["id"];
            header("Location: practisemainpage.php");
        } else {
            echo "<script> alert('Wrong Password'); </script>";
        }
    } else {
        echo "<script> alert('User Not Registered'); </script>";
    }
}
?>
</body>
</html>
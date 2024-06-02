<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE-edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UniFunds</title>
<style>
.card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.card {
    background-color: #ffffff;
    border-radius: 10px;
    border: 2px solid #007bff;
    padding: 20px;
    margin: 20px;
    width: 30%;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s ease-in-out;
}

.card:hover {
    transform: scale(1.05);
}

.title {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #333;
    position: relative;
}

.title::after {
    content: "";
    display: block;
    width: 200px;
    height: 4px;
    background-color: #007bff;
    position: absolute;
    bottom: -7px;
    left: 50%;
    transform: translateX(-50%);
}

.provider, .criteria, .award, .deadline, .state {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #555;
}

.view-scholarship-button {
    display: inline-block;
    background-color: #4caf50;
    color: #fff;
    padding: 16px 32px;
    font-size: 18px;
    border-radius: 5px;
    text-decoration: none;
    margin-top: 20px;
    transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
}

.view-scholarship-button:hover {
    background-color: #ff0000;
    color: #fff;
}
.translate-widget-container 
{
display:inline-block;
margin-right:20px;
}
.goog-te-combo
 {
 background-color: #007bff;
color: #fff; 
 padding: 20px 40px; 
 border: none;
 border-radius: 5px; 
cursor: pointer;
font-size:100px;
 } 
.goog-te-combo-arrow
 { 
display: none; 
 } 
</style>
<script src="https://translate.google.com/translate_a/element.js?cb=loadGoogleTranslate" async></script>
<script>

function loadGoogleTranslate() 
{
new google.translate.TranslateElement({
includedLanguages:'en,kn,ta,te,ml,as,bn,brx,doi,gu,ks,kok,mai,mni,mr,ne,or,pa,sa,sat,sd,ur,trp,tcy,kha,bho,raj,wbr,kfr,gbm,hne,hi',
layout:google.translate.TranslateElement.InlineLayout.SIMPLE,
autoDisplay:false
},'myid');
}
 document.addEventListener('DOMContentLoaded', loadGoogleTranslate);

        function changeLanguage(select) {
            var languageCode = select.value;
            var translateElement = new google.translate.TranslateElement({ pageLanguage: 'en' });
            translateElement.showWidget({ layout: google.translate.TranslateElement.InlineLayout.SIMPLE }, 'myid');
            translateElement.translatePage(languageCode);
        }
</script>
</head>
<body>
<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
$server = '127.0.0.1';
$username = 'root';
$password = '';
$database = 'scholarship_demo';

$conn = mysqli_connect($server, $username, $password, $database);

// Assuming your form method is POST and form fields are named 'graduation', 'gender', and 'state'
$graduation = mysqli_real_escape_string($conn, $_POST['graduation']);
$gender = mysqli_real_escape_string($conn, $_POST['gender']);
$State = mysqli_real_escape_string($conn, $_POST['State']);

// Build the WHERE clause based on user requirements
$whereClause = "BINARY graduation = '$graduation' AND BINARY gender = '$gender' AND BINARY State = '$State' ";


// Modify the SQL query to include the WHERE clause
$sql = "SELECT * FROM `scholarships` WHERE $whereClause";
$result = mysqli_query($conn, $sql);



$num = mysqli_num_rows($result);

echo "<br>";
if ($num > 0) {
    echo '<div class="card-container">';
    while ($row = mysqli_fetch_assoc($result)) {
        echo '<div class="card">';
        if (isset($row['title'])) {
            echo '<div class="title">'.$row['title'].'</div>';
        }
        if (isset($row['provider'])) {
            echo '<div class="provider">Provider: '.$row['provider'].'</div>';
        }
        if (isset($row['criteria'])) {
            echo '<div class="criteria">Criteria: '.$row['criteria'].'</div>';
        }
        if (isset($row['award'])) {
            echo '<div class="award">Award: '.$row['award'].'</div>';
        }
        if (isset($row['deadline'])) {
            echo '<div class="deadline">Deadline: '.$row['deadline'].'</div>';
        }
        if (isset($row['state'])) {
            echo '<div class="State">State: '.$row['State'].'</div>';
        }
        echo '<a href="scholarship_descripation.php?scholarship_id='.$row['scho_id'].' " class="view-scholarship-button">View Scholarship</a>';
        echo '</div>';
    }
    echo '</div>';
}
else{
echo '<p>No scholarships found matching the criteria.</p>';
}
?>
<div id="myid" class="translate-widget-container">
</div>
</body>
</html>

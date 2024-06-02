<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UniFunds</title>
    <style>
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
    </style>
    <script src="https://translate.google.com/translate_a/element.js?cb=loadGoogleTranslate" async></script>
    <script>
        function loadGoogleTranslate() {
            new google.translate.TranslateElement({
                includedLanguages: 'en,kn,ta,te,ml,as,bn,brx,doi,gu,ks,kok,mai,mni,mr,ne,or,pa,sa,sat,sd,ur,trp,tcy,kha,bho,raj,wbr,kfr,gbm,hne,hi',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
                autoDisplay: false
            }, 'google-translate-element');
        }

        document.addEventListener('DOMContentLoaded', loadGoogleTranslate);

        function changeLanguage(select) {
            var languageCode = select.value;
            var translateElement = new google.translate.TranslateElement({ pageLanguage: 'en' });
            translateElement.showWidget({ layout: google.translate.TranslateElement.InlineLayout.SIMPLE }, 'google-translate-element');
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

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Assuming the scholarship ID is passed as a URL parameter
if (isset($_GET['scholarship_id'])) {
    $scholarship_id = $_GET['scholarship_id'];

    // Fetch scholarship details from the database
    $sql = "SELECT title,eligibility_description, test, url,deadline,award FROM scholarships WHERE scho_id = $scholarship_id";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        $row = mysqli_fetch_assoc($result);
        echo "<h1>" . htmlspecialchars($row['title']) . "</h1>";
        echo "<h2>Eligibility Description</h2>";
        echo "<p>" . htmlspecialchars($row['eligibility_description']) . "</p>";
        echo "<h2>Test</h2>";
        echo "<p>" . htmlspecialchars($row['test']) . "</p>";

 echo "<h2>Deadline</h2>";
        echo "<p>" . htmlspecialchars($row['deadline']) . "</p>";

 echo "<h2>Award</h2>";
        echo "<p>" . htmlspecialchars($row['award']) . "</p>";

        echo '<a href="' . htmlspecialchars($row['url']) . '" class="view-scholarship-button">Apply Now</a>';
    } else {
        echo "No scholarship details found.";
    }
} else {
    echo "Scholarship ID not provided.";
}

mysqli_close($conn);
?>

<div id="google-translate-element" class="translate-widget-container"></div>

</body>
</html>

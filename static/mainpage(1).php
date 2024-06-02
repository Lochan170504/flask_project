<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE-edge">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unifunds</title>
<style>
*{
padding:0;
margin:0;
box-sizing:border-box;
}
body {
    min-height: 100vh;
    background-color: white;
    background-image: url('background4.jpg');
    background-size: cover;
    background-position: center;
    font-family: sans-serif;
}
header
{
position:fixed;
top:0;
left:0;
width:100%;
padding:20px 80px;
display:flex;
justify-content:space-between;
align-items:center;
z-index:99;
}
.logo
{
font-size:2em;
color:white;
user-select:none;
}
.navigation a{
position:relative;
font-size:1.1em;
color:white;
text-decoration:none;
font-weight:500;
margin-left:40px;
}

.navigation a::after{
content: ' ';
position:absolute;
left:0;
bottom:-6px;
width:100%;
height:3px;
background:#fff;
border-radius:5px;
transform:scalex(0);
transition:transform .5s;
}

.navigation a:hover::after{
transform:scalex(1);
}
.navigation .btnlogin-popup
{
width:130px;
height:50px;
background:transparent;
border:2px solid white;
outline:none;
border-radius:6px;
curser:pointer;
font-size:1.1em;
color:#fff;
font-weight:500;
margin-left:40px;
transition:.5s;
}
.navigation .btnlogin-popup:hover
{
background:white;
color:#162938
}
.scholarship-form-container
{
position:absolute;
top:60px;
left:20px;
width:300px;
padding:20px;
border:1px solid #ccc;
border-radius:15px;
box-shadow:0 0 10px rgba(0,0,0,0.1);

}

</style>
<script>

</script>
</head>
<body>
<header>
<h2 class="logo">Logo</h2>
<nav class="navigation">
<a href="#">Home</a>
<a href="#">About Us</a>
<a href="#">Content</a>
<a href="#">Services</a>
<button class="btnlogin-popup">Login</button>
</nav>
</header>
<section class="scholarship-form-container">
<form action="connect.php" method="post">
<div class="form-group">
<label for="graduation">Class</label></br>
<select id="graduation" name="graduation">
<option value="">--Select Class--</option>
<option value="Class 1 to PG">Class 1 to PG</option>
<option value="Undergraduate/Postgraduate">Undergraduate/Postgraduate</option>
<option value="Postgraduate">Postgraduate</option>
</select>
</br>
<label for="gender">Gender</label></br>
<select id="gender" name="gender">
<option value="">--Select Gender--</option>
<option value="Male">Male</option>
<option value="Female">Female</option>
<option value="Transgender">Transgender</option>
</select>
</br>
<div class="india-map">
 <select id="State" name="State">
 <option value="">Select State/Country</option>
 <option value="Karnataka">Karnataka</option>
 <option value="Andhra Pradesh">Andhra Pradesh</option>
<option value="Tamil Nadu">Tamil Nadu</option>
 <option value="Tripura">Tripura</option>
  <option value="Goa">Goa</option>
 <option value="Kerala">Kerala</option>
<option value="Telangana">Telangana</option>
 <option value="Maharashtra">Maharashtra</option>
<option value="Rajasthan">Rajasthan</option>
 </select>
  <br>
 <button type="submit">Submit</button>
</div>
</form>
</section>
<div class="accounment-container">
<p>Unifund Scholarship Validation</p>
<p>THIS IS THE ACCOUNMENT THAT SCROLL UP</p>
<p>THIS IS THE ACCOUNMENT THAT SCROLL UP</p>
<p>THIS IS THE ACCOUNMENT THAT SCROLL UP</p>
<p>THIS IS THE ACCOUNMENT THAT SCROLL UP</p>
<p>THIS IS THE ACCOUNMENT THAT SCROLL UP</p>
</div>
<div class="acknowlegment-no">
<p>To those Student who have apply the unifund scholarship can check whether  there are eligibile or not</p></br>
<form action="eligiabiltiy.html">
<label for="Acknowlegment-number">Enter your Acknowlegment Number<input type="text" /></label></br>
<button type="submit">Submit</button>
</form>
<div class ="application">
<p>Unifunds providing the scholarship.If you want to apply </p>
</br><a href="login.html">Click here</a>
<div class="provider-name">
<div class="item">Box1</div>
<div class="item">Box2</div>
<div class="item">Box3</div>
<div class="item">Box4</div>
<div class="item">Box5</div>
</div>
<footer>
 <p>&copy; 2022 Scholarship Portal. All rights reserved.</p>
  </footer>
</body>
</html>
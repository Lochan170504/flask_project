<?php
$scho_id=$_GET['scho_id'];
$query="SELECT * FROM scholarships WHERE id=$scho_id";
$result=mysqli_query($connection,$query);
if($result)
{
$scholarship=mysqli_fetch_assoc($result);
echo "<h2>{$scholarship['test']}</h2>;
echo "<p>{$scholarship['eligibility_description']}</p>;
}
else
{
echo "error retreving scholarship".mysqli_error($connection);
}
mysqli_close($connection);
?>
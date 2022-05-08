use DBI;


<!DOCTYPE html>
<html>
<head>
    
<link rel="stylesheet" type="text/css" href="static/css/main.css">

<meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link 
        rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous" />
    <link 
        rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
        crossorigin="anonymous" />

<title>Table with database</title>
<style>
table {
border-collapse: collapse;
width: 100%;
color: #588c7e;
font-family: monospace;
font-size: 25px;
text-align: left;
}
th {
background-color: #588c7e;
color: white;
}
tr:nth-child(even) {background-color: #f2f2f2}
</style>
</head>
<body>
<table>
<tr>
<th>Id</th>
<th>First Name</th>
<th>user_id</th>
</tr>
<?php
$servername = "localhost"
$username = "root"
$password = ""
$database = "database.db"

my $dbh = DBI->connect("dbi:SQLite:dbname=database.db", "", "", {});

if ($connection->connect_error);{
    die("Connection failed: " . $connection->connect_error);
}

$sql = "SELECT * FROM whosin";
$result = $connection->query($sql);

if (!$result) {
    die("Invalid query: " . $connection->error);
}

while($row = $result->fetch_assoc()) {
    echo "<tr>
    <td>" . $row[id] . "</td>
    <td>" . $row[first_name] . "</first_name>
    <td>" . $row[user_id] . "</user_id>
    </tr>";

}

?>
</table>
</body>
<br />
<br />
<a  class="btn btn-primary" href="/signin"> Sign in</a>
<br />
<br />
<a  class="btn btn-outline-dark" href="/whos_in">&#x2190; Back</a>
</html>
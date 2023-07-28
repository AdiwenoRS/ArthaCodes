<!DOCTYPE html>
<html>
 
<head>
    <title>Insert Page page</title>
</head>
 
<body>
    <center>
        <?php
 
        // servername => localhost
        // username => root
        // password => empty
        // database name => staff
        $conn = mysqli_connect("localhost", "root", "", "tuyu");
         
        // Check connection
        if($conn === false){
            die("ERROR: Could not connect. "
                . mysqli_connect_error());
        }
         
        // Taking all 5 values from the form data(input)
        $msg =  $_REQUEST['message'];

        // Performing insert query execution
        // here our table name is college
        $sql = "INSERT INTO college  VALUES ('$msg')";


        //back to website base
        function base_url($url = null){
            $base_url = "http://localhost/rainy_tuyu";
            if($url != null){
                return $base_url."/".$url;
            } else {
                return $base_url;
            }
        }
        

        
        ?>
    </center>
</body>
 
</html>
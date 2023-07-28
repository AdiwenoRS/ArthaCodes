<!php
require_once "../_config/config.php"
!>

<!DOCTYPE html>   
<html>
   <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Flying Message</title>
    <link rel="stylesheet" href="style.css">
    
   </head>

   <body>

      <!-- LETTER -->
      <div class="msbtn">
         <a href="letter/index.php">
            <button type="button"> <b>MESSAGES</b></button>
         </a>
      </div>
      <div class="imgletter">
         <a onclick="openForm()">
            <img src="img/MessageCropped.png" width="500px">
         </a>
      </div>
      

      
      <!-- FORM POP UP -->
      <div class="form-popup" id="myForm">
         <form name="input" 
               action="" 
               method="POST"
               class="form-container">
            <center>
           <h1>Put Your Message Here</h1>
            </center>
            
           <input type="text" placeholder="" name="input" required>
           <b>
           <input type="submit" class="btn" onclick="closeForm()" value="Send" >
           <!--<button type="button" class="btn" onclick="closeForm()"><b>Send</b></button>-->
           <button type="button" class="btn cancel" onclick="closeForm()">Close</b></button>
         </form>
       </div>


       
<script>
   function openForm() {
     document.getElementById("myForm").style.display = "block";
   }
   
   function closeForm() {
     document.getElementById("myForm").style.display = "none";
   }
   </script>

   </body>


</html>


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
         
        // Taking all values from the form data(input)
        if (empty($_POST["input"])){
            False;
         }else{
            @$msg = $_POST["input"];
         }

        // here our table name is college
        @$sql = "INSERT INTO msg (message) VALUES ('$msg')";

        mysqli_query($conn, $sql)

      
         //echo "$sql";


  

        
        ?>
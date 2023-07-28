<?php
require_once "../_config/config.php"
?>


<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sky Login</title>
  <link rel="stylesheet" href="style.css">
  <link rel="icon" href="download.png" type="image/png">
</head>

<body>
<div id="wrapper">
  <div class="wrapper">

    <!--  logindatabase start -->
    <!--  logindatabase end -->

    <style>
      body {
        background-color: #F5EFE6;
        background-image: linear-gradient(rgba(0, 0, 0, 0.16),rgba(0, 0, 0, 0.16)) , url(rain.jfif);
        background-repeat: no-repeat;
        background-attachment: scroll;
        background-size: contain;
        background-position: right 0% top 0%;
      }
    </style>
    </style>



    <div style="display:inline-block;vertical-align:top;">
      <div class="card">
        <?php
        if(isset($_POST['enter'])){
            $user = trim(mysqli_real_escape_string($con, $_POST['usr']));
            $pass = trim(trim(mysqli_real_escape_string($con, $_POST['pass'])));
            $sql_login = mysqli_query($con, "SELECT * FROM user WHERE username = '$user' AND password = '$pass'")
             or die (mysqli_error($con));
             if (mysqli_num_rows($sql_login)){
                $_SESSION['usr']=$user;
                echo"<script>window.location='".base_url()."';</script>";
             } else { ?> 
                
                <div class="alert alert-danger alert-dismissable" role="alert">
                    <strong>Login invalid!</strong> Wrong username or password 
                </div>
                
            <?php
        }
    }
    ?>
        
      <form name="input" 
      action="" 
      method="post" >
        <h3>Login</h3>
        <div class="inputBox">
        
          <input type="text" name="usr" required="required">
        <!--  <span>Username</span> -->        
        </div>
        <div class="inputBox">
          <input type="password" name="pass" required="required">
        <!--  <span>Password</span> -->
        </div>

        <div class="Box">
        <input type="submit" name="enter" value="ENTER">
        </div>
    </form>  
         
      </div>
    </div>
    <div style="display:inline-block;">
      <div class="wordmar">
        <p><b>Favorite Sky</b></p>
      </div>
      <div class="wordmar1">
        <p>Fell to happiness</p>
      </div>
    </div>

  </div>
</div> 
</body>

</html>
    
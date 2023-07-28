<?php
require_once "../_config/config.php"
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rainy Login</title>
  
  <!-- css link -->
  <link rel="stylesheet" href="style.css">
  <!-- icon link -->
  <link rel="icon" href="download.png" type="image/png">
  <!-- Bootstrap link -->
  <link href="../_assets/css/bootstrap.min.css" rel="stylesheet">

</head>

<body>
  <div class="wrapper">

    <style>
      body {
        background-color: #F5EFE6;
        background-image: linear-gradient(rgba(0, 0, 0, 0.16),rgba(0, 0, 0, 0.16)) , url(rain.jfif);
        background-repeat: no-repeat;
        background-attachment: scroll;
        background-size: 1000px;
        background-position: right 0% top 0%;
      }
    </style>
    </style>



    <div style="display:inline-block;vertical-align:top;">
      <div class="card">
      <?php
            if(isset($_POST['login'])){
               $user = trim(mysqli_real_escape_string($con,$_POST['user']));
               $pass = sha1(trim(mysqli_real_escape_string($con,$_POST['pass'])));
               $sql_login = mysqli_query($con, "SELECT * FROM user WHERE username = '$user' AND password = '$pass' ") or die(mysqli_error($con));
               if (mysqli_num_rows($sql_login) > 0){
                  $SESSION['user']=$user;
                  echo"<script>window.location=".base_url().";</script>";
               } else { ?>
                     <div class="row">
                        <div class="col-lg-6 col-lg-offset-3">
                           <div class="alert alert-danger alert-dismissable"
                           role="aler">
                              <a href="#" class="close" data-dismiss="alert"
                              aria-label="close">&times;</a>
                              <span class="glyphicon glyphicon_exlamation-sign" aria-hidden=true></span>
                             <strong>Login gagal!</strong> Username / Password salah
                           </div>
                        </div>
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
          <input type="text" name="user" required="required">
          <span>Username</span>
        </div>
        <div class="inputBox">
          <input type="password" name="pass" required="required">
          <span>Password</span>
        </div>

        <button><a>ENTER</a></button>
    </form>  
         
      </div>
    </div>
    <div style="display:inline-block;">
      <div class="wordmar">
        <p><b>Favorite Rain</b></p>
      </div>
      <div class="wordmar1">
        <p>Fell to happiness</p>
      </div>
    </div>

  </div>

</body>

</html>
    
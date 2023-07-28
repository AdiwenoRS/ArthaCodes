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
         <a href="../index.php">
            <button type="button"> <b>LETTER</b></button>
         </a>
      </div>
      
      <div class="judul">
         </div>
      <?php
         include "../_config/config.php";
         ?>


<center>
      <div class="scroll">
   <h1><center>MESSAGES</center></h1>

      <?php 
         $sql="select * from msg";
         
         $hasil=mysqli_query($con,$sql);
         $no=0;
         while ($data = mysqli_fetch_array($hasil)){
            $no++;
            ?>
         <div class=text>
            <table>
               <td><?php echo "@- " ,$data["message"]; ?></td>
               
            </table>
         </div>
         <?php
         }
         ?>
            
         </div>           
      </center>
      
   </body>
</html>
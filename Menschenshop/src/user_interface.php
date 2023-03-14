<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../stylesheet.css">
    <title>Online-Shop</title>
</head>
<body>
    <img src="../bILDER_SRC/walkurelogo.png" onclick="window.location ='../index.php'" alt="logo">
    <h2>
      <table id="tb1">
       <tr id="tb1">
          <th id="tb1"><a href="../index.php">Homepage</a></th>
          <th id="tb1"><a href="impressum.html">Impressum</a></th>
          <th id="tb1"><a href="anmelden.php?logout">Abmelden</a></th>
        </tr>
    </table>
    </h2>
    <br>
    <p>Willkommen im internen Bereich!</p>
    <p>Möchten sie Ihrem Sortiment ein neues Produkkt hinzufügen? <a href="addprodukt.php">[Klick hier]</a></p>
    </tbody>
    <br>
    <table width='50%'>
        <thead>
            <tr>
                <th>ID</th>
                <th>Produktname</th>
                <th>Preis</th>
                <th>Bild</th>
            </tr>
        </thead>
    </table>
    <tbody>
    <?php 
        session_start();
        $user_id = $_SESSION['user_id'];
        if(!isset($user_id))
        {
         die('Sie sind nicht angemeldet! <a href="anmelden.php">[Login]</a>');
        }

        //prüfen ob die datenbank erreichbar ist
        $servername = "127.0.0.1"; 
        $username = "simon";
        $password = "himbeerkuchen";
        $db = "q2_andrewtateshop";

        // Create connection
        $connection = new mysqli($servername, $username, $password, $db);

        // Check connection
        if ($connection->connect_error){
            die("Connection failed: " . $conn->connect_error);
        }

        //daten von der datenbank lesen
        $sql = "SELECT * FROM produkt WHERE fk_verkaeuferID = $user_id"; 
        $result = $connection->query($sql); //suche ausführen und speichern

        //suche überprüfen
        if (!$result) {
            die("Invalid query: " . $connection->error);
        }

        //daten von der datenbank lesen und ausgeben
        while($row = $result->fetch_assoc()){
            echo "
            <table width='54%'>
                <tr>
                    <td>$row[ID]</td>
                    <td>$row[name]</td>
                    <td>$row[preis] $row[waehrung]</td>
                    <td><img src='../$row[bild]' width='50' height='50'/></td>
                </tr>
            </table>
            ";
        }

        if($_SERVER['REQUEST_METHOD'] == 'POST'){ //checken ob daten übertragen wurden
            $pID = $_POST["pID"];//wenn es klappt daten übertragen

            $sql = "DELETE FROM `produkt` WHERE `id` = $pID";
            $result = $connection->query($sql); //query ausführen
            
            header("location: /simon/src/user_interface.php"); //wenn es funktioniert hat den user zur seite zurückschicken
        }  

    ?>
    </tbody>
    </br>
    <h2>
		Produkt löschen
	</h2>
    <form action="user_interface.php" method="post">
        <label>Produkt ID</label>
        <input type="text" placeholder="ID" name="pID">
        <br>
        <input type="submit" name="löschen" value="loeschen"></button><br>
    </form>
</body>
</html>
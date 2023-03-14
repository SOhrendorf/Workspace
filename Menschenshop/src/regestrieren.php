<?php
        //Stammvariabeln für DB
        $servername = "127.0.0.1";
        $username = "simon";
        $password = "himbeerkuchen";
        $db = "q2_andrewtateshop";

        //Verbindung aufbauen
        $connection = new mysqli($servername, $username, $password, $db);

         // Check connection
         if ($connection->connect_error){
            die("Connection failed: " . $conn->connect_error);     
        }

    $errorMessage = "";
    $succesMessage = "";

    if($_SERVER['REQUEST_METHOD'] == 'POST'){ //checken ob daten übertragen wurden
        $vorname = $_POST["vorname"]; //wenn es klappt daten übertragen 
        $name = $_POST["name"];
        $email = $_POST["email"];
        $passwort = $_POST["passwort"];
        $ort = $_POST["ort"];
        $plz = $_POST["plz"];
        $strasse = $_POST["strasse"];
        $hausnummer = $_POST["hausnummer"];

        do{ 
            if (empty($vorname) || empty($name) || empty($email) || empty($passwort) || empty($ort) || empty($plz) || empty($strasse) || empty($hausnummer)){
                // password validation

                $errorMessage = "Alle Felde müssen ausgefüllt sein";
                break;
            } //wenn ein feld leer ist error message
            if (empty($passwort)){
                $error = true;
                $errorMessage = "Bitte Passwort eingeben.";

                break;
             } else if (preg_match("/[a-z]/", $passwort)
                   && preg_match("/[A-Z]/", $passwort)
                   && preg_match("/[0-9]/", $passwort)) {
                $error = true;
                $errorMessage = "Das Passwort muss Kleinbuchstaben, Großbuchstaben und Zahlen enthalten.";
                break;
            } else if (strlen($passwort) < 8) {
                $error = true;
                $errorMessage = "Das Passwort muss mindestens 8 Zeichen lang sein.";
                break;
            } 
            

            //einen kunden in die datenbank eintragen
            //Pfefer
            $peper = "gretz4350th78T/e05";
            $passwort = $passwort.$peper;
            //hash + Sals
            $pwd = password_hash($passwort, PASSWORD_BCRYPT, array("cost" => 11));
            $sql = "INSERT INTO benutzer (vorname, name, email, passwort, ort, plz, strasse, hausnummer) " .
                    "VALUES ('$vorname', '$name', '$email', '$pwd', '$ort', '$plz', '$strasse', '$hausnummer')";

            $result = $connection->query($sql); //query ausführen
            
            if(!$result){ //ggf. fehler anzeigen
                $errorMessage = "Invalid query: " . $connection->error;
                break;
            }

            $succesMessage = "Kunde wurde hinzugefügt";

            header("location: /simon/src/anmelden.php"); //wenn es funktioniert hat den user zur seite zurückschicken
            exit;

        } while (false);
    }

?>

<!DOCTYPE html>
<html lang="de">
    <head>
        <link rel="stylesheet" href="../stylesheet.css">
        <title>
          Anmelden
        </title>
    </head>
    
    <body>
        <img src="../bILDER_SRC/walkurelogo.png" onclick="window.location ='../index.php'" alt="logo">
        <h1>
			Neunen Benutzer anlegen
		</h1>
        <table>
            <tr>
                <th id="tb1">
                        <a href="../index.php">Startseite</a>
                </th>
                <th id="tb1">
                        <a href="impressum.html">Impressum</a>
                </th>
                <th id="tb1">
                    <a href="anmelden.php">Anmelden</a>
                </th>    
            </tr>
        </table>
        </P>

        <h2>Kunden registrieren</h2>

        <?php
            if(!empty($errorMessage)){ //fehlermeldung wenn es schiefgeht
                echo"
                    <strong> $errorMessage </strong>
                    <button type ='button' data-bs-dismiss='alert' aria-label='Close'></button>
                ";
            }
        ?> 
        
        <form method="post"> <!--Eingabefelder -->
            <label>Vorname</label>
            <input type="text" placeholder="Vorname" name="vorname">
            <br>
            <label>Nachname</label>
            <input type="text" placeholder="Nachname" name="name">
            <br>
            <label>E-Mail</label>
            <input type="text" placeholder="E-Mail" name="email">
            <br>
            <label>Passwort</label>
            <input type="password" placeholder="Passwort" name="passwort">
            <br>
            <label>Ort</label>
            <input type="text" placeholder="Ort" name="ort">
            <br>
            <label>PLZ</label>
            <input type="text" placeholder="Postleitzahl" name="plz">
            <br>
            <label>Straße</label>
            <input type="text" placeholder="Starße" name="strasse">
            <br>
            <label>Straßennummer</label>
            <input type="text" placeholder="Hausnummer" name="hausnummer">
            <br>

            <?php
                if(!empty($succesMessage)){ //meldung wenn es geklappt hat
                 echo"
                    <strong> $succesMessage </strong>
                    <button type ='button' data-bs-dismiss='alert' aria-label='Close'></button>
                 ";
                }
            ?>

            <button type="submit">Registrieren</button>
        </form>
    </body>
    <p>
    <img src="../bILDER_SRC/bepett.png" width ="60%" height="30%"> <br>
    
    <h1>Bei uns sind sie sicher</h1>
</html>
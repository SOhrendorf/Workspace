class Hund {
    beine:number = 4
    static anzahlAllerHunde:number = 10 //keine Instansvariable, sondern eine Klassenvariabel; für alle aus der Klasse gleich

    laufen():void{
        console.log("Running in the 90s")
    }

    bellen():void {
        console.log("Wuff")
    }

}

class Pudel extends Hund {
}
var rex:Pudel = new Pudel()
rex.laufen()
Hund.anzahlAllerHunde = 50
console.log(Hund.anzahlAllerHunde)
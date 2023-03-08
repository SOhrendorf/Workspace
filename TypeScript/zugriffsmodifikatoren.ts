class Hund {
    private beine:number = 4

    public setBeine(beine:number) {
        if(beine < 0) {
            console.log("Fehler negative Anzahl an Beinen nicht möglich. Also was zu Hölle machst du da ?!")
        }
        else{
            this.beine = beine
        }
    }

    public getBeine():number {
        return this.beine
    }

    private laufen():void{ //keine Angabe = public; public kann von allem aufgrufen werden
        console.log("Running in the 90s")
    }

    bellen():void {
        this.laufen() //private kann nur aus der Klasse aufgrufen werden
    }

}

class Pudel extends Hund { // eine Unterklasse darf nur protected aufrufen
    public test():void{
        this.laufen() //nicht beachten, leigt an Z.17 private
    }
}
var rex:Pudel = new Pudel()
var rexi:Hund = new Hund() //sinvolles Beispiel

rex.bellen()
rexi.setBeine(-1)
console.log(rexi.getBeine())
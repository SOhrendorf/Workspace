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

var rex:Hund = new Hund()

function id<T>(param:T):T{ // auch arrays sind möglich param:T[]
    return param
}

console.log(id(rex).getBeine())
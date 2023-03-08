class Wohnung {
    zimmer:number
    groesse:number
    balkon:Boolean

    constructor(z:number, g:number, b:Boolean) {
        this.zimmer = z
        this.groesse = g
        this.balkon = b
    }

    preis():number {
        if (this.balkon) {
            return 5*this.groesse*this.zimmer
        }
        else{
            return 2*this.groesse*this.zimmer  
        }
    }
}
var meineWohnung:Wohnung = new Wohnung(10, 1000, true)

var zweiteWohnung:Wohnung = new Wohnung(1.5, 35, false)

console.log(meineWohnung.preis())
console.log(zweiteWohnung.preis())
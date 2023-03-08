class Tier {
    laufen():void {
        console.log("Ich will raus")
    }
}

class Hund extends Tier{
    beine:number = 4

    bellen():void {
        console.log("Wuff")
    }
}

class Pudel extends Hund {
    laufen():void {
        console.log("running in the 90s")
    }
}

class Schaeferhund extends Hund { // extends funktioniert nur einmal; kann nur von einer Klasse erben

}

var rex:Hund = new Pudel()
var milo:Hund = new Schaeferhund()
var hunde:Hund[] = [rex, milo]
for(var i = 0; i < 2; i++) {
    hunde[i].laufen()
}
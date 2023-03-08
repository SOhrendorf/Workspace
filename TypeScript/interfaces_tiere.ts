interface Tier {
    beine:number
    laufen:() => void
}

class Hund implements Tier{ //könnte  von mehreren interfaces ehrben
    beine:number = 4

    laufen():void{
        console.log("Ich will raus!")
    }

    bellen():void {
        console.log("Wuff")
    }
}

class Pudel extends Hund {
    laufen():void {
        console.log("running in the 90s")
    }
}

class Schaeferhund extends Hund {

}

var rex:Hund = new Pudel()
var milo:Hund = new Schaeferhund()
var hunde:Tier[] = [rex, milo]
for(var i = 0; i < 2; i++) {
    hunde[i].laufen()
}
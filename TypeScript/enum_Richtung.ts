enum Richtung{ //enum = Aufzählung
    HOCH, //zählt von alleine weiter; fängt standerdmäßig bei 0 an
    RUNTER = 42,
    LINKS ,  //immer Zahl davor +1
    RECHTS,
}

console.log(Richtung.RECHTS)
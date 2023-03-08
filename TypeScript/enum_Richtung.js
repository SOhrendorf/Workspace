var Richtung;
(function (Richtung) {
    Richtung[Richtung["HOCH"] = 0] = "HOCH";
    Richtung[Richtung["RUNTER"] = 42] = "RUNTER";
    Richtung[Richtung["LINKS"] = 43] = "LINKS";
    Richtung[Richtung["RECHTS"] = 44] = "RECHTS";
})(Richtung || (Richtung = {}));
console.log(Richtung.RECHTS);

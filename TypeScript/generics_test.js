var Hund = /** @class */ (function () {
    function Hund() {
        this.beine = 4;
    }
    Hund.prototype.setBeine = function (beine) {
        if (beine < 0) {
            console.log("Fehler negative Anzahl an Beinen nicht möglich. Also was zu Hölle machst du da ?!");
        }
        else {
            this.beine = beine;
        }
    };
    Hund.prototype.getBeine = function () {
        return this.beine;
    };
    Hund.prototype.laufen = function () {
        console.log("Running in the 90s");
    };
    Hund.prototype.bellen = function () {
        this.laufen(); //private kann nur aus der Klasse aufgrufen werden
    };
    return Hund;
}());
var rex = new Hund();
function id(param) {
    return param;
}
console.log(id(rex).getBeine());

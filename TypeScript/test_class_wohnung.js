var Wohnung = /** @class */ (function () {
    function Wohnung(z, g, b) {
        this.zimmer = z;
        this.groesse = g;
        this.balkon = b;
    }
    Wohnung.prototype.preis = function () {
        if (this.balkon) {
            return 5 * this.groesse * this.zimmer;
        }
        else {
            return 2 * this.groesse * this.zimmer;
        }
    };
    return Wohnung;
}());
var meineWohnung = new Wohnung(10, 1000, true);
var zweiteWohnung = new Wohnung(1.5, 35, false);
console.log(meineWohnung.preis());
console.log(zweiteWohnung.preis());

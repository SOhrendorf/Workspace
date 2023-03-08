var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
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
var Pudel = /** @class */ (function (_super) {
    __extends(Pudel, _super);
    function Pudel() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Pudel.prototype.test = function () {
        this.laufen();
    };
    return Pudel;
}(Hund));
var rex = new Pudel();
var rexi = new Hund();
rex.bellen();
rexi.setBeine(-1);
console.log(rexi.getBeine());

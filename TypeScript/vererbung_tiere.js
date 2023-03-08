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
var Tier = /** @class */ (function () {
    function Tier() {
    }
    Tier.prototype.laufen = function () {
        console.log("Ich will raus");
    };
    return Tier;
}());
var Hund = /** @class */ (function (_super) {
    __extends(Hund, _super);
    function Hund() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.beine = 4;
        return _this;
    }
    Hund.prototype.bellen = function () {
        console.log("Wuff");
    };
    return Hund;
}(Tier));
var Pudel = /** @class */ (function (_super) {
    __extends(Pudel, _super);
    function Pudel() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Pudel.prototype.laufen = function () {
        console.log("running in the 90s");
    };
    return Pudel;
}(Hund));
var Schaeferhund = /** @class */ (function (_super) {
    __extends(Schaeferhund, _super);
    function Schaeferhund() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    return Schaeferhund;
}(Hund));
var rex = new Pudel();
var milo = new Schaeferhund();
var hunde = [rex, milo];
for (var i = 0; i < 2; i++) {
    hunde[i].laufen();
}

var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (_) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var panels = [19846, 11043, 43792, 2785, 52805, 58649, 56421, 5069, 62964, 12501, 29466, 4776, 43439, 428];
var largePanels = [11043, 19846, 2785, 43792];
var smallPanels_all = [52805, 58649, 56421, 5069, 62964, 12501, 29466, 4776, 43439, 428];
var smallPanels_reihe = [62964, 12501, 29466, 4776, 43439, 428];
var specialPanels = [56421, 5069, 58649, 52805];
var sortedPanels = [];
var address = "http://192.168.178.68:16021/api/v1/gEnntf1ygTGNOq0b2fxW8mpsLLdc1ymi/effects";
//Beginn Client
var client = /** @class */ (function () {
    function client() {
    }
    client.buildBaseRequestAddress = function (ipAddress, authToken) {
        return "http://" + ipAddress + ":" + client.defaultPort + "/api/v1/" + authToken;
    };
    client.convertHSVtoRGB = function (color) {
        // based on: https://stackoverflow.com/questions/17242144/javascript-convert-hsb-hsv-color-to-rgb-accurately
        var h = color.hue;
        var s = color.saturation;
        var v = color.value;
        var r, g, b, i, f, p, q, t;
        i = Math.floor(h * 6);
        f = h * 6 - i;
        p = v * (1 - s);
        q = v * (1 - f * s);
        t = v * (1 - (1 - f) * s);
        switch (i % 6) {
            case 0:
                r = v, g = t, b = p;
                break;
            case 1:
                r = q, g = v, b = p;
                break;
            case 2:
                r = p, g = v, b = t;
                break;
            case 3:
                r = p, g = q, b = v;
                break;
            case 4:
                r = t, g = p, b = v;
                break;
            case 5:
                r = v, g = p, b = q;
                break;
            default:
                r = 0, g = 0, b = 0;
                break;
        }
        return {
            red: Math.round(r * 255),
            green: Math.round(g * 255),
            blue: Math.round(b * 255)
        };
    };
    client.callPUT = function (relativePath, body) {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                return [2 /*return*/, fetch(client.buildBaseRequestAddress(this.ipAddress, this.authToken) + relativePath, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(body)
                    })];
            });
        });
    };
    client.setPanelColors = function (data) {
        return __awaiter(this, void 0, void 0, function () {
            var animData, json;
            var _this = this;
            return __generator(this, function (_a) {
                data.forEach(function (panel) { return _this.colors.set(panel.panelId, panel.color); });
                if (data.length >= 1) {
                    animData = "" + data.length +
                        data
                            .map(function (entry) { return " " + entry.panelId + " 1 " + entry.color.red + " " + entry.color.green + " " + entry.color.blue + " 0 1"; })
                            .join("");
                    json = {
                        "write": {
                            "command": "display",
                            "animType": "static",
                            "animData": animData,
                            "loop": false,
                            "palette": []
                        }
                    };
                    this.callPUT("/effects", json);
                }
                return [2 /*return*/];
            });
        });
    };
    client.setPanelColor = function (panelId, color) {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                this.setPanelColors([{ panelId: panelId, color: color }]);
                return [2 /*return*/];
            });
        });
    };
    client.ipAddress = "192.168.178.68";
    client.authToken = "gEnntf1ygTGNOq0b2fxW8mpsLLdc1ymi";
    client.defaultPort = 16021;
    client.colors = new Map();
    return client;
}());
//Beginn Server
function alleKachelnFärben(color) {
    var data = panels.map(function (entry) { return ({
        panelId: entry,
        color: client.convertHSVtoRGB({ hue: color / 360, saturation: 1, value: 1 })
    }); });
    client.setPanelColors(data);
}
//Start function mit delay option 
function start() {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            alleKachelnFärben(120);
            return [2 /*return*/];
        });
    });
}
start(); //erste Aufruf

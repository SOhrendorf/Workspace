"use strict";
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
var __spreadArrays = (this && this.__spreadArrays) || function () {
    for (var s = 0, i = 0, il = arguments.length; i < il; i++) s += arguments[i].length;
    for (var r = Array(s), k = 0, i = 0; i < il; i++)
        for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
            r[k] = a[j];
    return r;
};
exports.__esModule = true;
var node_fetch_1 = require("node-fetch");
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
    client.testi = function () {
        console.log("halihalo");
    };
    client.getAllPanelIds = function (sorted) {
        var _a, _b;
        return __awaiter(this, void 0, void 0, function () {
            var response, json, positionData, panels, panelIds;
            return __generator(this, function (_c) {
                switch (_c.label) {
                    case 0: return [4 /*yield*/, this.getAllPanelInfo()];
                    case 1:
                        response = _c.sent();
                        if (response.status !== 200) {
                            return [2 /*return*/, []];
                        }
                        return [4 /*yield*/, response.json()];
                    case 2:
                        json = _c.sent();
                        positionData = (_b = (_a = json.panelLayout) === null || _a === void 0 ? void 0 : _a.layout) === null || _b === void 0 ? void 0 : _b.positionData;
                        panels = sorted ? positionData.sort(function (a, b) { return a.y - b.y; }) : positionData;
                        panelIds = panels === null || panels === void 0 ? void 0 : panels.map(function (entry) { return entry.panelId; }).filter(function (entry) { return entry !== 0; });
                        return [2 /*return*/, panelIds];
                }
            });
        });
    };
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
    client.callGET = function (relativePath) {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                return [2 /*return*/, node_fetch_1["default"](client.buildBaseRequestAddress(this.ipAddress, this.authToken) + relativePath, { method: 'GET' })];
            });
        });
    };
    client.callPUT = function (relativePath, body) {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                return [2 /*return*/, node_fetch_1["default"](client.buildBaseRequestAddress(this.ipAddress, this.authToken) + relativePath, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(body)
                    })];
            });
        });
    };
    client.getAllPanelInfo = function () {
        return __awaiter(this, void 0, void 0, function () {
            return __generator(this, function (_a) {
                return [2 /*return*/, this.callGET("")];
            });
        });
    };
    client.getPanelColor = function (panelId) {
        return this.colors.get(panelId);
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
    client.setBrightness = function (level) {
        return __awaiter(this, void 0, void 0, function () {
            var data;
            return __generator(this, function (_a) {
                data = { brightness: { value: level } };
                this.callPUT("/state", data);
                return [2 /*return*/];
            });
        });
    };
    client.setState = function (on) {
        return __awaiter(this, void 0, void 0, function () {
            var data;
            return __generator(this, function (_a) {
                data = { on: { value: on } };
                this.callPUT("/state", data);
                return [2 /*return*/];
            });
        });
    };
    client.setHue = function (hue) {
        return __awaiter(this, void 0, void 0, function () {
            var data;
            return __generator(this, function (_a) {
                data = { hue: { value: hue } };
                this.callPUT("/state", data);
                return [2 /*return*/];
            });
        });
    };
    client.setSaturation = function (sat) {
        return __awaiter(this, void 0, void 0, function () {
            var data;
            return __generator(this, function (_a) {
                data = { sat: { value: sat } };
                this.callPUT("/state", data);
                return [2 /*return*/];
            });
        });
    };
    client.setColorTemperature = function (temperature) {
        return __awaiter(this, void 0, void 0, function () {
            var data;
            return __generator(this, function (_a) {
                data = { ct: { value: temperature } };
                this.callPUT("/state", data);
                return [2 /*return*/];
            });
        });
    };
    client.writeRawEffect = function (command, animType, loop, duration, animData) {
        return __awaiter(this, void 0, void 0, function () {
            var json;
            return __generator(this, function (_a) {
                json = {
                    "write": {
                        "command": command,
                        "duration": duration,
                        "animType": animType,
                        "animData": animData,
                        "loop": loop,
                        "palette": []
                    }
                };
                this.callPUT("/effects", json);
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
client.getAllPanelIds(true).then(function (iDs) { return sortedPanels = iDs; }); // zwischen Zeile für sortedPanels
//Beginn Server
function delay(ms) {
    return new Promise(function (resolve) { return setTimeout(resolve, ms); });
}
function glitter2() {
    var data = panels.map(function (entry) { return ({
        panelId: entry,
        color: client.convertHSVtoRGB({ hue: Math.random(), saturation: 1, value: 1 })
    }); });
    client.setPanelColors(data);
}
function sendColor(value) {
    client.setPanelColor(panels[Math.floor(Math.random() * panels.length)], client.convertHSVtoRGB({ hue: value / 360, saturation: 1, value: 1 }));
}
function shuffleArray(input) {
    var _a;
    var array = __spreadArrays(input);
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        _a = [array[j], array[i]], array[i] = _a[0], array[j] = _a[1];
    }
    return array;
}
function customEffects(PanelId, WertR, WertG, WertB, duration, mode, random) {
    var shuffeldPanel = [];
    if (random == true) {
        shuffeldPanel = shuffleArray(panels);
    }
    else {
        shuffeldPanel = sortedPanels;
    }
    var frames = 2;
    var animData;
    var panel_1 = 0;
    var oldR_1 = client.getPanelColor(shuffeldPanel[0]).red;
    var oldG_1 = client.getPanelColor(shuffeldPanel[0]).green;
    var oldB_1 = client.getPanelColor(shuffeldPanel[0]).blue;
    if (mode == "one") {
        if (PanelId > 0) {
            panel_1 = PanelId;
        }
        else {
            panel_1 = shuffeldPanel[0];
        }
        var anzahlPanel = 1;
        animData = anzahlPanel + " " + panel_1 + " " + frames + " " + oldR_1 + " " + oldG_1 + " " + oldB_1 + " 0 1 " + WertR + " " + WertG + " " + WertB + " 0 5";
    }
    else {
        var anzahlPanel = 14;
        var transitionTime = 5;
        var panel_1 = shuffeldPanel[0];
        var panel_2 = shuffeldPanel[1];
        var panel_3 = shuffeldPanel[2];
        var panel_4 = shuffeldPanel[3];
        var panel_5 = shuffeldPanel[4];
        var panel_6 = shuffeldPanel[5];
        var panel_7 = shuffeldPanel[6];
        var panel_8 = shuffeldPanel[7];
        var panel_9 = shuffeldPanel[8];
        var panel_10 = shuffeldPanel[9];
        var panel_11 = shuffeldPanel[10];
        var panel_12 = shuffeldPanel[11];
        var panel_13 = shuffeldPanel[12];
        var panel_14 = shuffeldPanel[13];
        var oldR_2 = client.getPanelColor(shuffeldPanel[1]).red;
        var oldG_2 = client.getPanelColor(shuffeldPanel[1]).green;
        var oldB_2 = client.getPanelColor(shuffeldPanel[1]).blue;
        var oldR_3 = client.getPanelColor(shuffeldPanel[2]).red;
        var oldG_3 = client.getPanelColor(shuffeldPanel[2]).green;
        var oldB_3 = client.getPanelColor(shuffeldPanel[2]).blue;
        var oldR_4 = client.getPanelColor(shuffeldPanel[3]).red;
        var oldG_4 = client.getPanelColor(shuffeldPanel[3]).green;
        var oldB_4 = client.getPanelColor(shuffeldPanel[3]).blue;
        var oldR_5 = client.getPanelColor(shuffeldPanel[4]).red;
        var oldG_5 = client.getPanelColor(shuffeldPanel[4]).green;
        var oldB_5 = client.getPanelColor(shuffeldPanel[4]).blue;
        var oldR_6 = client.getPanelColor(shuffeldPanel[5]).red;
        var oldG_6 = client.getPanelColor(shuffeldPanel[5]).green;
        var oldB_6 = client.getPanelColor(shuffeldPanel[5]).blue;
        var oldR_7 = client.getPanelColor(shuffeldPanel[6]).red;
        var oldG_7 = client.getPanelColor(shuffeldPanel[6]).green;
        var oldB_7 = client.getPanelColor(shuffeldPanel[6]).blue;
        var oldR_8 = client.getPanelColor(shuffeldPanel[7]).red;
        var oldG_8 = client.getPanelColor(shuffeldPanel[7]).green;
        var oldB_8 = client.getPanelColor(shuffeldPanel[7]).blue;
        var oldR_9 = client.getPanelColor(shuffeldPanel[8]).red;
        var oldG_9 = client.getPanelColor(shuffeldPanel[8]).green;
        var oldB_9 = client.getPanelColor(shuffeldPanel[8]).blue;
        var oldR_10 = client.getPanelColor(shuffeldPanel[9]).red;
        var oldG_10 = client.getPanelColor(shuffeldPanel[9]).green;
        var oldB_10 = client.getPanelColor(shuffeldPanel[9]).blue;
        var oldR_11 = client.getPanelColor(shuffeldPanel[10]).red;
        var oldG_11 = client.getPanelColor(shuffeldPanel[10]).green;
        var oldB_11 = client.getPanelColor(shuffeldPanel[10]).blue;
        var oldR_12 = client.getPanelColor(shuffeldPanel[11]).red;
        var oldG_12 = client.getPanelColor(shuffeldPanel[11]).green;
        var oldB_12 = client.getPanelColor(shuffeldPanel[11]).blue;
        var oldR_13 = client.getPanelColor(shuffeldPanel[12]).red;
        var oldG_13 = client.getPanelColor(shuffeldPanel[12]).green;
        var oldB_13 = client.getPanelColor(shuffeldPanel[12]).blue;
        var oldR_14 = client.getPanelColor(shuffeldPanel[13]).red;
        var oldG_14 = client.getPanelColor(shuffeldPanel[13]).green;
        var oldB_14 = client.getPanelColor(shuffeldPanel[13]).blue;
        animData = anzahlPanel + " " + panel_1 + " " + frames + " " + oldR_1 + " " + oldG_1 + " " + oldB_1 + " 0 " + transitionTime + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_2 + " " + frames + " " + oldR_2 + " " + oldG_2 + " " + oldB_2 + " 0 " + transitionTime * 2 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_3 + " " + frames + " " + oldR_3 + " " + oldG_3 + " " + oldB_3 + " 0 " + transitionTime * 3 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_4 + " " + frames + " " + oldR_4 + " " + oldG_4 + " " + oldB_4 + " 0 " + transitionTime * 4 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_5 + " " + frames + " " + oldR_5 + " " + oldG_5 + " " + oldB_5 + " 0 " + transitionTime * 5 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_6 + " " + frames + " " + oldR_6 + " " + oldG_6 + " " + oldB_6 + " 0 " + transitionTime * 6 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_7 + " " + frames + " " + oldR_7 + " " + oldG_7 + " " + oldB_7 + " 0 " + transitionTime * 7 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_8 + " " + frames + " " + oldR_8 + " " + oldG_8 + " " + oldB_8 + " 0 " + transitionTime * 8 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_9 + " " + frames + " " + oldR_9 + " " + oldG_9 + " " + oldB_9 + " 0 " + transitionTime * 9 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_10 + " " + frames + " " + oldR_10 + " " + oldG_10 + " " + oldB_10 + " 0 " + transitionTime * 10 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_11 + " " + frames + " " + oldR_11 + " " + oldG_11 + " " + oldB_11 + " 0 " + transitionTime * 11 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_12 + " " + frames + " " + oldR_12 + " " + oldG_12 + " " + oldB_12 + " 0 " + transitionTime * 12 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_13 + " " + frames + " " + oldR_13 + " " + oldG_13 + " " + oldB_13 + " 0 " + transitionTime * 13 + " " + WertR + " " + WertG + " " + WertB + " 0 5 " + panel_14 + " " + frames + " " + oldR_14 + " " + oldG_14 + " " + oldB_14 + " 0 " + transitionTime * 14 + " " + WertR + " " + WertG + " " + WertB + " 0 5";
        //PanelAnzahl; PanelId; Anzahl der Frame; RGBW Werte; transition Time (global); (RGBW-Wert; Transition Time (lokal)) --> 2 frame; [PanelId, Anzahl...] --> 2 Panel
    }
    client.writeRawEffect("displayTemp", "custom", false, duration, animData);
}
function smothEffect(color, fadeColor, duration) {
    var frames = 3;
    var animData;
    var anzahlPanel = 14;
    var transitionTime = 5;
    var fadeColor = fadeColor / 360;
    var colorRGB = color / 360;
    var fadeR = client.convertHSVtoRGB({ hue: fadeColor, saturation: 1, value: 1 }).red;
    var fadeG = client.convertHSVtoRGB({ hue: fadeColor, saturation: 1, value: 1 }).green;
    var fadeB = client.convertHSVtoRGB({ hue: fadeColor, saturation: 1, value: 1 }).blue;
    var colorR = client.convertHSVtoRGB({ hue: colorRGB, saturation: 1, value: 1 }).red;
    var colorG = client.convertHSVtoRGB({ hue: colorRGB, saturation: 1, value: 1 }).green;
    var colorB = client.convertHSVtoRGB({ hue: colorRGB, saturation: 1, value: 1 }).blue;
    animData = anzahlPanel + " " + sortedPanels[0] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 1 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[1] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 2 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[2] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 3 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[3] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 4 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[4] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 5 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[5] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 6 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[6] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 7 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[7] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 8 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[8] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 9 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[9] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 10 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[10] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 11 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[11] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 12 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[12] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 13 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10 " + sortedPanels[13] + " " + frames + " " + fadeR + " " + fadeG + " " + fadeB + " 0 " + transitionTime * 14 + " " + fadeR + " " + fadeG + " " + fadeB + " 0 10 " + colorR + " " + colorG + " " + colorB + " 0 10";
    client.writeRawEffect("displayTemp", "custom", false, duration, animData);
}
function alleKachelnFärben(color) {
    var data = panels.map(function (entry) { return ({
        panelId: entry,
        color: client.convertHSVtoRGB({ hue: color / 360, saturation: 1, value: 1 })
    }); });
    client.setPanelColors(data);
}
function eineKachelFärben(PanelId, color) {
    var data = PanelId.map(function (entry) { return ({
        panelId: entry,
        color: client.convertHSVtoRGB({ hue: color / 360, saturation: 1, value: 1 })
    }); });
    client.setPanelColors(data);
}
function specialShapetypeFärben(color, shapetype) {
    var panelArray = [];
    if (shapetype == "large") {
        panelArray = largePanels;
    }
    else if (shapetype == "small_all") {
        panelArray = smallPanels_all;
    }
    else if (shapetype == "small_reihen") {
        panelArray = smallPanels_reihe;
    }
    else {
        panelArray = specialPanels;
    }
    var data = panelArray.map(function (entry) { return ({
        panelId: entry,
        color: client.convertHSVtoRGB({ hue: color / 360, saturation: 1, value: 1 })
    }); });
    client.setPanelColors(data);
}
//Start function mit delay option 
function start() {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    client.setState(true);
                    client.setBrightness(100);
                    alleKachelnFärben(120);
                    return [4 /*yield*/, delay(1000)];
                case 1:
                    _a.sent();
                    smothEffect(100, 200, 12);
                    return [2 /*return*/];
            }
        });
    });
}
start(); //erste Aufruf
//Dokumentation Client:
//
//testi: consolen output
//buildBaseRequestAddress(): builded iwas aus ip und authtoken
//convertHsvToRgb(hueWert, 1, 1): ändert Hsv typen und Werte in RGB
//callGet(relativePath): selbe wie in Postmann
//callPut(relativePath, body): Put wie in Postmann
//getAllPanelInfo(): gibt die Übersicht aus allen Infos, wie bei Postmann
//getPanelColor(panelId): greift auf ein Internes Array zu und überprüft den Farbwerte für die Id
//setPanelColors(ColoredPanel[]): setzt das angegebene Pannel auf die entsprechende Farbe
//setPanelColor(ColoredPanel[]): extrener Aufruf von setPanelColors
//setBrightness(number): setzt die Brightniss aller Kacheln
//setState(boolean): power of / on im client
//setHue(): setzt alle kacheln auf die Farbe; aber ohne sie zu speichern und ohne saturation
//setColorTemperature(number): speziellen Weißton aufrufen
//writeRawEffect(...): client Aufruf von eigenem Effect übermitteln
//Dokumentation Server:
//
//delay: um Verzögerungen im Server zu ermöglichen
//glitter: alle Kacheln zufällig färben
//sendColor(hueWert): färbt eine zufällig Kachel in der Farbe
//shuffleArray(Array): ändert die Werte im Array zufällig
//CustomEffects(pannelId;RGB, duration, mode): spielt einen eigen Effect ab; genaueres siehe im Effect
//smoothEffect(color, fade, duration): färbt die Panels von oben nach unten mit einem Effect + Übergang
//allekachelnFärben(hueWert): Färbt alle kacheln in der angegeben Farbe
//eineKachelFärben(panelId[], hueWert): färbt die angegebene kacheln in der Farbe, nicht schnell hintereinander ausführen
//specialShapetypeFärben(color, shapeType): fräbt eine bestimte Sorte an Pannel
//BeispielAufrufe:
//await delay(1000);
//glitter2();
//sendColor2(0)
//shuffleArray(panels)
//customEffects(0, 0, 229, 255, 5, 'all')
//smothEffect(0, 220, 12)
//alleKachelnFärben(110)
//eineKachelFärben([428], 20)
//specialShapetypeFärben(220, "special")

import { debug } from 'console';
import fetch from 'node-fetch';
import { on, send } from 'process';
import { collapseTextChangeRangesAcrossMultipleVersions } from 'typescript';

const panels = [19846, 11043, 43792, 2785, 52805, 58649, 56421, 5069, 62964, 12501, 29466, 4776, 43439, 428]
const largePanels = [11043, 19846, 2785, 43792]
const smallPanels_all = [52805, 58649, 56421, 5069, 62964, 12501, 29466, 4776, 43439, 428]
const smallPanels_reihe = [62964, 12501, 29466, 4776, 43439, 428]
const specialPanels = [56421, 5069, 58649, 52805]
let sortedPanels: number[] = []
const address = "http://192.168.178.68:16021/api/v1/gEnntf1ygTGNOq0b2fxW8mpsLLdc1ymi/effects"


interface Color { red: number, green: number, blue: number }
interface ColoredPanel { panelId: number, color: Color }



//Beginn Client

class client {
    private static ipAddress = "192.168.178.68"
    private static authToken = "gEnntf1ygTGNOq0b2fxW8mpsLLdc1ymi"
    private static defaultPort = 16021
    private static colors: Map<number, Color> = new Map<number, Color>();

    static testi() {
        console.log("halihalo");

    }

    static async getAllPanelIds(sorted: boolean): Promise<Array<number>> {
        const response = await this.getAllPanelInfo()

        if (response.status !== 200) {
            return []
        }

        const json = await response.json()
        const positionData: Array<any> = json.panelLayout?.layout?.positionData
        const panels = sorted ? positionData.sort((a, b) => a.y - b.y) : positionData
        const panelIds = panels?.map((entry: any) => entry.panelId).filter((entry: number) => entry !== 0)

        return panelIds
    }

    private static buildBaseRequestAddress(ipAddress: string, authToken: string) {
        return `http://${ipAddress}:${client.defaultPort}/api/v1/${authToken}`
    }

    static convertHSVtoRGB(color: { hue: number, saturation: number, value: number }): Color {
        // based on: https://stackoverflow.com/questions/17242144/javascript-convert-hsb-hsv-color-to-rgb-accurately
        let h = color.hue;
        let s = color.saturation;
        let v = color.value;
        let r, g, b, i, f, p, q, t;
        i = Math.floor(h * 6);
        f = h * 6 - i;
        p = v * (1 - s);
        q = v * (1 - f * s);
        t = v * (1 - (1 - f) * s);
        switch (i % 6) {
            case 0: r = v, g = t, b = p; break;
            case 1: r = q, g = v, b = p; break;
            case 2: r = p, g = v, b = t; break;
            case 3: r = p, g = q, b = v; break;
            case 4: r = t, g = p, b = v; break;
            case 5: r = v, g = p, b = q; break;
            default: r = 0, g = 0, b = 0; break;
        }
        return {
            red: Math.round(r * 255),
            green: Math.round(g * 255),
            blue: Math.round(b * 255)
        };
    }

    static async callGET(relativePath: String) {
        return fetch(client.buildBaseRequestAddress(this.ipAddress, this.authToken) + relativePath,
            { method: 'GET' })
    }

    static async callPUT(relativePath: String, body: any) {
        return fetch(client.buildBaseRequestAddress(this.ipAddress, this.authToken) + relativePath,
            {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(body),
            })
    }

    static async getAllPanelInfo() {
        return this.callGET("")
    }

    static getPanelColor(panelId: number) {
        return this.colors.get(panelId)
    }

    static async setPanelColors(data: ColoredPanel[]) {
        data.forEach(panel => this.colors.set(panel.panelId, panel.color));

        if (data.length >= 1) {
            const animData = `${data.length}` +
                data
                    .map((entry) => ` ${entry.panelId} 1 ${entry.color.red} ${entry.color.green} ${entry.color.blue} 0 1`)
                    .join("")

            const json = {
                "write":
                {
                    "command": "display",
                    "animType": "static",
                    "animData": animData,
                    "loop": false,
                    "palette": []
                }
            }

            this.callPUT("/effects", json)
        }
    }

    static async setPanelColor(panelId: number, color: Color) {
        this.setPanelColors([{ panelId: panelId, color: color }]);
    }

    static async setBrightness(level: number) {
        const data = { brightness: { value: level } };
        this.callPUT("/state", data);
    }

    static async setState(on: boolean) {
        const data = { on: { value: on } }
        this.callPUT("/state", data);
    }

    static async setHue(hue: number) {
        const data = { hue: { value: hue } }
        this.callPUT("/state", data);
    }

    static async setSaturation(sat: number) {
        const data = { sat: { value: sat } }
        this.callPUT("/state", data);
    }

    static async setColorTemperature(temperature: number) {
        const data = { ct: { value: temperature } }
        this.callPUT("/state", data);
    }

    static async writeRawEffect(
        command: "add" | "display" | "displayTemp", animType: "static" | "custom", loop: boolean, duration: number, animData) {

        const json = {
            "write":
            {
                "command": command,
                "duration": duration,
                "animType": animType,
                "animData": animData,
                "loop": loop,
                "palette": []
            }
        }

        this.callPUT("/effects", json)

    }
}

client.getAllPanelIds(true).then(iDs => sortedPanels = iDs) // zwischen Zeile für sortedPanels
//Beginn Server

function delay(ms: number) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function glitter2() {
    const data = panels.map(entry => ({
        panelId: entry,
        color: client.convertHSVtoRGB(
            { hue: Math.random(), saturation: 1, value: 1 })
    }))
    client.setPanelColors(data);
}

function sendColor(value: number) {
    client.setPanelColor(panels[Math.floor(Math.random() * panels.length)],
        client.convertHSVtoRGB(
            { hue: value / 360, saturation: 1, value: 1 }
        )
    )
}

function shuffleArray(input: Array<number>) {
    const array = [...input];
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function customEffects(PanelId: number, WertR: number, WertG: Number, WertB: number, duration: number, mode: "one" | "all", random: boolean) {
    var shuffeldPanel: number[] = []
    if (random == true) {
        shuffeldPanel = shuffleArray(panels)
    } else {
        shuffeldPanel = sortedPanels
    }
    const frames = 2
    var animData
    var panel_1 = 0;

    const oldR_1 = client.getPanelColor(shuffeldPanel[0]).red
    const oldG_1 = client.getPanelColor(shuffeldPanel[0]).green
    const oldB_1 = client.getPanelColor(shuffeldPanel[0]).blue

    if (mode == "one") {

        if (PanelId > 0) {
            panel_1 = PanelId
        } else {
            panel_1 = shuffeldPanel[0]
        }

        const anzahlPanel = 1

        animData = `${anzahlPanel} ${panel_1} ${frames} ${oldR_1} ${oldG_1} ${oldB_1} 0 1 ${WertR} ${WertG} ${WertB} 0 5`

    } else {
        const anzahlPanel = 14
        const transitionTime = 5
        var panel_1 = shuffeldPanel[0]
        var panel_2 = shuffeldPanel[1]
        const panel_3 = shuffeldPanel[2]
        const panel_4 = shuffeldPanel[3]
        const panel_5 = shuffeldPanel[4]
        const panel_6 = shuffeldPanel[5]
        const panel_7 = shuffeldPanel[6]
        const panel_8 = shuffeldPanel[7]
        const panel_9 = shuffeldPanel[8]
        const panel_10 = shuffeldPanel[9]
        const panel_11 = shuffeldPanel[10]
        const panel_12 = shuffeldPanel[11]
        const panel_13 = shuffeldPanel[12]
        const panel_14 = shuffeldPanel[13]

        const oldR_2 = client.getPanelColor(shuffeldPanel[1]).red
        const oldG_2 = client.getPanelColor(shuffeldPanel[1]).green
        const oldB_2 = client.getPanelColor(shuffeldPanel[1]).blue

        const oldR_3 = client.getPanelColor(shuffeldPanel[2]).red
        const oldG_3 = client.getPanelColor(shuffeldPanel[2]).green
        const oldB_3 = client.getPanelColor(shuffeldPanel[2]).blue

        const oldR_4 = client.getPanelColor(shuffeldPanel[3]).red
        const oldG_4 = client.getPanelColor(shuffeldPanel[3]).green
        const oldB_4 = client.getPanelColor(shuffeldPanel[3]).blue

        const oldR_5 = client.getPanelColor(shuffeldPanel[4]).red
        const oldG_5 = client.getPanelColor(shuffeldPanel[4]).green
        const oldB_5 = client.getPanelColor(shuffeldPanel[4]).blue

        const oldR_6 = client.getPanelColor(shuffeldPanel[5]).red
        const oldG_6 = client.getPanelColor(shuffeldPanel[5]).green
        const oldB_6 = client.getPanelColor(shuffeldPanel[5]).blue

        const oldR_7 = client.getPanelColor(shuffeldPanel[6]).red
        const oldG_7 = client.getPanelColor(shuffeldPanel[6]).green
        const oldB_7 = client.getPanelColor(shuffeldPanel[6]).blue

        const oldR_8 = client.getPanelColor(shuffeldPanel[7]).red
        const oldG_8 = client.getPanelColor(shuffeldPanel[7]).green
        const oldB_8 = client.getPanelColor(shuffeldPanel[7]).blue

        const oldR_9 = client.getPanelColor(shuffeldPanel[8]).red
        const oldG_9 = client.getPanelColor(shuffeldPanel[8]).green
        const oldB_9 = client.getPanelColor(shuffeldPanel[8]).blue

        const oldR_10 = client.getPanelColor(shuffeldPanel[9]).red
        const oldG_10 = client.getPanelColor(shuffeldPanel[9]).green
        const oldB_10 = client.getPanelColor(shuffeldPanel[9]).blue

        const oldR_11 = client.getPanelColor(shuffeldPanel[10]).red
        const oldG_11 = client.getPanelColor(shuffeldPanel[10]).green
        const oldB_11 = client.getPanelColor(shuffeldPanel[10]).blue

        const oldR_12 = client.getPanelColor(shuffeldPanel[11]).red
        const oldG_12 = client.getPanelColor(shuffeldPanel[11]).green
        const oldB_12 = client.getPanelColor(shuffeldPanel[11]).blue

        const oldR_13 = client.getPanelColor(shuffeldPanel[12]).red
        const oldG_13 = client.getPanelColor(shuffeldPanel[12]).green
        const oldB_13 = client.getPanelColor(shuffeldPanel[12]).blue

        const oldR_14 = client.getPanelColor(shuffeldPanel[13]).red
        const oldG_14 = client.getPanelColor(shuffeldPanel[13]).green
        const oldB_14 = client.getPanelColor(shuffeldPanel[13]).blue

        animData = `${anzahlPanel} ${panel_1} ${frames} ${oldR_1} ${oldG_1} ${oldB_1} 0 ${transitionTime} ${WertR} ${WertG} ${WertB} 0 5 ${panel_2} ${frames} ${oldR_2} ${oldG_2} ${oldB_2} 0 ${transitionTime * 2} ${WertR} ${WertG} ${WertB} 0 5 ${panel_3} ${frames} ${oldR_3} ${oldG_3} ${oldB_3} 0 ${transitionTime * 3} ${WertR} ${WertG} ${WertB} 0 5 ${panel_4} ${frames} ${oldR_4} ${oldG_4} ${oldB_4} 0 ${transitionTime * 4} ${WertR} ${WertG} ${WertB} 0 5 ${panel_5} ${frames} ${oldR_5} ${oldG_5} ${oldB_5} 0 ${transitionTime * 5} ${WertR} ${WertG} ${WertB} 0 5 ${panel_6} ${frames} ${oldR_6} ${oldG_6} ${oldB_6} 0 ${transitionTime * 6} ${WertR} ${WertG} ${WertB} 0 5 ${panel_7} ${frames} ${oldR_7} ${oldG_7} ${oldB_7} 0 ${transitionTime * 7} ${WertR} ${WertG} ${WertB} 0 5 ${panel_8} ${frames} ${oldR_8} ${oldG_8} ${oldB_8} 0 ${transitionTime * 8} ${WertR} ${WertG} ${WertB} 0 5 ${panel_9} ${frames} ${oldR_9} ${oldG_9} ${oldB_9} 0 ${transitionTime * 9} ${WertR} ${WertG} ${WertB} 0 5 ${panel_10} ${frames} ${oldR_10} ${oldG_10} ${oldB_10} 0 ${transitionTime * 10} ${WertR} ${WertG} ${WertB} 0 5 ${panel_11} ${frames} ${oldR_11} ${oldG_11} ${oldB_11} 0 ${transitionTime * 11} ${WertR} ${WertG} ${WertB} 0 5 ${panel_12} ${frames} ${oldR_12} ${oldG_12} ${oldB_12} 0 ${transitionTime * 12} ${WertR} ${WertG} ${WertB} 0 5 ${panel_13} ${frames} ${oldR_13} ${oldG_13} ${oldB_13} 0 ${transitionTime * 13} ${WertR} ${WertG} ${WertB} 0 5 ${panel_14} ${frames} ${oldR_14} ${oldG_14} ${oldB_14} 0 ${transitionTime * 14} ${WertR} ${WertG} ${WertB} 0 5`
        //PanelAnzahl; PanelId; Anzahl der Frame; RGBW Werte; transition Time (global); (RGBW-Wert; Transition Time (lokal)) --> 2 frame; [PanelId, Anzahl...] --> 2 Panel
    }

    client.writeRawEffect("displayTemp", "custom", false, duration, animData)
}

function smothEffect(color: number, fadeColor: number, duration: number) {
    const frames = 3
    var animData
    const anzahlPanel = 14
    const transitionTime = 5
    var fadeColor = fadeColor / 360
    const colorRGB = color / 360

    const fadeR = client.convertHSVtoRGB({hue: fadeColor, saturation: 1, value: 1}).red
    const fadeG = client.convertHSVtoRGB({hue: fadeColor, saturation: 1, value: 1}).green
    const fadeB = client.convertHSVtoRGB({hue: fadeColor, saturation: 1, value: 1}).blue

    const colorR = client.convertHSVtoRGB({hue: colorRGB, saturation: 1, value: 1}).red
    const colorG = client.convertHSVtoRGB({hue: colorRGB, saturation: 1, value: 1}).green
    const colorB = client.convertHSVtoRGB({hue: colorRGB, saturation: 1, value: 1}).blue


    animData = `${anzahlPanel} ${sortedPanels[0]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*1} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[1]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*2} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[2]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*3} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[3]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*4} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[4]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*5} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[5]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*6} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[6]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*7} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[7]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*8} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[8]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*9} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[9]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*10} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[10]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*11} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[11]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*12} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[12]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*13} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10 ${sortedPanels[13]} ${frames} ${fadeR} ${fadeG} ${fadeB} 0 ${transitionTime*14} ${fadeR} ${fadeG} ${fadeB} 0 10 ${colorR} ${colorG} ${colorB} 0 10`

    client.writeRawEffect("displayTemp", "custom", false, duration, animData)
}

function alleKachelnFärben(color: number) {
    const data = panels.map(entry => ({
        panelId: entry,
        color: client.convertHSVtoRGB(
            { hue: color / 360, saturation: 1, value: 1 })
    }))
    client.setPanelColors(data);
}

function eineKachelFärben(PanelId: number[], color: number) {
    const data = PanelId.map(entry => ({
        panelId: entry,
        color: client.convertHSVtoRGB(
            { hue: color / 360, saturation: 1, value: 1 })
    }))
    client.setPanelColors(data);
}

function specialShapetypeFärben(color: number, shapetype: "large" | "small_all" | "small_reihen" | "special"){
    let panelArray = []

    if(shapetype == "large"){
        panelArray = largePanels
    }else if (shapetype == "small_all"){
        panelArray = smallPanels_all
    }else if (shapetype == "small_reihen"){
        panelArray = smallPanels_reihe
    }else {
        panelArray = specialPanels
    }

    const data = panelArray.map(entry => ({
        panelId: entry,
        color: client.convertHSVtoRGB(
            { hue: color / 360, saturation: 1, value: 1 })
    }))
    client.setPanelColors(data);
}


//Start function mit delay option 
async function start() {
    client.setState(true);
    client.setBrightness(100);
    alleKachelnFärben(120)
    await delay(1000)
    smothEffect(100, 200, 12)
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
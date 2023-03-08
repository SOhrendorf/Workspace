import { debug } from 'console';
import fetch from 'node-fetch';

const panels = [19846, 11043, 43792, 2785, 52805, 58649, 56421, 5069, 62964, 12501, 29466, 4776, 43439, 428]
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


//Beginn Server

function glitter2() {
    const data = panels.map(entry => ({
        panelId: entry,
        color: client.convertHSVtoRGB(
            { hue: Math.random(), saturation: 1, value: 1 })
    }))
    client.setPanelColors(data);
}

function sendColor2(value: number) {
    client.setPanelColor(panels[Math.floor(Math.random() * panels.length)],
        client.convertHSVtoRGB(
            { hue: value / 360, saturation: 1, value: 1 }
        )
    )
}

function power(value: boolean) {
    client.setState(value)
}

function shuffleArray(input: Array<number>) {
    const array = [...input];
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function customEffects(anzahlPanel: number, WertR: number, WertG: Number, WertB: number, duration: number) {
    const shuffeldPanel = shuffleArray(panels)
    const frames = 2
    const panel_1 = shuffeldPanel[0]
    const panel_2 = shuffeldPanel[1]
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


    const array = panels
    for (let i = panels.length - 1; i > 0; i--) {
        const newId = array[i]
    }
    const animData = `${anzahlPanel} ${panel_1} ${frames} ${WertR} ${WertG} ${WertB} 0 1 0 0 225 0 5 ${panel_2} ${frames} ${WertR} ${WertG} ${WertB} 0 10 0 0 225 0 5 ${panel_3} ${frames} ${WertR} ${WertG} ${WertB} 0 15 0 0 225 0 5 ${panel_4} ${frames} ${WertR} ${WertG} ${WertB} 0 20 0 0 225 0 5`
    //PanelAnzahl; PanelId; Anzahl der Frame; RGBW Werte; transition Time (global); (RGBW-Wert; Transition Time (lokal)) --> 2 frame; [PanelId, Anzahl...] --> 2 Panel

    client.writeRawEffect("displayTemp", "custom", false, duration, animData)

}



//Aufrufe
client.setState(true);
client.setBrightness(100);
//client.testi();
//glitter2();
//customEffects(4, 111, 100, 0, 5)
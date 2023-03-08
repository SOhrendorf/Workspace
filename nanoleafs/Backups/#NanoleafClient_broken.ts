import fetch from 'node-fetch';
import { response } from "express";
import { debug } from 'console';

export interface Color { red: number, green: number, blue: number }
export interface ColoredPanel { panelId: number, color: Color }

export class NanoleafClient {

    private static defaultPort = 16021

    private static buildBaseRequestAddress(ipAddress: string, authToken: string) {
        return `http://${ipAddress}:${NanoleafClient.defaultPort}/api/v1/${authToken}`
    }

    static async printAuthKey(ipAddress: string) {

        const errorMessage = "Received error while requesting nanoleaf auth token. Make sure to press the 'on' button for 5 seconds before executing this command."

        try {
            const response = await fetch(`http://${ipAddress}:${this.defaultPort}/api/v1/new`,
                { method: 'POST' })

            const json = await response.json()
            if (json.auth_token) {
                const authToken = json.auth_token
                console.log(`Your Auth Token is: '${authToken}'.`);
            }
        } catch (error) {
            console.log(errorMessage);
        }
    }

    static async verifyConnection(ipAddress: string, authToken: string) {
        const response = await fetch(NanoleafClient.buildBaseRequestAddress(ipAddress, authToken),
            { method: 'GET' })
        return response.status === 200
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

    private colors: Map<number, Color> = new Map<number, Color>();

    constructor(private ipAddress: string, private authToken: string) {
        NanoleafClient.verifyConnection(ipAddress, authToken).then(response => {
            if (response) {
                console.log("Connected to Nanoleafs successfully!");
            } else {
                console.log("Unable to connect to Nanoleafs. Please check your credentials.");
            }
        })
    }

    private async callGET(relativePath: String) {
        return fetch(NanoleafClient.buildBaseRequestAddress(this.ipAddress, this.authToken) + relativePath,
            { method: 'GET' })
    }

    private async callPUT(relativePath: String, body: any) {
        return fetch(NanoleafClient.buildBaseRequestAddress(this.ipAddress, this.authToken) + relativePath,
            {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(body),
            })
    }

    async getAllPanelInfo() {
        return this.callGET("")
    }

    async getAllPanelIDs(): Promise<Array<number>> {
        const response = await this.getAllPanelInfo()

        if (response.status !== 200) {
            return []
        }

        const json = await response.json();
        const panelIDs = json.panelLayout?.layout?.positionData
            ?.map((entry: any) => entry.panelId)
            .filter((entry: number) => entry !== 0);

        return panelIDs;
    }

    async setPanelColors(data: ColoredPanel[]){
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

    async testi(){
        console.log("ich lebe ja doch");
    }
}

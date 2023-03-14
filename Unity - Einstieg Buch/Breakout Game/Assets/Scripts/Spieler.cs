using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Spieler : MonoBehaviour
{
    public GameObject ziegelEinsPrefab;
    public GameObject zeigelZweiPrefab;
    public GameObject ziegelDreiPrefab;
    public GameObject ball;
    public Ball ballKlasse;
    Rigidbody2D ballRB;
    readonly float eingabeFaktor = 10;
    public bool ballUnterwegs = false;
    public Text infoAnzeige;
    public Text zeitAnzeige;
    public Text zeitAnzeigeAlt;
    public Text lebenAnzeige;
    public Text punkteAnzeige;
    public bool spielGestartet = false;
    public float spielZeitStart;

    // Start is called before the first frame update
    void Start()
    {
        ballRB = ball.GetComponent<Rigidbody2D>();
        ZiegelErzeugen();
        zeitAltLaden();
    }

    // Update is called once per frame
    void Update()
    {
        float xEingabe = Input.GetAxis("Horizontal");
        float yEingabe = Input.GetAxis("Vertical");

        if (!ballUnterwegs && yEingabe > 0)
        {
            if (!spielGestartet)
            {
                ballRB.AddForce(new Vector2(240, 160));
            }
            ballRB.velocity = new Vector2(ballKlasse.speedx, ballKlasse.speedy);
            ballUnterwegs = true;
            if (!spielGestartet)
            {
                spielGestartet = true;
                spielZeitStart = Time.time;
            }
            infoAnzeige.text = "";
        }
        if (ballUnterwegs)
        {
            float xNeu = transform.position.x + xEingabe * eingabeFaktor * Time.deltaTime;
            if (xNeu < -6)
            {
                xNeu = -6;
            }
            if (xNeu > 6)
            {
                xNeu = 6;
            }
            transform.position = new Vector3(xNeu, transform.position.y, 0);
        }

        if (spielGestartet)
        {
            zeitAnzeige.text = string.Format("Zeit: {0,6:##0.0} sec.", Time.time - spielZeitStart);
        }
    }

    void ZiegelErzeugen()
    {
        for (int x = 1; x <= 10; x++)
        {
            for (int y = 1; y <= 5; y++)
            {
                GameObject ziegel;
                int zufall = Random.Range(1, 4);
                switch (zufall)
                {
                    case 1: ziegel = ziegelEinsPrefab; break;
                    case 2: ziegel = zeigelZweiPrefab; break;
                    default: ziegel = ziegelDreiPrefab; break;
                }
                Instantiate(ziegel, new Vector3(x * 1.2f - 6.6f, y * 0.75f - 0.25f, 0), Quaternion.identity);
            }
        }
    }

    void zeitAltLaden()
    {
        float zeitAlt = 0;
        if (PlayerPrefs.HasKey("zeitAlt"))
        {
            zeitAlt = PlayerPrefs.GetFloat("zeitAlt");
        }
        zeitAnzeigeAlt.text = string.Format("Alt: {0,6:#0.0} sec.", zeitAlt);
    }

    public void SpielNeuButton_Click()
    {
        if (spielGestartet)
        {
            return;
        }
        ballKlasse.anzahlLeben = 5;
        ballKlasse.anzahlPunkte = 0;
        punkteAnzeige.text = "Punkte : 0";
        lebenAnzeige.text = "Leben: 5";
        zeitAnzeige.text = "Zeit: 0.0 sec.";
        infoAnzeige.text = "Schiesse den Ball mt Pfeil-Aufwärts ab. \n"
        + "Bewege den schwarzen Speiler mit Pfeil-Links und Pfeil-Rechts. \n"
        + "Zerstöre Ziegel und vermeide den roten Boden.";

        zeitAltLaden();
        ZiegelErzeugen();
        AufStartpunkt();
    }

    public void AufStartpunkt()
    {
        gameObject.SetActive(true);
        transform.position = new Vector3(0, -4.55f, 0);

        ball.SetActive(true);
        ball.transform.position = new Vector3(0, -4.1f, 0);
    }

    public void AnwendungEndeButton_Click()
    {
        if (spielGestartet)
        {
            Application.Quit();
        }
    }
}

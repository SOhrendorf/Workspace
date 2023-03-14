using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Ball : MonoBehaviour
{
    public GameObject spieler;
    public AudioClip kollisionZiegelAudio;
    public int anzahlPunkte = 0;
    Rigidbody2D rb;
    public Spieler spielerKlasse;
    public int anzahlLeben = 5;
    public Text punkteAnzeige;
    public Text lebenAnzeige;
    public Text infoAnzeige;
    public float speedx;
    public float speedy;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnCollisionEnter2D(Collision2D coll)
    {
        GameObject anderesObjekt = coll.gameObject;
        if (anderesObjekt.CompareTag("Ziegel"))
        {
            AudioSource.PlayClipAtPoint(kollisionZiegelAudio, transform.position);
            anzahlPunkte++;
            punkteAnzeige.text = "Punkte: " + anzahlPunkte;

            if (anzahlPunkte < 50)
            {
                Destroy(anderesObjekt, 0.1f);
                if (anzahlPunkte % 10 == 0)
                {
                    rb.velocity = new Vector2(rb.velocity.x * 1.1f, rb.velocity.y * 1.1f);
                }
                Debug.Log("Punkte: " + anzahlPunkte + " Gescwindigkeit: " + rb.velocity.magnitude);
            }
            else
            {
                Destroy(anderesObjekt);
                spieler.SetActive(false);
                gameObject.SetActive(false);
                // Debug.Log("Du hast gewonnen.");
                float spielZeitAktuell = Time.time - spielerKlasse.spielZeitStart;
                infoAnzeige.text = string.Format("Du hast gewonnen, in {0,6:##0.0} sec.", spielZeitAktuell);
                spielerKlasse.spielGestartet = false;
                PlayerPrefs.SetFloat("zeitAlt", spielZeitAktuell);
                PlayerPrefs.Save();
            }
        }
        else if (anderesObjekt.CompareTag("BodenMitte"))
        {
            anzahlLeben--;

            speedx = rb.velocity.x;
            speedy = rb.velocity.y;

            spieler.SetActive(false);
            gameObject.SetActive(false);
            spielerKlasse.ballUnterwegs = false;

            lebenAnzeige.text = "Leben: " + anzahlLeben;

            if (anzahlLeben >= 1)
            {
                Invoke(nameof(NaechstesLeben), 1);
                // Debug.Log("Leben: " + anzahlLeben);
                infoAnzeige.text = "Du hast nur noch  " + anzahlLeben + " Leben!";
            }
            else
            {
                // Debug.Log("Du hast verloren");
                infoAnzeige.text = "Du hast verloren!";
                spielerKlasse.spielGestartet = false;
            }
        }
    }

    void NaechstesLeben()
    {
        infoAnzeige.text = "";
        spielerKlasse.AufStartpunkt();
    }
}

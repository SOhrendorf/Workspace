using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Ball : MonoBehaviour
{
    public GameObject hEins, hZwei, hDrei, bueschelPrefab;
    public int AnzahlBueschel;
    Rigidbody2D rb;
    bool aufschlagRechts;
    public GameObject spielerLinks;
    public GameObject spielerRechts;
    readonly float eingabeFaktor = 10;
    bool toggleMaulwurf = true;
    int punkteLinks = 0;
    int punkteRechts = 0;
    public Text punkteLinzsAnzeige;
    public Text punkteAnzeigeRechts;
    public InputField GweinnPunkte;
    public AudioClip Aufschlag;
    public AudioClip prallen;
    public AudioClip Punkt;
    public AudioClip movment;

    void Start()
    {
        for (AnzahlBueschel = 0; AnzahlBueschel < 100; AnzahlBueschel++)
        {
            rb = GetComponent<Rigidbody2D>();
            Instantiate(bueschelPrefab, new Vector3(Random.Range(-8.0f, 8.0f), Random.Range(-4.5f, 4.5f), 0), Quaternion.identity);
            HindernissSetzen();
            if (Random.Range(0, 10) <= 5)
            {
                transform.position = new Vector3(7.99f, 0, 0);
                aufschlagRechts = true;
            }
            else
            {
                transform.position = new Vector3(-7.99f, 0, 0);
                aufschlagRechts = false;
            }
        }
    }

    void Update()
    {
        if (rb.velocity.x == 0)
        {
            if (aufschlagRechts && Input.GetKeyDown(KeyCode.LeftArrow))
            {
                if (GweinnPunkte.text == "")
                {
                    GweinnPunkte.text = "5";
                }
                GweinnPunkte.readOnly = true;
                rb.AddForce(new Vector2(-200, 300));
                AudioSource.PlayClipAtPoint(Aufschlag, transform.position);
            }
            else if (!aufschlagRechts && Input.GetKeyDown(KeyCode.D))
            {
                if (GweinnPunkte.text == "")
                {
                    GweinnPunkte.text = "5";
                }
                GweinnPunkte.readOnly = true;
                rb.AddForce(new Vector2(200, 300));
                AudioSource.PlayClipAtPoint(Aufschlag, transform.position);
            }
        }
        else if (Input.GetKey(KeyCode.UpArrow))
        {
            float yNeu = spielerRechts.transform.position.y + eingabeFaktor * Time.deltaTime;
            if (yNeu > 3.5f)
            {
                yNeu = 3.5f;
            }
            spielerRechts.transform.position = new Vector3(8.44f, yNeu, 0);
        }
        else if (Input.GetKey(KeyCode.DownArrow))
        {
            float yNeu = spielerRechts.transform.position.y - eingabeFaktor * Time.deltaTime;
            if (yNeu < -3.5f)
            {
                yNeu = -3.5f;
            }
            spielerRechts.transform.position = new Vector3(8.44f, yNeu, 0);
        }
        else if (Input.GetKeyDown(KeyCode.LeftArrow))
        {
            spielerRechts.transform.Translate(-0.3f, 0, 0);
            AudioSource.PlayClipAtPoint(movment, transform.position);
            Invoke(nameof(SpielerRechtsZurueck), 0.2f);
        }
        if (Input.GetKey(KeyCode.W))
        {
            float yNeu = spielerLinks.transform.position.y + eingabeFaktor * Time.deltaTime;
            if (yNeu > 3.5f)
            {
                yNeu = 3.5f;
            }
            spielerLinks.transform.position = new Vector3(-8.44f, yNeu, 0);
        }
        else if (Input.GetKey(KeyCode.S))
        {
            float yNeu = spielerLinks.transform.position.y - eingabeFaktor * Time.deltaTime;
            if (yNeu < -3.5f)
            {
                yNeu = -3.5f;
            }
            spielerLinks.transform.position = new Vector3(-8.44f, yNeu, 0);
        }
        else if (Input.GetKeyDown(KeyCode.D))
        {
            spielerLinks.transform.Translate(0.3f, 0, 0);
            AudioSource.PlayClipAtPoint(movment, transform.position);
            Invoke(nameof(SpielerLinksZurueck), 0.2f);
        }
    }

    void HindernissSetzen()
    {
        hEins.transform.position = new Vector3(Random.Range(-3.0f, 3.0f), Random.Range(-3.5f, 3.5f), 0);

        do
        {
            hZwei.transform.position = new Vector3(Random.Range(-3.0f, 3.0f), Random.Range(-3.5f, 3.5f), 0);
        }
        while ((hZwei.transform.position - hEins.transform.position).magnitude < 2);

        do
        {
            hDrei.transform.position = new Vector3(Random.Range(-3.0f, 3.0f), Random.Range(-3.5f, 3.5f), 0);
        } while ((hDrei.transform.position + hEins.transform.position).magnitude < 2 || (hDrei.transform.position - hZwei.transform.position).magnitude < 2);
    }

    public void ToggleMaulwurf_Click()
    {
        if (toggleMaulwurf == true)
        {
            toggleMaulwurf = false;
            hEins.SetActive(false);
            hZwei.SetActive(false);
            hDrei.SetActive(false);
        }
        else
        {
            toggleMaulwurf = true;
            hEins.SetActive(true);
            hZwei.SetActive(true);
            hDrei.SetActive(true);
        }
    }

    void SpielerRechtsZurueck()
    {
        spielerRechts.transform.Translate(0.3f, 0, 0);
    }

    void SpielerLinksZurueck()
    {
        spielerLinks.transform.Translate(-0.3f, 0, 0);
    }

    void OnCollisionEnter2D(Collision2D coll)
    {
        if (coll.gameObject.CompareTag("WandLinks"))
        {
            AudioSource.PlayClipAtPoint(Punkt, transform.position);
            punkteRechts++;
            punkteAnzeigeRechts.text = punkteRechts + "";
            aufschlagRechts = true;
            gameObject.SetActive(false);
            if (punkteRechts == int.Parse(GweinnPunkte.text))
            {
                punkteAnzeigeRechts.text = "Gew.";
                return;
            }
            Invoke(nameof(BallAufStartRechts), 1);
        }
        else if (coll.gameObject.CompareTag("WandRechts"))
        {
            AudioSource.PlayClipAtPoint(Punkt, transform.position);
            punkteLinks++;
            punkteLinzsAnzeige.text = punkteLinks + "";
            aufschlagRechts = false;
            gameObject.SetActive(false);
            if (punkteLinks == int.Parse(GweinnPunkte.text))
            {
                punkteLinzsAnzeige.text = "Gew.";
                return;
            }
            Invoke(nameof(BallAufStartLinks), 1);
        }
        else if (coll.gameObject.CompareTag("Spieler"))
        {
            rb.velocity = new Vector2(rb.velocity.x * 1.02f, rb.velocity.y * 1.02f);
        }
        else if (!coll.gameObject.CompareTag("WandRechts") && !coll.gameObject.CompareTag("WandLinks"))
        {
            AudioSource.PlayClipAtPoint(prallen, transform.position);
        }
    }

    void BallAufStartRechts()
    {
        transform.position = new Vector3(7.99f, 0, 0);
        BallAufStart();
    }

    void BallAufStartLinks()
    {
        transform.position = new Vector3(-7.99f, 0, 0);
        BallAufStart();
    }

    void BallAufStart()
    {
        HindernissSetzen();
        spielerLinks.transform.position = new Vector3(-8.44f, 0, 0);
        spielerRechts.transform.position = new Vector3(8.44f, 0, 0);
        gameObject.SetActive(true);
    }

    public void NeuesSpiel_Click()
    {
        GweinnPunkte.readOnly = false;
        gameObject.SetActive(false);
        if (Random.Range(0, 10) <= 5)
        {
            transform.position = new Vector3(7.99f, 0, 0);
            aufschlagRechts = true;
        }
        else
        {
            transform.position = new Vector3(-7.99f, 0, 0);
            aufschlagRechts = false;
        }
        BallAufStart();
        punkteLinks = 0;
        punkteRechts = 0;
        punkteAnzeigeRechts.text = punkteRechts + "";
        punkteLinzsAnzeige.text = punkteLinks + "";
    }

    public void SpielBeenden_Click()
    {
        Application.Quit();
    }
}

//TODO:
// - evtl. KI einbauen
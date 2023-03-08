#include <Arduino.h>                      // mit #include Bibliotheken hinzugefügt - also schon fertiger Code, damit wir nicht zu viel schreiben müssen. Wir arbeiten mit dem Arduino Framework und der FastLED Bibliothek
#include <FastLED.h>

#define DATA_PIN    2                   //hier trägt man den Pin ein, an dem die Datenleitung am Digispark angeschlossen ist.
#define LED_TYPE    NEOPIXEL              //wir arbeiten mit WS2812B - LEDs -> sind die gleichen wie neopixel
#define NUM_LEDS    30                   //das maximum ist bei Digispark anscheinend bei 108 LEDs -> wir haben 20 LEDs -> was passiert wenn du eine höhere oder niedrigere Zahl eingibst?
CRGB strip[NUM_LEDS];                     //hier wird Speicherplatz für die Farben von jeder einzelnen LED reserviert -> also 20 x CRGB - Werte -> sind dann 32 bit pro farbe, also insgesamt 640 bit

uint8_t led_nummer = 0;                   // hier wird gespeichert, bei welcher LED sich das Licht gerade befindet. Die Zahl kann von 0 - 255 gehen ( für PingPongLeds)
bool hochZaelen;                           // das ist ein Boolean. Das bedeutet das die hochZaelen nur wahr oder falsch 
unsigned long nextzeit = 1000;

void lilazublau(){
  for(int i=0; i<NUM_LEDS; i++){
    strip[i] = CRGB(16*i, 0, 126);
  }
  FastLED.show();
}

void pingPongLicht(){
   if(led_nummer == NUM_LEDS - 1){
    hochZaelen = false;                     //wenn die vorletzte LED ausgewählt ist, dann rückwärts zählen
  }
  
  if(led_nummer == 0){
    hochZaelen = true;                      //wenn die erste LED ausgewählt ist dann vorwärts zählen
  }

  if(hochZaelen){
    led_nummer++;                         //wähle die nächste LED aus wenn die laufrichtung rückwärts ist
  }

  else{
    led_nummer--;                         //wähle die vorherige LED aus senn die Richtung nicht vorwärts ist
  }

  strip[led_nummer] = CRGB(255,0,0); //suche dir deine Farbe aus, indem du die *** durch zahlen zwischen 0 und 255 ersetzt
  
  FastLED.show();                         //sende die neuen Farben für die LEDs an den streifen
  strip[led_nummer] = CRGB::Black;        //setze die Farbe der LED wieder auf schwarz -> die LED geht dann erst im nächsten durchlauf aus weil FastLED.show() noch nicht aufgerufen ist
  delay(100);                             // warte eine zehntel sekunde -> je höher diese Zahl, desto langsamer läuft das licht
}

void zufallsFarben(){
  if(millis() > nextzeit){                              //wenn die nächste LED angeschaltet werden soll
    nextzeit = millis() + random(100,200);              //bestimme den zeitpunkt für die nächste LED. Die Zahlen in der Klammer bestimmen wie oft eine neue LED angeht
    led_nummer = random(NUM_LEDS-1);                    //wählt eine Zufällige LED aus
    strip[led_nummer] += CRGB(random8(),random8(),random8());       //wählt eine Zufällige farbe für diese LED
  }
  for(int i = 0; i<NUM_LEDS; i++){
    strip[i]--;                                         //dadurch weden die LEDs langsam dunkler
  }
    FastLED.show();                                    //lässt die Farben anzeigen
  delay(5);                                          //hier kann man die Geschwindigkeit einstellen -> je höher, desto langsamer gehen die LEDs aus
}


//erklährung zu den Zahlen: 1. die Led-Nummer, 2. die geschwindigkeit, mit der die Welle durch den Streifen geht 3. die länge einer welle, 4. die helligkeit der welle und zu guter letzt die zeit
uint8_t berechneSinusFarbe( uint8_t LED_num, float geschwindigkeit, float laenge, int helligkeit, float zeit)
{
  return (uint8_t) helligkeit *( sinf( zeit * geschwindigkeit + (LED_num * laenge) ) + 1 );
}


void sinusWellenFarben()
{

  float time = float(millis())/1000;                                //erst mal die Zeit ausrechnen

  for(int i = 0; i<NUM_LEDS; i++){                                  //der Loop geht durch alle LEDs durch und berechnet:

    uint8_t r = berechneSinusFarbe(i, 10, 4, 50, time);            //den Roten Farbwert  (hier kann man die mittleren 3 zahlen in der Klammer verändern, um die Farben auf dem Led Streifen zu verändern)
    uint8_t g = berechneSinusFarbe(i, 0.4, 20, 50, time);          //den grünen Farbwert
    uint8_t b = berechneSinusFarbe(i, 2, 13, 50, time);            //den blauen Farbwert

    strip[i] = CRGB(r,g,b);                                         //am Ende werden die Rot, grün und blau werte zu einer Farbe gemischt
  }
  FastLED.show();                                                   //und dann noch angezeigt
}

void setup() 
{
  FastLED.addLeds<LED_TYPE, DATA_PIN>(strip, NUM_LEDS);             //weise den Speicherplatz für die Farben der LEDs zu
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 500);                   // LED-Streifen wird über USB betrieben - bei 5V & 500mA
}

void loop() 
{
  //pingPongLicht();                                                  //hier kann man einstellen, wie dein Streifen am ende leuchten soll. (es gibt 3 varianten schon fertig)
  //zufallsFarben();                                                //Kommentiere dazu einfach eine der Funktionen aus, indem du die zwei "/" zeichen vor der Zeile löscht!
  sinusWellenFarben();                                            //Es sollte aber immer nur eine Funktion auf einmal aktiv sein.
}
import java.util.Scanner;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Vokabeltrainer {

    static List<Vokabel> vokabelListe;

    public Vokabeltrainer(){
        //Konstruktor Vokabeltrainer; nötig um static aus main aufzulösen
        //VokabelListe erscchaffen, danach aufruf des menues 
        vokabelListe = new List<Vokabel>();
        //menue();
    }

    public static void main(String[] args) {
        //Eine Objekt vt vom Typ Vokabeltrainer erstellen
        Vokabeltrainer vt = new Vokabeltrainer();
        JFrame meinJFrame = new JFrame();
        meinJFrame.setTitle("Vokabeltrainer");
        JPanel panel = new JPanel();
        JButton button = new JButton("neue Vokabeln eingeben");
        button.addActionListener(new java.awt.event.ActionListener(){
            public void actionPerformed(java.awt.event.ActionEvent e) {
                vt.vokabelnEinfuegen();
            }
        });
        panel.add(button);
        meinJFrame.add(panel);
        meinJFrame.pack();
        meinJFrame.setVisible(true);
 
    }

    void menue(){
        //Auswahlmöglichkeiten ausgeben
        System.out.println("1) neue Vokabel einfügen");
        System.out.println("9) alle Vokabeln anzeigen");
        System.out.println("42) Testmethode aufrufen");
        Scanner input = new Scanner(System.in);

        //Eingabe verarbeiten
        int auswahl = input.nextInt();
        switch(auswahl){
            case 1:
                vokabelnEinfuegen();
                break;
            case 9:
                alleVokabel();
            case 42:
                Testmethode();
                break;
            default:
                break;
        }
    }

    static void Testmethode(){
        Vokabel pVokabel = new Vokabel("Home", "Haus");
        vokabelListe.insert(pVokabel);
        vokabelListe.toFirst();
        System.out.print(vokabelListe.getContent().deutsch);
        System.out.print(" = ");
        System.out.println(vokabelListe.getContent().fremd);
    }
    
    void vokabelnEinfuegen(){
        System.out.print("Bitte das Deutschwort eingeben: ");
        Scanner deInput = new Scanner(System.in);
        String deVokabel = deInput.nextLine();
        System.out.print("Bitte das Fremdwort eingeben: ");
        String engVokabel = deInput.nextLine();
        Vokabel v = new Vokabel(engVokabel, deVokabel);
        vokabelListe.append(v);
        //menue();
    }

    void alleVokabel(){
        vokabelListe.toFirst();
        while(vokabelListe.hasAccess()){
            System.out.println(vokabelListe.getContent().deutsch + " - " + vokabelListe.getContent().fremd);
            vokabelListe.next();
            menue();
        }
    }
}

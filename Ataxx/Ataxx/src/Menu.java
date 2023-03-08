import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

public class Menu extends JMenuBar implements ActionListener {
	private static final long serialVersionUID = 1L;
	Ataxx parent;
	GamePanel gamePanel;

	public Menu(Ataxx parent) {
		this.parent = parent;
		this.gamePanel = parent.spielfeld;

		JMenu m = new JMenu("Spiel");
		JMenuItem mi = new JMenuItem("Neustart");
		mi.setActionCommand("start");
		mi.addActionListener(this);
		m.add(mi);
		m.addSeparator();
		mi = new JMenuItem("Spielbrett 1");
		mi.setActionCommand("game0");
		mi.addActionListener(this);
		m.add(mi);
		mi = new JMenuItem("Spielbrett 2");
		mi.setActionCommand("game1");
		mi.addActionListener(this);
		m.add(mi);
		mi = new JMenuItem("Spielbrett 3");
		mi.setActionCommand("game2");
		mi.addActionListener(this);
		m.add(mi);
		m.addSeparator();
		mi = new JMenuItem("Beenden");
		mi.setActionCommand("exit");
		mi.addActionListener(this);
		m.add(mi);
		this.add(m);

		m = new JMenu("Hilfe");
		mi = new JMenuItem("Über Ataxx...");
		mi.setActionCommand("about");
		mi.addActionListener(this);
		m.add(mi);
		mi = new JMenuItem("Spielregeln");
		mi.setActionCommand("rules");
		mi.addActionListener(this);
		m.add(mi);
		this.add(m);
	}

	public void actionPerformed(ActionEvent event) {
		if (event.getActionCommand().equals("start")) {
			gamePanel.reset();
		}
		if (event.getActionCommand().equals("exit")) {
			System.exit(0);
		}
		if (event.getActionCommand().equals("game0")) {
			gamePanel.selectGame(0);
		}
		if (event.getActionCommand().equals("game1")) {
			gamePanel.selectGame(1);
		}
		if (event.getActionCommand().equals("game2")) {
			gamePanel.selectGame(2);
		}
		if (event.getActionCommand().equals("about")) {
			new AlertBox(parent, "Über Ataxx...", 0, "Ataxx\n(c) 2017 by Jörg (Yogi) Kuhle");
		}
		if (event.getActionCommand().equals("rules")) {
			new AlertBox(parent, "Spielregeln", 0,
					"Das Spiel endet, wenn es vollständig gefüllt ist.\nEs gewinnt der Spieler mit den meisten Steinen.\nEin Stein wird verdoppelt, wenn man auf sein Nachbarfeld in beliebiger Richtung zieht.\nEin Sprung kann zwei Felder waagerecht oder senkrecht ausgeführt werden.\nGegnerische Steine, neben die gezogen wird, werden zu eigenen Steinen.");
		}
	}

}

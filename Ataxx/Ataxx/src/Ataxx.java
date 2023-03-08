import java.awt.*;
import java.awt.event.*;

import javax.swing.JFrame;
import javax.swing.JTextField;

public class Ataxx extends JFrame {
	private static final long serialVersionUID = 1L;
	GamePanel spielfeld;
//	JTextField statusBar;

	public static void main(String[] args) {
		new Ataxx();
	}

	public Ataxx() {
		super("Ataxx");
		spielfeld = new GamePanel(this);
		this.add(spielfeld, BorderLayout.CENTER);
//		statusBar=new JTextField("White: 2, Black: 2");
//		this.add(statusBar, BorderLayout.SOUTH);
		this.setBounds(0, 0, 100, 100);
//		this.setJMenuBar(new Menu(this));
		setUndecorated(true);
		this.pack();
		this.setVisible(true);

		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent event) {
				setVisible(false);
				dispose();
				System.exit(0);
			}
		});
	}

}

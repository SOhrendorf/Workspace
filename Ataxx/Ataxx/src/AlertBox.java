import java.awt.*;
import javax.swing.*;
import java.awt.event.*;


public class AlertBox extends JDialog implements ActionListener {
	private static final long serialVersionUID = 1L;
	
	public AlertBox(JFrame parent, String title, int icon, String text) {
		super(parent, title, true);
		
        enableEvents(AWTEvent.WINDOW_EVENT_MASK);
        setBounds(parent.getX()+100,parent.getY()+100,300,150);
		JPanel panel=new JPanel();
		panel.setLayout(new FlowLayout(FlowLayout.CENTER));
		JTextPane label=new JTextPane();
		label.setText(text);
		label.setEditable(false);
		panel.add(label);
		add(panel, BorderLayout.CENTER);
		panel=new JPanel();
		panel.setLayout(new FlowLayout(FlowLayout.CENTER));
        JButton Ok = new JButton("OK");
        Ok.addActionListener(this);
        Ok.setActionCommand("ok");
        panel.add(Ok);
        add(panel, BorderLayout.SOUTH);
        pack();		
        setVisible(true);
	}
	
	public void actionPerformed(ActionEvent event) {
		setVisible(false);
	}

    public void processEvent(AWTEvent event) {
        if (event.getID() == Event.WINDOW_DESTROY) {
            dispose();
        } else {
            super.processEvent(event);
        }
    }	
}

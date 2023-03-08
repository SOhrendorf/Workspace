import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JPanel;

public class GamePanel extends JPanel implements Runnable {
	private static final long serialVersionUID = 1L;
	Image bgimg;
	Image trackerWhite, trackerBlack;
	Image feltImage;
	Image holeImage;
	Image ataxxImage;
	Image gridImage;
	Image[] cursorImage;
	Ataxx parent;
	Stone[][] field;
	boolean[][] holes;
	int player = 0;
	private Image dbImage;
	private Graphics dbGraphics;
	Thread timer = null;
	Stone tracker = null;
	int step = 0;
	Color lightColor = new Color(0, 196, 0);
	Color darkColor = new Color(0, 128, 0);
	Color overlayColor = new Color(0, 0, 0, 64);
	Color cursorColorWhite = new Color(192, 192, 192);
	Color cursorColorBlack = new Color(32, 32, 32);
	int mouseX, mouseY;
	int gameType = 0;
	boolean gameRunning;
	Sound sound;
	boolean infected = false;
	int theme = 1;
	Image restartImage;
	Image shutdownImage;

	public GamePanel(Ataxx parent) {
		super();
		sound = new Sound();
		this.setPreferredSize(new Dimension(900, 700));

		this.parent = parent;
		reset();

		bgimg = this.getToolkit().getImage("img/back.jpg");
		trackerWhite = this.getToolkit().getImage("img/tracker0.png");
		trackerBlack = this.getToolkit().getImage("img/tracker1.png");
		holeImage = this.getToolkit().getImage("img/theme" + theme + "/hole.png");
		ataxxImage = this.getToolkit().getImage("img/theme" + theme + "/ataxx2.png");
		gridImage = this.getToolkit().getImage("img/grid.png");
		cursorImage = new Image[2];
		cursorImage[0] = this.getToolkit().getImage("img/cursor0.png");
		cursorImage[1] = this.getToolkit().getImage("img/cursor1.png");
		restartImage = this.getToolkit().getImage("img/restart.png");
		shutdownImage = this.getToolkit().getImage("img/shutdown.png");
		startTimer();

		addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent event) {
				if (event.getX() > 8 && event.getX() < 136 && event.getY() > 8 && event.getY() < 136) {
					System.exit(0);
				}
				else if (event.getX() > 8 && event.getX() < 136 && event.getY() > 144 && event.getY() < 272) {
					reset();					
				} else {
					if (timer == null) {
						int x = (event.getX() - 512) / 128;
						int y = (event.getY() - 92) / 128;
						if (x >= 0 && y >= 0 && x < 7 && y < 7) {
							if (!holes[x][y]) {
								gameRunning = true;
								if (tracker == null && field[x][y] != null && field[x][y].getPlayer() == player) {
									// Neuen Stein auswaehlen
									tracker = field[x][y];
									repaint();
								} else {
									if (tracker != null) {
										// Zug durchfuehren
										if (field[x][y] == null) {
											if (Math.abs(x - tracker.getX()) <= 1
													&& Math.abs(y - tracker.getY()) <= 1) {
												// Nachbarfeld belegen
												Stone stone = new Stone(x, y, theme);
												stone.setPlayer(player);
												field[x][y] = stone;
												infect(x, y, player);
												player = 1 - player;
												startTimer();
												sound.play("sfx/sfx0.wav");
												tracker = null;
											} else if ((Math.abs(x - tracker.getX()) == 2 && y == tracker.getY())
													|| (Math.abs(y - tracker.getY()) == 2 && x == tracker.getX())) {
												// Auf Feld springen
												field[x][y] = field[tracker.getX()][tracker.getY()];
												field[tracker.getX()][tracker.getY()] = null;
												field[x][y].jump(x, y);
												infect(x, y, player);
												player = 1 - player;
												startTimer();
												sound.play("sfx/sfx1.wav");
												tracker = null;
											}
										} else {
											if (field[x][y].getPlayer() == player) {
												tracker = field[x][y];
											} else {
												tracker = null;
											}
										}
									}
									repaint();
								}
							}
						}
						if (!possibleMove()) {
							player = 1 - player;
							fillField();
							startTimer();
						}
						count();
					}
				}
			}
		});

		addMouseMotionListener(new MouseAdapter() {
			public void mouseMoved(MouseEvent event) {
				int x = (event.getX() - 512) / 128;
				int y = (event.getY() - 92) / 128;
				if (x < 0)
					x = 0;
				if (y < 0)
					y = 0;
				if (x >= 8)
					x = 7;
				if (y >= 8)
					y = 7;
				if (mouseX != x || mouseY != y) {
					mouseX = x;
					mouseY = y;
					repaint();
				}
			}
		});
	}

	public boolean possibleMove() {
		boolean possible = false;
		for (int y = 0; y < 7; y++) {
			for (int x = 0; x < 7; x++) {
				if (field[x][y] != null && field[x][y].getPlayer() == player) {
					for (int j = y - 1; j <= y + 1; j++) {
						for (int i = x - 1; i <= x + 1; i++) {
							if (i >= 0 && j >= 0 && i < 7 && j < 7) {
								if (field[i][j] == null) {
									possible = true;
								}
							}
						}
					}
					if (x + 2 < 7 && field[x + 2][y] == null)
						possible = true;
					if (x - 2 >= 0 && field[x - 2][y] == null)
						possible = true;
					if (y + 2 < 7 && field[x][y + 2] == null)
						possible = true;
					if (y - 2 >= 0 && field[x][y - 2] == null)
						possible = true;
				}
			}
		}
		return possible;
	}

	public void fillField() {
		for (int y = 0; y < 7; y++) {
			for (int x = 0; x < 7; x++) {
				if (field[x][y] == null) {
					Stone stone = new Stone(x, y, theme);
					stone.setPlayer(player);
					field[x][y] = stone;
				}
			}
		}
	}

	public void infect(int x, int y, int player) {
		infected = false;
		for (int j = y - 1; j <= y + 1; j++) {
			for (int i = x - 1; i <= x + 1; i++) {
				if (i >= 0 && j >= 0 && i < 7 && j < 7) {
					if (field[i][j] != null && field[i][j].getPlayer() != player) {
						field[i][j].turnPlayer();
						infected = true;
					}
				}
			}
		}
		// if (infected)
		// startTimer();
	}

	public void count() {
		int black = 0;
		int white = 0;
		for (int y = 0; y < 7; y++) {
			for (int x = 0; x < 7; x++) {
				if (field[x][y] != null) {
					if (field[x][y].getPlayer() == 0)
						white++;
					else
						black++;
				}
			}
		}
//		parent.statusBar.setText("White: " + white + ", Black: " + black);
	}

	public void startTimer() {
		if (timer == null) {
			timer = new Thread(this);
			step = 0;
			timer.start();
		}
	}

	public void setStone(int x, int y) {
		Stone stone = new Stone(x, y, theme);
		stone.setPlayer(player);
		field[x][y] = stone;
	}

	public boolean checkMove(int x, int y) {
		// Steinreihe nach rechts suchen (alle folgenden Steine gehoeren dem
		// anderen Spieler und der letzte wieder dem aktuellen Spieler
		int px = x + 1;
		while (px < 8 && field[px][y] != null && field[px][y].getPlayer() == 1 - player) {
			px++;
		}
		if (px < 8 && field[px][y] != null && field[px][y].getPlayer() == player && px > x + 1) {
			// Gueltiger Zug
			return true;
		}

		// Steine nach links suchen
		px = x - 1;
		while (px >= 0 && field[px][y] != null && field[px][y].getPlayer() == 1 - player) {
			px--;
		}
		if (px >= 0 && field[px][y] != null && field[px][y].getPlayer() == player && px < x - 1) {
			// Gueltiger Zug
			return true;
		}

		// Steinreihe nach unten suchen
		int py = y + 1;
		while (py < 8 && field[x][py] != null && field[x][py].getPlayer() == 1 - player) {
			py++;
		}
		if (py < 8 && field[x][py] != null && field[x][py].getPlayer() == player && py > y + 1) {
			// Gueltiger Zug
			return true;
		}

		// Steine nach oben suchen
		py = y - 1;
		while (py >= 0 && field[x][py] != null && field[x][py].getPlayer() == 1 - player) {
			py--;
		}
		if (py >= 0 && field[x][py] != null && field[x][py].getPlayer() == player && py < y - 1) {
			// Gueltiger Zug
			return true;
		}

		// Steine nach rechts unten suchen
		px = x + 1;
		py = y + 1;
		while (px < 8 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px++;
			py++;
		}
		if (px < 8 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == player && px > x + 1
				&& py > y + 1) {
			return true;
		}

		// Steine nach links unten suchen
		px = x - 1;
		py = y + 1;
		while (px >= 0 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px--;
			py++;
		}
		if (px >= 0 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == player && px < x - 1
				&& py > y + 1) {
			return true;
		}

		// Steine nach links oben suchen
		px = x - 1;
		py = y - 1;
		while (px >= 0 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px--;
			py--;
		}
		if (px >= 0 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == player && px < x - 1
				&& py < y - 1) {
			return true;
		}

		// Steine nach rechts oben suchen
		px = x + 1;
		py = y - 1;
		while (px < 8 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px++;
			py--;
		}
		if (px < 8 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == player && px > x + 1
				&& py < y - 1) {
			return true;
		}

		return false;
	}

	public void turn(int x, int y) {
		// Steinreihe nach rechts suchen und umdrehen
		int px = x + 1;
		while (px < 8 && field[px][y] != null && field[px][y].getPlayer() == 1 - player) {
			px++;
		}
		if (px < 8 && px > x + 1 && field[px][y] != null && field[px][y].getPlayer() == player) {
			px = x + 1;
			while (px < 8 && field[px][y] != null && field[px][y].getPlayer() == 1 - player) {
				field[px][y].turnPlayer();
				px++;
			}
		}

		// Steine nach links suchen und umdrehen
		px = x - 1;
		while (px >= 0 && field[px][y] != null && field[px][y].getPlayer() == 1 - player) {
			px--;
		}
		if (px >= 0 && px < x - 1 && field[px][y] != null && field[px][y].getPlayer() == player) {
			px = x - 1;
			while (px >= 0 && field[px][y] != null && field[px][y].getPlayer() == 1 - player) {
				field[px][y].turnPlayer();
				px--;
			}
		}

		// Steinreihe nach unten suchen und umdrehen
		int py = y + 1;
		while (py < 8 && field[x][py] != null && field[x][py].getPlayer() == 1 - player) {
			py++;
		}
		if (py < 8 && py > y + 1 && field[x][py] != null && field[x][py].getPlayer() == player) {
			py = y + 1;
			while (py < 8 && field[x][py] != null && field[x][py].getPlayer() == 1 - player) {
				field[x][py].turnPlayer();
				py++;
			}
		}

		// Steinreihe nach oben suchen und umdrehen
		py = y - 1;
		while (py >= 0 && field[x][py] != null && field[x][py].getPlayer() == 1 - player) {
			py--;
		}
		if (py >= 0 && py < y - 1 && field[x][py] != null && field[x][py].getPlayer() == player) {
			py = y - 1;
			while (py >= 0 && field[x][py] != null && field[x][py].getPlayer() == 1 - player) {
				field[x][py].turnPlayer();
				py--;
			}
		}

		// Steinreihe nach rechts unten suchen und umdrehen
		px = x + 1;
		py = y + 1;
		while (px < 8 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px++;
			py++;
		}
		if (px < 8 && py < 8 && px > x + 1 && py > y + 1 && field[px][py] != null
				&& field[px][py].getPlayer() == player) {
			px = x + 1;
			py = y + 1;
			while (px < 8 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
				field[px][py].turnPlayer();
				px++;
				py++;
			}
		}

		// Steinreihe nach links unten suchen und umdrehen
		px = x - 1;
		py = y + 1;
		while (px >= 0 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px--;
			py++;
		}
		if (px >= 0 && py < 8 && px < x - 1 && py > y + 1 && field[px][py] != null
				&& field[px][py].getPlayer() == player) {
			px = x - 1;
			py = y + 1;
			while (px >= 0 && py < 8 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
				field[px][py].turnPlayer();
				px--;
				py++;
			}
		}

		// Steinreihe nach links oben suchen und umdrehen
		px = x - 1;
		py = y - 1;
		while (px >= 0 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px--;
			py--;
		}
		if (px >= 0 && py >= 0 && px < x - 1 && py < y - 1 && field[px][py] != null
				&& field[px][py].getPlayer() == player) {
			px = x - 1;
			py = y - 1;
			while (px >= 0 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
				field[px][py].turnPlayer();
				px--;
				py--;
			}
		}

		// Steinreihe nach rechts oben suchen und umdrehen
		px = x + 1;
		py = y - 1;
		while (px < 8 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
			px++;
			py--;
		}
		if (px < 8 && py >= 0 && px > x + 1 && py < y - 1 && field[px][py] != null
				&& field[px][py].getPlayer() == player) {
			px = x + 1;
			py = y - 1;
			while (px < 8 && py >= 0 && field[px][py] != null && field[px][py].getPlayer() == 1 - player) {
				field[px][py].turnPlayer();
				px++;
				py--;
			}
		}

	}

	public void update(Graphics g) {
		// Double-Buffer initialisieren
		if (dbImage == null) {
			dbImage = createImage(this.getWidth(), this.getHeight());
			dbGraphics = dbImage.getGraphics();
		}
		// Hintergrund loeschen
		dbGraphics.setColor(getBackground());
		dbGraphics.fillRect(0, 0, this.getWidth(), this.getHeight());
		// Vordergrund zeichnen
		dbGraphics.setColor(getForeground());
		paint(dbGraphics);
		// Offscreen anzeigen
		g.drawImage(dbImage, 0, 0, this);
	}

	public void paint(Graphics g) {
		// Hintergrund malen
		g.drawImage(bgimg, 0, 0, this);

		// Spielfeld malen
		for (int y = 0; y < 7; y++)
			for (int x = 0; x < 7; x++)
				g.drawImage(gridImage, (x << 7) + 300, (y << 7) + 20, this);

		// Cursor zeichnen
		g.drawImage(cursorImage[player], (mouseX << 7) + 512, (mouseY << 7) + 92, this);

		// Loecher zeichnen
		for (int y = 0; y < 7; y++)
			for (int x = 0; x < 7; x++)
				if (holes[x][y])
					g.drawImage(holeImage, (x << 6) + 32, (y << 6) + 32, this);

		// Spielsteine zeichnen
		for (int y = 0; y < 7; y++)
			for (int x = 0; x < 7; x++)
				if (field[x][y] != null)
					field[x][y].paint(g, this, x, y, step);

		if (!gameRunning)
			g.drawImage(ataxxImage, 0, 224, this);

		// Tracker zeichnen
		if (tracker != null) {
			tracker.paintTracker(g);
		}

		g.drawImage(restartImage, 8, 144, this);
		g.drawImage(shutdownImage, 8, 8, this);
	}

	public void reset() {
		field = new Stone[7][7];
		Stone stone = new Stone(0, 0, theme);
		stone.setPlayer(0);
		field[0][0] = stone;
		stone = new Stone(6, 6, theme);
		stone.setPlayer(0);
		field[6][6] = stone;
		stone = new Stone(0, 6, theme);
		stone.setPlayer(1);
		field[0][6] = stone;
		stone = new Stone(6, 0, theme);
		stone.setPlayer(1);
		field[6][0] = stone;
		holes = new boolean[7][7];

		if (gameType == 1) {
			holes[1][1] = true;
			holes[5][1] = true;
			holes[1][5] = true;
			holes[5][5] = true;
		}
		if (gameType == 2) {
			holes[3][3] = true;
			holes[2][2] = true;
			holes[2][4] = true;
			holes[4][2] = true;
			holes[4][4] = true;
		}

		player = 0;
		gameRunning = false;
		startTimer();
	}

	public void selectGame(int gameType) {
		this.gameType = gameType;
		reset();
	}

	public void run() {
		while (timer != null) {
			step++;
			repaint();
			if (infected && step == 8)
				sound.play("sfx/sfx2.wav");

			if (step >= 17) {
				step = 0;
				timer = null;
			}
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
			}
		}
	}

}

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Stone {
	private int player;
	private Image[] images;
	boolean flipped = false;
	boolean created = false;
	boolean jumped = false;
	private int x, y;
	private int lastX, lastY;
	Image holeImage;

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}

	Color shadowColor = new Color(0, 0, 0, 50);
	Color highlightColor = new Color(255, 255, 255, 50);

	public Stone(int x, int y, int theme) {
		this.x = x;
		this.y = y;
		loadImages(theme);
		if (theme == 1) {
			highlightColor = new Color(0, 0, 0, 50);
		}
		created = true;
	}

	private void loadImages(int theme) {
		// Bilder fuer Animation laden
		// Dazu wird ein grosses Images zerschnitten
		images = new Image[9];
		BufferedImage shapes = null;
		try {
			shapes = ImageIO.read(new File("img/rings.png"));
		} catch (IOException e) {
			System.out.println("Kann Shapes nicht laden.");
		}
		for (int i = 0; i < 9; i++)
			images[i] = shapes.getSubimage(i * 128, 0, 128, 128);
	}

	public int getPlayer() {
		return player;
	}

	public void setPlayer(int player) {
		if (player < 0)
			player = 0;
		if (player > 1)
			player = 1;
		this.player = player;
	}

	public void turnPlayer() {
		flipped = true;
		player = 1 - player;
	}

	public void jump(int x, int y) {
		lastX = this.x;
		lastY = this.y;
		this.x = x;
		this.y = y;
		jumped = true;
	}

	public void stopAnimation() {
		created = false;
		flipped = false;
	}

	public void paint(Graphics g, GamePanel panel, int x, int y, int step) {
		if (step == 0 || (!flipped && !created && !jumped)) {
			g.drawImage(images[player * 8], (x << 7) + 512, (y << 7) + 92, panel);
		} else {
			if (step <= 8) {
				if (created) {
					g.drawImage(images[player * 8], (x << 7) + 512 + 64  - (step << 3), (y << 7) + 92 + 64 - (step << 3), step << 4,
							step << 4, panel);
				} else if (jumped) {
					int size = 128 + (int) (Math.sin((double) step / 8 * 3.1416) * 32);
					int pos = (int) ((1 - Math.cos((double) step / 8 * 3.1416)) * 128);
					if (x > lastX) {
						g.drawImage(images[player * 8], (x << 7) + 512 + 64 - (size / 2) - 256 + pos,
								(y << 7) + 92 + 64 - (size / 2), size, size, panel);
					} else if (x < lastX) {
						g.drawImage(images[player * 8], (x << 7) + 512 + 64 - (size / 2) + 256 - pos,
								(y << 7) + 92 + 64 - (size / 2), size, size, panel);
					} else if (y > lastY) {
						g.drawImage(images[player * 8], (x << 7) + 512 + 64 - (size / 2),
								(y << 7) + 92 + 64 - (size / 2) - 256 + pos, size, size, panel);
					} else {
						g.drawImage(images[player * 8], (x << 7) + 512 + 64 - (size / 2),
								(y << 7) + 92 + 64 - (size / 2) + 256 - pos, size, size, panel);
					}
//					if (x > lastX) {
//						g.drawImage(images[player * 8], (x << 6) + 32 + 32 - (size / 2) - 128 + pos,
//								(y << 6) + 32 + 32 - (size / 2), size, size, panel);
//					} else if (x < lastX) {
//						g.drawImage(images[player * 8], (x << 6) + 32 + 32 - (size / 2) + 128 - pos,
//								(y << 6) + 32 + 32 - (size / 2), size, size, panel);
//					} else if (y > lastY) {
//						g.drawImage(images[player * 8], (x << 6) + 32 + 32 - (size / 2),
//								(y << 6) + 32 + 32 - (size / 2) - 128 + pos, size, size, panel);
//					} else {
//						g.drawImage(images[player * 8], (x << 6) + 32 + 32 - (size / 2),
//								(y << 6) + 32 + 32 - (size / 2) + 128 - pos, size, size, panel);
//					}
//
				} else {
					if (flipped) {
						g.drawImage(images[(1 - player) * 8], (x << 7) + 512, (y << 7) + 92, panel);
					} else {
						g.drawImage(images[player * 8], (x << 7) + 512, (y << 7) + 92, panel);
					}
				}
			}
			if (step >= 8 && flipped) {
				if (player == 1) {
					g.drawImage(images[step - 8], (x << 7) + 512, (y << 7) + 92, panel);
				} else {
					g.drawImage(images[8 - (step - 8)], (x << 7) + 512, (y << 7) + 92, panel);
				}
			}
			if (step >= 8) {
				created = false;
				jumped = false;
			}
			if (step >= 16) {
				flipped = false;
			}
		}
	}

	public void paintTracker(Graphics g) {
		g.setColor(player == 0 ? shadowColor : highlightColor);
		g.fillOval((x << 6) + 36, (y << 6) + 36, 55, 55);
	}
}

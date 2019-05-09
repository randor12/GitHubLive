/**
 * Ryan Nicholas
 * Make the code be able to autosave
 */

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.lang.*;

/**
 * @author Ryan's Computer
 *
 */
public class SaveFunction extends JPanel implements ActionListener {

	private int count = 0;
	private Robot r = null;
	
	private static final int WIDTH = 10;
	private static final int HEIGHT = 10;
	
	/**
	 * initialize the save function
	 */
	public SaveFunction()
	{
		this.initCheckAction();
	}
	
	/**
	 * sets up key listener
	 */
	public void initCheckAction()
	{
		addKeyListener(new TAdapter());
		setBackground(Color.black);
		setFocusable(true);
		
		setPreferredSize(new Dimension(WIDTH, HEIGHT));
		
	}
	
	/**
	 * Checks to autosave 
	 */
	public void checkSave()
	{
		if (count % 20 == 0)
		{
			try {
				r = new Robot();
			} catch (AWTException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			r.keyPress(KeyEvent.VK_CONTROL);
			r.keyPress(KeyEvent.VK_S);
			r.keyRelease(KeyEvent.VK_S);
			r.keyRelease(KeyEvent.VK_CONTROL);
			
		}
	}
	
	@Override
	/**
	 * This checks to save the action
	 * @param e		auto save action
	 */
	public void actionPerformed(ActionEvent e)
	{
		this.checkSave();
	}
	
	private class TAdapter extends KeyAdapter
	{
		public void keyPressed(KeyEvent e)
		{
			int key = e.getKeyCode();
			if (key == KeyEvent.KEY_RELEASED)
			{
				count++;
			}
		}
	}
	
}

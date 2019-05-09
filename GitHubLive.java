/**
 * Ryan Nicholas
 * Git Hub Live Program
 * This automatically saves code after pressing 
 * a button 20 times
 */

import java.awt.*;
import javax.swing.*;

/**
 * @author Ryan's Computer
 * @version 2019.05.08
 *
 */
public class GitHubLive extends JFrame {
	
	/**
	 * Set up the GitHub code
	 */
	public GitHubLive()
	{
		initUI();
	}
	
	private void initUI()
	{
		add(new SaveFunction());
		
		setResizable(false);
		pack();
        
        setTitle("Git Hub Auto Save"); //title
        setLocationRelativeTo(null); 
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Exit application
		
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		EventQueue.invokeLater(() -> {
            JFrame ex = new GitHubLive(); //Initialize snake game
            ex.setVisible(true);
        });
	}
}

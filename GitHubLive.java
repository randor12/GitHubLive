/**
 * Ryan Nicholas
 * Git Hub automatic push/pull system
 */

import java.io.IOException;
import java.io.OutputStream;
import java.lang.*;

/**
 * @author Ryan's Computer
 * @version 2019.05.08
 *
 */
public class GitHubLive {
	
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String command = "/bin/bash -c git status";
		String newPull = "/bin/bash -c git pull";
		String newCommit = "/bin/bash -c git commit -m \"New commit\"";
		String newPush = "/bin/bash -c git push";
		
		Process proc = new ProcessBuilder(command).start();
	 	OutputStream out = null;
	 	
	 	out = proc.getOutputStream();
	 	
	 	String response = out.toString();
	 	
	 	if (!response.contains("nothing to commit"))
	 	{
	 		new ProcessBuilder(newPull).start();
	 		new ProcessBuilder(newCommit).start();
	 		new ProcessBuilder(newPush).start();
	 	}
	 	
	}

}

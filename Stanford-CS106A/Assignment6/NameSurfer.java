/*
 * File: NameSurfer.java
 * ---------------------
 * When it is finished, this program will implements the viewer for
 * the baby-name database described in the assignment handout.
 */

import acm.graphics.*;
import acm.program.*;

import java.awt.Dimension;
import java.awt.event.*;
import javax.swing.*;

public class NameSurfer extends Program implements NameSurferConstants {
//public class NameSurfer extends ConsoleProgram implements NameSurferConstants {
/* Method: init() */
/**
 * This method has the responsibility for reading in the data base
 * and initializing the interactors at the bottom of the window.
 */
	private JTextField nameField;
	private JButton graphButton;
	private JButton deleteButton;
	private JButton clearButton;
	private JButton testButton;
	private NameSurferGraph graph;
	private GCanvas canvas;
	private NameSurferDataBase db;

	@Override
	public void init() {
	    // You fill this in, along with any helper methods //
		//create any collection objects		
		createController();
		db = new NameSurferDataBase(NAMES_DATA_FILE);
		graph = new NameSurferGraph();
		add(graph);		
		addActionListeners();
	}

	private void createController() {
		add( new JLabel("Name"), SOUTH);
		nameField = new JTextField(MAX_NAME_LENGTH);
		add(nameField, SOUTH);
		graphButton = new JButton("Graph"); 
		add( graphButton, SOUTH);
		deleteButton = new JButton("Delete"); 
		add( deleteButton, SOUTH);
		add(Box.createRigidArea(new Dimension(10,0)), SOUTH);
		clearButton = new JButton("Clear");
		add( clearButton, SOUTH);
		
//		add(Box.createRigidArea(new Dimension(100,0)), SOUTH);
//		testButton = new JButton("Test");
//		add( testButton, SOUTH);		
		addActionListeners();
		nameField.addActionListener(this);		
	}
	
/* Method: actionPerformed(e) */
/**
 * This class is responsible for detecting when the buttons are
 * clicked, so you will have to define a method to respond to
 * button actions.
 */
	@Override
	public void actionPerformed(ActionEvent e) {
		Object source = e.getSource();
		String name = nameField.getText().toLowerCase();
		String capitalizedName = db.capitalizeFirstLetter(name);
		if ( ( source == graphButton || source == nameField ) && checkValidEntry( name )  && graph.checkSeriesMap(capitalizedName) == false)  {
				NameSurferEntry entry = db.findEntry(name);
				graph.addEntry(entry);
		} else if ( source == clearButton ) {
			graph.clear();
		} else if ( source == deleteButton ) {
			String capitilizedName = db.capitalizeFirstLetter(name);
			graph.deleteEntry( capitilizedName );
//		} else if ( source == testButton ) {
//			graph.testEntry();
//		}
		}
		nameField.setText ( "" );
	}
	
	private Boolean checkValidEntry (String name) {
		return 0 < name.length() && name.length() < MAX_NAME_LENGTH; 
	}
	 
}

/*
 * File: NameSurferEntry.java
 * --------------------------
 * This class represents a single entry in the database.  Each
 * NameSurferEntry contains a name and a list giving the popularity
 * of that name for each decade stretching back to 1900.
 */

import java.util.*;

public class NameSurferEntry implements NameSurferConstants {
	
	private String name;
	private int[] rankArray;	
	
/* Constructor: NameSurferEntry(line) */
/**
 * Creates a new NameSurferEntry from a data line as it appears
 * in the data file.  Each line begins with the name, which is
 * followed by integers giving the rank of that name for each
 * decade.
 */
	public NameSurferEntry(String line) {
			/* iterate through the loop and mark the index when the rankings start
			 * then add the values to the rankArray as spaces are met
			 */	
			rankArray = new int[11];
			String[] helper = line.split("\\s+");
			name = helper[0];
			for (int i = 1; i < helper.length; i++) {
			rankArray[i-1] = Integer.parseInt(helper[i]);
		}						
	}

/* Method: getName() */
/**
 * Returns the name associated with this entry.
 */
	public String getName() {
		return name;
	}

/* Method: getRank(decade) */
/**
 * Returns the rank associated with an entry for a particular
 * decade.  The decade value is an integer indicating how many
 * decades have passed since the first year in the database,
 * which is given by the constant START_DECADE.  If a name does
 * not appear in a decade, the rank value is 0.
 */
	public int getRank(int decade) {
		return rankArray[decade];
	}
	
	public int[] getRankArray() {
		return rankArray;
	}

/* Method: toString() */
/**
 * Returns a string that makes it easy to see the value of a
 * NameSurferEntry.
 */
	@Override
	public String toString() {
		// You need to turn this stub into a real implementation //
		return name + " " + Arrays.toString(rankArray);
	}		
}
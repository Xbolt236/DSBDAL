import java.util.*;

public class WordCounter {

    public static void main(String[] args) {

        String paragraph = "This is a sample paragraph. It contains several words. "
                         + "We need to count the number of words in this paragraph.";

        int wordCount = countWords(paragraph);
        System.out.println("Number of words in the paragraph: " + wordCount);
    }

    public static int countWords(String paragraph) {

        // Split the paragraph into words using space as the delimiter

        String[] words = paragraph.split("\\s+");

        // Return the number of words
        return words.length;
    }
}

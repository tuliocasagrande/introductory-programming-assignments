/**
 * Created by tulio on 12/12/15.
 */
public class Triangle {
    public static void main(String[] args) {
        easiestExerciseEver();
        drawHorizontalLine(8);
        drawVerticalLine(3);
        drawRightTriangle(3);
    }

    private static void drawRightTriangle(int size) {
        for (int i = 0; i < size; i++) {
            drawHorizontalLine(i+1);
        }
    }

    private static void drawVerticalLine(int size) {
        for (int i = 0; i < size; i++) {
            drawHorizontalLine(1);
        }
    }

    private static void drawHorizontalLine(int size) {
        for (int i = 0; i < size; i++) {
            System.out.print("*");
        }
        System.out.println();
    }

    private static void easiestExerciseEver() {
        System.out.println("*");
    }

}

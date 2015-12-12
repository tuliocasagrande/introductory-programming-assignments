/**
 * Created by tulio on 12/12/15.
 */
public class Diamond {

    public static void main(String[] args) {
        drawIsoscelesTriangle(3);
        drawIsoscelesTriangle(4);
        drawDiamond(3);
        drawDiamond(4);
    }

    private static void drawDiamond(int size) {
        for (int i = 1; i <= size; i++) {
            drawTriangleLine(i, size);
        }
        for (int i = size-1; i >= 1; i--) {
            drawTriangleLine(i, size);
        }
    }

    private static void drawIsoscelesTriangle(int size) {
        for (int i = 1; i <= size; i++) {
            drawTriangleLine(i, size);
        }
    }

    private static void drawTriangleLine(int line, int size) {
        int asterisks = line*2 - 1;
        int spaces = size - line;

        for (int i = 0; i < spaces; i++) {
            System.out.print(" ");
        }
        for (int i = 0; i < asterisks; i++) {
            System.out.print("*");
        }
        System.out.println();
    }
}

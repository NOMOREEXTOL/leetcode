/**
 * leetcode59: 两层for循环
 * 0ms,39.8MB(100.0,11.17 % )
 *
 */

public class leetcode59 {
    public static void main(String[] args) {
        int n = 4;
        int[][] ans = generateMatrix(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(ans[i][j] + "\t");
            }
            System.out.println();
        }

    }


    public static int[][] generateMatrix(int n) {
        int[][] dirList = {{0,1},{1,0},{0,-1},{-1,0}};
        int dirConPara = 0;
        int accuPara = 1;

        int[][] ans = new int[n][n]; // 默认值为0
        int baseX = 0;
        int baseY = -1;


        int cirConPara = n;

        for (int i = 0; i < cirConPara; i++) {
            baseX += dirList[dirConPara][0];
            baseY += dirList[dirConPara][1];
            ans[baseX][baseY] = accuPara++;
        }

        dirConPara++;
        cirConPara--;

        while (cirConPara != 0) {
            for (int i = 0; i < cirConPara; i++) {
                baseX += dirList[dirConPara][0];
                baseY += dirList[dirConPara][1];
                ans[baseX][baseY] = accuPara++;
            }
            dirConPara = (dirConPara + 1) % 4;

            for (int i = 0; i < cirConPara; i++) {
                baseX += dirList[dirConPara][0];
                baseY += dirList[dirConPara][1];
                ans[baseX][baseY] = accuPara++;
            }
            dirConPara = (dirConPara + 1) % 4;
            cirConPara--;
        }

        return ans;
    }
}








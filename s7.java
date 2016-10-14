public class Main {
    public static void main(String[] args) {
    // write your code here
		Scanner in = new Scanner(System.in);
		int n = Integer.parseInt(in.next());
		double[][] a = new double[n][n];
		double[][] b=new double[n][n];
		double[][] prev=new double[n][n];
		for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		if(i==j) {
			prev[i][j]=1;
		}
		for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			a[i][j] = in.nextFloat();
			b[i][j]=a[i][j];
		}
		int sh=0;
		while (sh<3) {
			double[][] rez=new double[n][n];
			double[][] T=new double[n][n];
			for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			if(i==j)
			T[i][j]=1;
			double max = a[1][0];
			int maxi = 1;
			int maxj = 0;
			for (int i = 1; i < n; i++)
			for (int j = 0; j < i; j++)
			if (a[i][j] >= max) {
				max = a[i][j];
				maxi = i;
				maxj = j;
			}
			double p = 2 * max;
			double q = a[maxi][maxi] - a[maxj][maxj];
			double c;
			double s;
			double d = Math.sqrt(p * p + q * q);
			double r;
			if (q == 0) {
				c = (1 / Math.sqrt(2));
				s = c;
			} else {
				r = Math.abs(q) / (2 * d);
				c = Math.sqrt(0.5 + r);
				int sign = (int) (p * q / (Math.abs(p * q)));
				s = (Math.sqrt(0.5 - r) * sign);
			}
			T[maxi][maxi]=c;
			T[maxi][maxj]=-s;
			T[maxj][maxi]=s;
			T[maxj][maxj]=c;
			b[maxi][maxi] = c * c * a[maxi][maxi] + s * s * a[maxj][maxj] + 2 * c * s * a[maxi][maxj];
			b[maxj][maxj] = s * s * a[maxi][maxi] + c * c * a[maxj][maxj] - 2 * c * s * a[maxi][maxj];
			b[maxi][maxj] = 0;
			b[maxj][maxi] = 0;
			for (int m = 0; m < n; m++)
			if ((m != maxi) && (m != maxj)) {
				double k = c * a[m][maxi] + s * a[m][maxj];
				b[maxi][m] = k;
				b[m][maxi] = k;
				k = -s * a[m][maxi] + c * a[m][maxj];
				b[maxj][m] = k;
				b[m][maxj] = k;
			}
			for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				for(int m=0;m<n;m++)
				rez[i][j]+=prev[i][m]*T[m][j];
			}
			for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				prev[i][j]=rez[i][j];
				a[i][j] = b[i][j];
			}
			sh++;
			for(int i=0;i<n;i++)
			{
				for (int j = 0; j < n; j++)
				{
					// prev[i][j]=Math.round(prev[i][j]*1000)/1000;
					System.out.print(prev[i][j]);
					System.out.print(" ");
				}
				System.out.println();
			}
		}
		for(int i=0;i<n;i++)
		{
			for (int j = 0; j < n; j++)
			{
				a[i][j]=a[i][j]*1000;
				int k=(int)Math.round(a[i][j]);
				a[i][j]=(double)k/1000;
				System.out.print(a[i][j]);
				System.out.print(" ");
			}
			System.out.println();
		}
		for(int i=0;i<n;i++)
		{
			for (int j = 0; j < n; j++)
			{
				prev[i][j]=prev[i][j]*1000;
				int k=(int)Math.round(prev[i][j]);
				prev[i][j]=(double)k/1000;
				System.out.print(prev[i][j]);
				System.out.print(" ");
			}
			System.out.println();
		}
    }
}
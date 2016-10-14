#include <stdio.h>
#include <iostream>
#include <conio.h>
#include "QR_Decomposition.h"
using namespace std;

void f(double **an, double *bn, int m)
{
    int i, j;
    cout << " \n";
    for (i = 0; i <= m; i++)
    {
        for (j = 0; j <= m; j++) cout << " " << an[i][j];
        cout << "   " << bn[i] << " \n";
    }
}
double * SimpleIteration(cMatrix a, double * bn)
{
    int i, j, k, l, m, n, jj, kk, j1;
    double mi, d;
    double **an = new double*[a.m];
    for (int count = 0; count < a.m; count++)
        an[count] = new double[a.n];
    for (int count_row = 0; count_row < a.m; count_row++)
        for (int count_column = 0; count_column < a.n; count_column++)
            an[count_column][count_row] = a.A[count_column * a.n + count_row];/// a.A[count_row][count_column];
    //double an[a.m][a.n];
   /* { { 81, 2, 3, 2 },
    { 2, 899, 3, 3},
    { 2, 3, 1, 8} ,
    {1, 2, 3, 4}
    };*/
   /* double bn[size] = { 3, 4, 5, 7};
    double xn[size];*/
   // double * bn = new double[a.n];
    double * xn = new double[a.n];
     m = a.n -1;
    cout.precision(18);
    f(an, bn, m);
    n = m - 1;
    k = 0;
    for (j = 0; j <= n; j++)
    {
        l = 1;
        for (i = k + 1; i <= m; i++)
        {
            mi = an[k + l][k] / an[k][k];
            bn[i] = bn[i] - mi*bn[k];
            for (j1 = k; j1 <= m; j1++) an[k + l][j1] = an[k + l][j1] - mi*an[k][j1];
            l = l + 1;
        }
        k = k + 1;
    }
    //    f(an,bn,m);
    xn[m] = bn[m] / an[m][m];
    k = 1;
    d = 0;
    for (i = n; i >= 0; i--)
    {
        kk = 1;
        for (jj = 1; jj <= k; jj++)
        {
            d = d + an[i][i + kk] * xn[i + kk];
            kk = kk + 1;
        }
        xn[i] = (bn[i] - d) / an[i][i];
        d = 0;
        k = k + 1;
    }
    cout << " \n";
    cout << " \n";
    for (i = 0; i <= m; i++) cout << " " << xn[i] << " \n";

  //  getch();
   // cin.get();
    return xn;
  
}
int main(int argc, char* argv[]) {

    double temp[] = { 7, 9, 3, 5,    9, 46, 12, 14,    3, 12, 4, 4,   5, 14, 4, 6 };
    cMatrix A__(4, 4, temp);
    //double temp[] = {4,3,0,2, 2,1,2,1, 4,4,0,3};
    // A__(3,4,temp);
    cMatrix Q__(1, 1), R__(1, 1);// , S__(1, 1);

    //A__.householderBidiagonalization(Q__, R__, S__);
    A__.householderDecomposition(Q__,R__);
    cout << "Matrica A__ \n";
    A__.output();
    cout << "Matrica Q__ \n";
    Q__.output();
    cout << "Matrica R__ \n";
    R__.output();
    cout << "((Q__.transpose())*Q__)\n";
    ((Q__.transpose())*Q__).output();
   // cout << "Matrica S__ \n";
   // S__.output();
   // cout << "Matrica Q__*R__*S__ \n";

   // (Q__*R__*S__).output();
   // cout << "Q__*Q__";

   // (Q__*Q__.transpose()).output();
   // cout << "S__*S__.transpose()) \n";
   // (S__*S__.transpose()).output();
   // cout << "Matrica Q*S \n";
   // (Q__*S__).output();
   // //cout<<"(Q__*S__)*(Q__*S__).transpose.output() \n";
   // //(Q__*S__*(Q__*S__).transpose).output();
   //double bn[4] = { -1.263, -9.536, -6.7932, 7.1634 };
    cout << ("Solve Linear System  : Q__ *Y = b\n                                               Q                                           b");
    double bn[4] = {48,151,39,59 };
    double * xn = new double[4];
    xn=SimpleIteration(Q__, bn);
    cout << ("Solve Linear System  : R__ *X = Y\n                                               R                                           Y");
    //double bn[4] = { 6,-12,1,3 };
    //double * xn = new double[4];
    xn = SimpleIteration(R__, xn);
   // //xn = SimpleIteration(R__*S__, xn);
   // double temp[] = { 3, 1, -1, 2,    -5, 1, 3, -4,    2, 0, 1, -1,   1, -5, 3, 3 };
    cMatrix X__(4, 1, xn);
    cout << ("Check the solution of QR method\n A*X =   ");
    (A__*X__).transpose().output();
    for (int s = 1; s < 100; s++)
    std::cin.get();

    return 0;
}
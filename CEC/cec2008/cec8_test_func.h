#ifndef CEC8_TEST_FUNC_H
#define CEC8_TEST_FUNC_H

#include <math.h>

#define abss(a)     (a<0 ? (-a) : a)
#define amax(a , b)  (a>b ?   a  : b)
#define amin(a , b)  (a>b ?   b  : a)

double func(int, int, double*);
double Shifted_Sphere(int, double*);
double Schwefel_Problem(int, double*);
double Shifted_Rosenbrock(int, double*);
double Shifted_Rastrigin(int, double*);
double Shifted_Griewank(int, double*);
double Shifted_Ackley(int, double*);
double Shifted_Weierstrass(int, double*);

double runtest(double*, int, int);

#endif

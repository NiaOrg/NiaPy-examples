#ifndef CEC19_TEST_FUNC_H 
#define CEC19_TEST_FUNC_H

#define INF 1.0e99
#define EPS 1.0e-14
#define E  2.7182818284590452353602874713526625
#define PI 3.1415926535897932384626433832795029


double runtest(double*, int, int);
void cec19_test_func(double*, double*, int, int, int);
void schaffer_F7_func (double*, double*, int, double*, double*, int, int);
void griewank_func (double*, double*, int, double*, double*, int, int);
void ackley_func (double*, double*, int, double*, double*, int, int);
void weierstrass_func (double*, double*, int, double*, double*, int, int);
void rastrigin_func (double*, double*, int, double*, double*, int, int);
void step_rastrigin_func (double*, double*, int, double*, double*, int, int);
void schwefel_func (double*, double*, int, double*, double*, int, int);
void escaffer6_func (double*, double*, int, double*, double*, int, int);
void happycat_func (double*, double*, int, double*, double*, int, int);
void shiftfunc (double*, double*, int, double*);
void rotatefunc (double*, double*, int, double*);
void sr_func (double*, double*, int, double*, double*, double, int, int);
void asyfunc (double*, double*, int, double);
void oszfunc (double*, double*, int);
void Lennard_Jones(double*, int, double*);
void Hilbert(double*, int, double*);
void Chebyshev(double*, int, double*);

#endif

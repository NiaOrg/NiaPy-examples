#include "cec8_test_func.h"
#include "data.h"

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

static double pi;
static double e;

double runtest(double* x, int dim, int fnum) {
	return func(fnum, dim, x);
}

double func(int func_number , int dim , double* x) {
	pi = acos(-1.0), e = exp(1.0);
	if(dim > 1000) dim = 1000;
	switch(func_number){
		case 1 : return Shifted_Sphere(dim, x);
		case 2 : return Schwefel_Problem(dim, x);
		case 3 : return Shifted_Rosenbrock(dim, x);
		case 4 : return Shifted_Rastrigin(dim, x);
		case 5 : return Shifted_Griewank(dim, x);
		case 6 : return Shifted_Ackley(dim, x);
		default : 
					printf("Error : Function number out of range\n");
					exit(0);
					break;
	}
}

double Shifted_Sphere(int dim , double* x){
	int i;
	double z;
	double F = 0;
	for(i=0;i<dim;i++){
		z = x[i] - sphere[i];
		F += z*z;
	}
	return F + f_bias[0];
}

double Schwefel_Problem( int dim , double* x ){
	int i;
	double z;
	double F = abss(x[0] - schwefel[0]);
	for(i=1;i<dim;i++){
		z = x[i] - schwefel[i];
		F = amax(F , abss(z));
	}
	return F + f_bias[1]; 
}

double Shifted_Rosenbrock( int dim , double* x ){
	int i;
	double z[dim];
	double F = 0;
	for(i=0;i<dim;i++) z[i] = x[i] - rosenbrock[i] + 1;   
	for(i=0;i<dim-1;i++) F = F + 100 * (pow((pow(z[i], 2) - z[i + 1]) , 2)) + pow((z[i] - 1) , 2);
	return F + f_bias[2]; 
}

double Shifted_Rastrigin( int dim , double* x ) {
	int i;
	double z;
	double F = 0;
	for(i=0;i<dim;i++){  
		z = x[i] - rastrigin[i];
		F = F + ( pow(z,2) - 10*cos(2*pi*z) + 10);
	}
	return F + f_bias[3]; 
}

double Shifted_Griewank( int dim , double* x ){
	int i;
	double z;
	double F1 = 0;
	double F2 = 1;
	for(i=0;i<dim;i++){       
		z = x[i] - griewank[i];
		F1 = F1 + ( pow(z,2) / 4000 );
		F2 = F2 * ( cos(z/sqrt(i+1)));
	}
	return (F1 - F2 + 1 + f_bias[4]); 
}

double Shifted_Ackley( int dim , double* x ){
	int i;
	double z;
	double Sum1 = 0;
	double Sum2 = 0;
	double F = 0;
	for(i=0;i<dim;i++){   
		z = x[i] - ackley[i];
		Sum1 = Sum1 + pow(z , 2 );
		Sum2 = Sum2 + cos(2*pi*z);
	}
	F = -20*exp(-0.2*sqrt(Sum1/dim)) -exp(Sum2/dim) + 20 + e + f_bias[5];
	return F; 
}

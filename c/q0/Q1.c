#include <stdio.h>

void quad_x(double a, double b, double c, double *r1, double *r2){
    *r1 = (-b + sqrt(b*b - 4*a*c))/(2*a);
    *r2 = (-b - sqrt(b*b - 4*a*c))/(2*a);
}

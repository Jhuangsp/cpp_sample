#include <iostream>
#include "main.h"

using namespace std;

/*extern "C" {
    int hello();
	int add_int(int, int);
	float add_float(float, float);
}
*/
int add_int(int num1, int num2){
    return num1 + num2;
}
float add_float(float num1, float num2){
    return num1 + num2;
}
int hello(){
	cout << "Hello World!";
	return 23;
}
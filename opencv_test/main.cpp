#include "opencv2/highgui/highgui.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(){

    string location = "81484897_583884578857893_3054186664780890112_n.png" ;

    Mat im = cv::imread(location ,1 );
    if (im.empty())
    {
        cout << "Cannot open image!" << endl;
        return -1;
    }

    std::cout << im.size;

    return 0;
}
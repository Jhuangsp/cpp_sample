
# g++ -I"C:\opencv\install\include" -L"C:\opencv\install\x64\mingw\lib" -L"C:\opencv\install\x64\mingw\bin"  cv2.cpp -lopencv_core3412 -lopencv_highgui3412 -lopencv_imgproc3412 -lopencv_imgcodecs3412 -o cv2
from ctypes import cdll
lib = cdll.LoadLibrary("./cv2.dll")
lib.test_opencv()
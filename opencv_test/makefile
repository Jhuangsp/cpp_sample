
CC=g++
INCLUDES = C:\\opencv\\build\\include
LIBDIRS = C:\\opencv\\build\\x64\\vc15\\lib
cv2.dll:cv2.cpp
    $(CC) -c cv2.cpp
    $(CC) -static -shared -I $(INCLUDES) -L $(LIBDIRS) -o cv2.dll cv2.o
clean:
    rm -f cv2.o
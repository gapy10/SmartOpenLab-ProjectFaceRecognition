# SmartOpenLab-ProjectFaceRecognition

This repository serves for educational purposes. It includes files that are under Intel Licence Agreement. Before using
any part of the repository, please take your time to understand terms and conditions of above-mentioned licence.

<h3>Prerequisites</h3>

Source code use is intended for Linux users only. OpenCV and Dlib are available for Windows and Mac as well, but it has
not been tested yet.

Requirements:
* Linux machine: this section will provide installation details for both Debian-based and RPM-based systems, tested on
Ubuntu 18.04 and Fedora 29
* Laptop with a built-in web camera
* Python 3.x, tested on Python 3.7.1

<h3>Installation of OpenCV and Dlib</h3>

We can use ```pip``` to install OpenCV. In case of errors, you might have to install from source. For that, look at
[this section](#bfs-opencv). There are four different packages, and you must select <b>only one</b> of them. This is a
set of unofficial pre-built OpenCV packages. Check <a href="https://docs.opencv.org/master/">here</a> for official
documentation.

* For standard desktop environments:
    * ```pip3 install opencv-python``` if main modules are needed.
    * ```pip3 install opencv-contrib-python``` if main and ```contrib``` modules are needed
* For headless environments (no GUI, beloved CLI only)
    * ```pip3 install opencv-python-headless``` if main modules are needed
    * ```pip3 install opencv-contrib-python-headless``` if main and ```contrib``` modules are needed

<a name="bfs-opencv">If you will/want to build OpenCV from source</a>:
* For <a href="https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/">Debian-based</a> systems
* For <a href="https://docs.opencv.org/3.4/dd/dd5/tutorial_py_setup_in_fedora.html">RPM-based</a> systems


<h4>Debian-based systems</h4>

For Dlib, you need to install a few dependencies. Some of those might already be present on your system.

    $ sudo apt update
    $ sudo apt install build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev
                       python python-dev python-pip python3 python3-dev python3-pip

If you are running Python in a virtual environment (like you should be), then you can simply use

    $ pip3 install numpy
    $ pip3 install dlib

<h4>RPM-based systems</h4>

First, <a href="http://dlib.net/compile.html">download and extract latest version of Dlib</a> in your home folder. Next,
you will probably need to install the following:

    $ sudo dnf install cmake gcc-c++

Move to the extracted folder and run

    $ cd examples
    $ mkdir build && cd build
    $ cmake ..
    $ cmake --build . --config Release

Installation of ```face_recognition``` is common for both types and can be accomplished with ```pip```
package manager.

    $ pip3 install face_recognition

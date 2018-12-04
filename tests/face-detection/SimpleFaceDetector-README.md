This repository serves for educational purposes. It includes files that are under
Intel Licence Agreement. Before using any part of the repository, please take
your time to understand terms and conditions of above-mentioned licence.

<h1>OpenCV</h1>

<a href="https://opencv.org/">OpenCV</a> is a computer vision library implementing
machine learning algorithms that enables accelerated use of machine perception.
It currently includes more than 2000 optimized algorithms that can be used for
facial detection and recognition, object identification etc. Check <a href="https://opencv.org/about.html">here</a> for more information on OpenCV.

<h4>Prerequisites</h4>

Source code and instructions are written for Linux users, I will try my best to provide instruction set for Debian and
RPM based systems.

Requirements:
* Linux distribution (assuming you are using Ubuntu or Fedora)
* Python 3.x (tested on Python 3.7.1)
* Laptop with a web camera

For Ubuntu or Debian-based systems, follow <a href="https://www.learnopencv.com/install-opencv-4-on-ubuntu-18-04/">these
</a> installation instructions. Fedora or other RPM-based systems should instead follow <a href="https://www.docs.opencv.org/3.1.0/dd/dd5/tutorial_py_setup_in_fedora.html">these</a>
instructions.

I personally recommend use of <a href="https://www.jetbrains.com/pycharm/">PyCharm</a>, Python IDE developed by JetBrains.
Installation of necessary components, such as Python libraries, is simplified.

<h1>Face detection</h1>

<h4>Theoretical background</h4>

<b>Attention:</b> this is a summary of <a href="http://eyalarubas.com/face-detection-and-recognition.html">this article</a>.

In order to detect a face, we need to define the general structure of a face, and since humans have relatively similar
facial structure, we can define components such as eyes, nose, mouth, ears etc. We do not need an accurate match to determine
if a given picture includes a face or not: this is called <a href="https://en.wikipedia.org/wiki/Template_matching">
Template matching</a>.

Furthermore, rather than determining if the image does contain a face, we can more quickly determine if the image does
not contain a face; because eliminations can be done quickly, while acceptance of faces will require more time. We call
such process a <b>cascading process</b>. This is an oversimplification of so-called
<a href="https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html">Haar cascade</a>.

Another classification method is called <a href="https://en.wikipedia.org/wiki/Local_binary_patterns">LBP</a> or Local
binary patterns.

<h4>Source code</h4>

You have the following files:
* XML classifiers (I am using Haar cascade)
    * ```haarcascade_eye.xml```
    * ```haarcascade_frontalface_default```
    * ```haarcascade_smile.xml```
* Python source code
    * ```SimpleFaceDetector-HaarCascade.py```: actual implementation of said cascade. It recognizes face, eyes and smile, works with
    multiple faces as well.

In case of false positives, adjust parameters in the source code. <b>Tip:</b> try to use your ID or driver licence for
detection. See if image quality affects the accuracy.

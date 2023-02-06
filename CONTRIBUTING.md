# Contributing

openMTPK welcomes any and all contributors! There are **many** ways to contribute to openMTPK. New implementations, updates to source code, documentations, language API, and much more. 

# Needed Help

These are the current fixes, ideas, and implementations involved with openMTPK. Contributors are welcome to open a pull request, the maintainer ([me](github.com/akielaries)), will take care of assuring passing tests and checks as far as github workflows.

1. The `Machine and Deep Learning Module` a continuous effort and I find is the most important and reusable module of the openMTPK project for programmers, students, researchers, etc. also meaning it requires the most help regarding implementations, tests, verifications, and any effort helping assure the accuracy of the implemented models. 
   
   *  To prove the existing and future implemented models and methods provide some use, benchmarking/comparisons against industry-grade and open-source projects like **PyTorch**, **TensorFlow (including the Keras interface)**, and **Sci-kit Learn** will prove beneficial. 

2. Perfecting the **Linux** and **OSX** installations with `CMake`. 
   
   * **Windows** is not currently on my agenda. Installation and support for Windows systems is handed off to those who need it or if I have a plethora of spare time. 
   
   * `CMake` installation currently only works with **Linux**, issues arise on **OSX** when it comes to the steps regarding GoogleTest.

3. Creating bindings for languages.
   
   * The stable `Python API` makes use of **SWIG** and **distutils** to wrap the source C++ code into a shared library, creating an overarching `openmtpk.py` file depending on the compiled C++ lib and acting as the callable Python module, making use of **Github Actions** to publish the package to PyPI with support for just about all `Linux` distros and `OSX` versions and platform architectures, see [here](https://pypi.org/project/openmtpk/#files). If this process can be polished it is highly welcomed. 
   
   * Properly implementing, testing, and updating the unstable/inprogress APIs for `R`, `OCaml`, and `Fortran`. 
     
     * This will require knowledge of the languages and openMTPK in order to create samples for the respective languages in the [samples](https://github.com/akielaries/openMTPK/tree/main/samples) folder.
     
     * As of now partial working steps for doing this with **SWIG** is present in each of the respective languages folders. 

4. Formalize openMTPK for real world applications.
- * Threading, acceleration, optimization, etc. This could include creating a 1-stop-shop implementation using some sort of cross-platform library/framework/technique that enable CPU and/or GPU exploitation just like popular libraries that are capable of handling extremely large data sets (PyTorch, TensorFlow, etc.).
  * pthreads, openCL, openMP? A custom take at this could prove difficult to implement and maintain. 

- 5. Updates to Documentation published with Doxygen to https://akielaries.github.io/openMTPK/. This is needed for both the C++ and Python uses while the former contains a decent amount already.

## 

# Bug fixes

* If you have a bug fix please submit a pull request with details highlighting what you are fixing, how you replicated it, and how you tested your fix. For fixes that include confidential information please feel free to send me an email [akiel@akiel.org](mailto:akiel@akiel.org)

# Code Style

openMTPK attempts to follow the neat [Google C++ Style Guide]([Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) for naming while a custom clang-format file is used for tidying formatting. 



Hopefully these guidelines are clear enough for you to begin contributing to this project. As always email me akiel@akiel.org for questions.
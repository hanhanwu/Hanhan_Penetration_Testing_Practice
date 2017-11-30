

***************************************************************************

OVERVIEW

* Python, Ruby and Perl are <b>interpreted languages</b>, the code will be turned into machine leanguage and execute. C, C++ are compiled languages, they will be compiled before running, and therefore they are faster. But, compiled code is generated for a specific system type and distribution, cannot be moved through a geterogeneous environment (an environment that has ultiple system types and different distributions), while interpreted code can be portable as long as the interpreter is avilable.
* Python is Dynamiclly Typed, which means variables are interpreted at runtime, so you don't need to define variable size or type

***************************************************************************

BASICS BUT MORE SECURE

* Better to put `#!/usr/bin/env python` at the top of each python file, so that OS (Linux, Unix, OSX) can determine which interpreter to run absed on what is set in `PATH` environment variable. Windows will ignore this line and treat it as a comment.

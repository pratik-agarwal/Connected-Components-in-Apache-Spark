# Connected Components in Apache Spark


### Problem
Your task in this assignment is to implement efficient end-to-end Apache Spark program for finding connected components. We make several assumptions:
1. Undirected graph on which we are operating is too large to be represented in the memory of a single compute node.
2. The graph is represented by a list of edges in the form source target , where source is integer representing source vertex id, target is intege
representing target vertex id, and source and target are separated with single space.
3. Graph has no self-loops (i.e. source = target ) and no particular ordering of source , target is assumed.


### Instructions

1. Create and use folder A2 to implement your program.
2. Your main program, which will be invoked via spark-submit , must be named a2.xxx , where xxx is the language specific extension, e.g. py for Pytho
scala for Scala, etc.
3. You can use any language you like as long as it works with Apache Spark. However, if you decide to use a compiled language, e.g. Scala, Java, you mus
provide a build system and Makefile to invoke it. In the essence, by running make in the main folder we should receive a2 executable, ready fo
submission with spark-submit .
4. Your application should be taking one input command line argument: the name of a file or directory containing the graph to analyze. You may assume tha
input is always correct and input files are passed properly.
5. Your application should create a folder or file, with output in the form vertex label , where vertex is vertex id, and label is the label of connecte
component to which vertex belongs. Vertex and label should be separated by a white space.
6. Once your solution is ready follow up with submission (see instructions below).


### Submission

To submit your code follow these steps:
1. Make sure that your main code contains your First, Last and UBIT names (as in previous assignments).
2. Remove binary and other unrelated files from your project directory.
3. Make sure that your project directory is named A2 and make tarball A2.tar out of it. Make sure that the resulting tarball indeed contains A2 directory (i.
untarring A2.tar should produce your A2 directory).
4. Follow to autograder (https://autograder.cse.buffalo.edu) to make your submission.



### Grading

1. A cluster of 8+ nodes will be used for testing.
2. Apache Spark 2.2.0, as configured at CCR, will used for testing.
3. Your code will be tested for scalability on large instances (up to the memory limit) and graded 0-100 points based on the correctness and scalability. 4. If your code does not compile/run, you will get 0 points.
5. If your code produces systematically incorrect answers, you will get 0 points.
6. There is no late submission policy! If you do not submit on time, you will get 0 points.



### Final Remarks

1. This is a fun project, which you can showcase to potential employers. Make it well.
2. This is challenging project, start early, you will have to play with CCR and that takes time!!!
3. By now you should know not to look for the solution on internet :-)
4. If the assignment instructions are not clear, use office hours and simply talk to me/ask for clarification!
5. I use automated plagiarism detection tools. It includes huge database of codes from the Internet and past courses I offered. In other words, if you decid
to cheat I will catch you. You will get F and fail the course (see syllabus for details (../UB-IntroPDP-Syllabus.pdf)). This is not because I am mean or do no like you. This is because I value and protect hard working students who do not cheat.
© 2017 Jaroslaw Zola

 

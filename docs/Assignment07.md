# Introduction to Pickling and Structured Error Handling
## Introduction 

As programs expand and become more complicated, the amount of computing space increases. Pickling uses binary to save Python acquired data with less required space. Additionally, structured error and handling allows the user to interpret errors that may occur while interacting with a program, without having to interpret cryptic Python error expressions. 

## Converting program into Binary 

Using last week’s assignment as template for this week’s assignment, I added two pickling functions to store and read my programs acquired data as raw binary, Figure 1. 

![Screen Shot 2022-12-01 at 2 27 03 PM](https://user-images.githubusercontent.com/118510934/205172359-68b3e155-6192-48cc-aa9d-eb6269c82827.png)

I first establish how I want the file to open. By using “rb”, I will be able to read the input data as a binary file. This is called upon using pickle.load(file). The next modification would be to save any data as a binary file instead of text. Paralleling the read function, “ab” was used instead of “a” to allow the pickling to occur. This was called upon by pickle.dump. By doing this, the data is saved as raw binary, Figure 2. 

![Screen Shot 2022-12-01 at 2 29 27 PM](https://user-images.githubusercontent.com/118510934/205172722-cc1d3fd1-a197-4573-9295-0a2f63b5cb3e.png)

## Using Structured Error Handling 

I wanted a custom error so that the user was not providing integers for the name and status values. To do this I used a “try and except” function to assess whether the input is a digit. If so, then an error message is returned, Figure 3.  

![Screen Shot 2022-12-01 at 2 29 23 PM](https://user-images.githubusercontent.com/118510934/205172790-d8462d31-c800-4e15-ae48-2cbf17c20c27.png)

## Conclusion 

Pickling is another beneficial function of Python. It stores data with less space than text and can be translated and read as a normal text file. Additionally, the use of error handling within a program allows you to catch any undesirable provided information in a complicated program without confusing the user.  

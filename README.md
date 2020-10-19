# SREAssignment
### [Git repo](https://github.com/harithadesikan23/SREAssignment.git)

**Project components:**
    The tool is used to calculate the structural similarity of different image pairs and also find out the cost of the computation. The project folder contains a main python script (SRETool.py) which performs the operations stated above, it takes a csv file as input (Input.csv) and calculates a similarity score for the image pairs along with the time taken to compute the score and inserts the results into an output csv file (Output.csv). Sample image pairs are also present in the project folder (Firstpic.jpg & Secondpic.jpg, Sunset1.jpg & Sunset2.jpg, Soccerball1.jpg & Soccerball2.PNG). The Input.csv file uses these images to calculate the score and elapsed time. 
The project also contains a unittest script (TestSRETool.py) which takes TestInput.csv as the input csv file. 

**Instructions to run the tool:**
    The project uses python 3.8.6 and pip to install the required packages. Additionally it requires the numpy, pandas and skimage packages to be installed. You can install them using the below pip commands:
        `pip install numpy`
        `pip install pandas`
        `pip install skimage`

   Start using the tool by cloning the git repo contents to a local folder. Later open a command line terminal and navigate to the folder and execute the python script (SRETool.py). 
        For Example - `python .\SRETool.py`

    **Note:** Please change the absolute path for the images present in the Input.csv as applicable to your system.

**Approach to developing the tool:**
    I came across a lot of python libraries like PIL, skimage and opencv that can deal with image comaprisons and found skimage to be the most appropriate as it comes with a method to calculate the structural similarity index between images. But since the method delivers a score of 1 for exactly similar image pairs, I had to write a conversion module that converts the score from a range of [-1,1] to [2,0]. Another problem was that the method did not work on images with different dimensions and so I had to crop the second image pair based on the first image pair's dimensions if they were different. 

**Answer to the considerations:**
    1. In order to make sure my code works, a unit test script is written along with a sample input. The test passes which proves the correctness of the application.
    2. Bjorn can read the README that will provide him the instructions he needs to run the application.
    3. Ferris can have a local branch created for himself in the git repo and make changes if required and I shall review the code before its being merged to the master branch.
    4. Since the master branch is the one having the latest version of the application at any minute, Bjorn can be rest assured that he is using the latest version. He can pull the master branch to run the latest version of the application.

# SREAssignment
### [Git repo](https://github.com/harithadesikan23/SREAssignment.git)

**Project components:**
    The tool is used to calculate the structural similarity of different image pairs and also find out the cost of the computation. The project folder contains a main python script (SRETool.py) which performs the operations stated above, it takes a csv file as input (Input.csv) and calculates a similarity score for the image pairs along with the time taken to compute the score and inserts the results into an output csv file (Output.csv). Sample image pairs are also present in the project folder (Firstpic.jpg & Secondpic.jpg, Sunset1.jpg & Sunset2.jpg, Soccerball1.jpg & Soccerball2.PNG). The Input.csv file uses these images to calculate the score and elapsed time. 
The project also contains a unittest script (TestSRETool.py) which takes TestInput.csv as the input csv file. 

![Workflow](Workflow Chart.png)

**Instructions to run the tool:**
**For Windows:**
    1. Python 3.8.6 can be installed from a web based installer on Windows (setup the path variable if needed) and then install pip to install the packages. To install pip, download get-pip.py file from the internet and run the below command from a terminal.
        `python get-pip.py`
    2. Before installing the packages, a virtual environment can be created using the below command from a terminal.
        `py -m venv env`
    2. Now, go to the project folder on a terminal and activate the virtual environment using the below command:
        `.\env\Scripts\activate`
    3. The project requires numpy, pandas and scikit-image packages to be installed. You can install them using the below pip commands:
        `pip install numpy`
        `pip install pandas`
        `pip install scikit-image`
        `pip install PyQt5`
 **For Mac:**
    1. Install homebrew if not already installed as it will be used to install python on mac.
    2. Now, install python and set up path variable in the ~/.bash_profile file. Note that pip3 comes installed with python3.
        `$ brew install python3` 
    3. Install virtual environment using below command from a terminal:
        `$ pip install virtualenv`
    4. Create the virtual environment using below command from a terminal:
        `$ virtualenv -p python3 <desired-path>`
    5. Activate the environment using below command from the project folder location:
        `$ source <desired-path>/bin/activate`
    6. The project requires numpy, pandas and scikit-image packages to be installed. You can install them using the below pip commands:
        `pip install numpy`
        `pip install pandas`
        `pip install scikit-image`
        `pip install PyQt5`

   Start using the tool by cloning the git repo contents to a local folder. Later open a command line terminal and navigate to the folder and execute the python script (SRETool.py). 
        For Example - `python .\SRETool.py`

    **Note:** Please change the absolute path for the images present in the Input.csv as applicable to your system.

**Approach to developing the tool:**
    I came across a lot of python libraries like PIL, skimage and opencv that can deal with image comaprisons and found skimage to be the most appropriate as it comes with a method to calculate the structural similarity index between images. But since the method delivers a score of 1 for exactly similar image pairs, I had to write a conversion module that converts the score from a range of [-1,1] to [2,0]. Another problem was that the method did not work on images with different dimensions and so I had to crop the second image pair based on the first image pair's dimensions if they were different. 

**Answer to the considerations:**
    1. In order to make sure my code works, a unit test script is written along with a sample input to test the correctness of the application.
    2. Bjorn can refer the README that will provide him instructions to run the application.
    3. Ferris can have a local branch created for himself in the git repo and make changes if required followed by a code review before its being merged to the master branch.
    4. Since the master branch is the one having the latest version of the application at any minute, Bjorn can be rest assured that he is using the latest version. He can pull the master branch to run the latest version of the application.

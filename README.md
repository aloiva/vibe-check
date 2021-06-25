# Vibe Check

This simple command line python program makes use of Natural Language ToolKit - nltk - to analyse the user input text and return on a scale of -1 to 1 the level of positivity or as stated by the program as "happiness score". The program then proceeds to print a random emoticon based on the happiness score from a set of five predefined levels - excited, happy, neutral, sad and melancholic. Based on the score, the user will either be asked to answer a few questions or proceeds to prompt for the next input. If the user is asked to answer a few questions based on pet preference, the program proceeds to display a picture of the certain pet chosen. User can enter `exit` any time of prompt to terminate the program.


## External libraries used:
- NLTK
- Pillow



## Prerequisites
1. NLTK
   1.  Install the package using pip.
   
       ```
       pip install nltk
       ```
   2.  Run `python` command and the following commands in order to download required module:
   
       ```
       import nltk
       ```
       ```
       nltk.downloader.download('vader_lexicon')
       ```
2. Pillow
   1. Install the package using pip.
   
      ```
      pip install Pillow
      ```
      

For other details, check out the official website for [NLTK](https://www.nltk.org/index.html) and [Pillow](https://pillow.readthedocs.io/en/stable/installation.html).



## Installation and Execution
   1. Clone the repo locally.
      
      ```
      git clone https://github.com/aloiva/vibe-check.git
      ```
   2. Run `main.py` in the terminal using
   
      ```
      python main.py
      ```

## Screenshots

### Sample Welcome

[![Sample-welcome.jpg](https://i.postimg.cc/htgN14Nv/Sample-welcome.jpg)](https://postimg.cc/CzPvF0hp)

### Sample input and output - 1
<br>

[![sample-input-and-output-1.jpg](https://i.postimg.cc/8PgYTPp4/sample-input-1.jpg)](https://postimg.cc/5jpg3JFQ)

### Sample input and output - 2

[![sample-input-and-output-2.jpg](https://i.postimg.cc/66Y6FSLM/sample-input-2.jpg)](https://postimg.cc/K43yM0WT)

Output

[![output-2.jpg](https://i.postimg.cc/ZYg29xTT/output-2.jpg)](https://postimg.cc/s1YwqSQ8)

## Customise your output emoticons

To cutomise the output emoticons, make changes to the `.txt` files present in `assets/emoticons` folder.

- Enter an emoticon in a new line to add it.
- Delete the line with emoticon to remove it.

   > Do not leave a blank line in any of the files, else there is a chance of getting a null output.

## Customise your output images

1. To add or remove the images, upload or delete the .jpg files in the `assets/img/<pet>` folder where <pet> is to be replaced by any of the three pets mentioned - cats, hamsters and bunnies.
   > Remember to rename the .jpg to an integer.jpg following the name of numerically last file in the folder.
2. Change the value of respective constants in the source code to the present total number of images.
      Example:
      
      ```
      CATS = <enter number of images in the folder assets/img/cats>
      ```
      ```
      HAMSTERS = <enter number of images in the folder assets/img/hamsters>
      ```
      ```
      BUNNIES = <enter number of images in the folder assets/img/bunnies>
      ```
## About
- Written by [@aloiva](https://github.com/aloiva)
  - Reach out to me at [LinkedIn](https://www.linkedin.com/in/pranavavedagnya/)
- Project Vibe Check - https://github.com/aloiva/vibe-check

## Acknowledgements
The program is written as the final project for Code in Place and makes use the concept of conditional statements, loops, lists, dictionaries, images and file handling as taught by the course.
   
Thank you Code in Place for the wonderful one month filled with learning. (\*^▽^\*)

###### © Pranava, 2021

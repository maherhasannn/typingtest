from time import time

# calculate the accuracy of input prompt
def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# calculate the speed in words per minute
def typingSpeed(iprompt, stime, etime):
    global time
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed

# calculate total time elapsed
def timeElapsed(stime, etime):
    time = etime - stime

    return time

if __name__ == '__main__':
    RED =  '\u001b[31m'
    GREEN = '\u001b[32m'
    RESET = "\033[0m"
    prompt = "You are gay"
    print("Type this:- '", prompt, "'")
    print(RED + "This is red text" + RESET)
    print(GREEN + "This is green text"+ RESET) 

    # listening to input ENTER
    input("press ENTER when you are ready!")

    # recording time for input
    stime = time()
    iprompt = input()
    etime = time()

    # gather all the information returned from functions
    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    # printing all the required data
    print("Total Time elapsed : ", time, "s")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", errors, "errors")


    

#     This code appears to be a simple Python program that calculates typing speed and accuracy when given a specific prompt. Let's break down the code and explain its functionality:

# The code imports the time function from the time module, which is used to measure the time taken for typing.

# The typingErrors function is defined to calculate the number of typing errors in the provided input text.

# It takes a single argument, prompt, which is the expected text to be typed.
# It initializes a global variable iwords.
# It splits the prompt text into words and stores them in the words list.
# It initializes an errors variable to count the typing errors.
# The function then iterates through the words in both the iwords list (presumably set elsewhere in the code) and the words list to compare each word. It checks whether the words match and if they don't, it increments the errors count.

# The function returns the total number of typing errors.

# The typingSpeed function is defined to calculate the typing speed in words per minute (WPM).

# It takes three arguments: iprompt (the input text), stime (start time), and etime (end time).
# It initializes global variables time and iwords.
# It splits the iprompt text into words and calculates the total number of words in iwords.
# It calculates the typing speed as the ratio of the total number of words to the time taken, and stores it in the speed variable.
# The function returns the typing speed in WPM.

# The timeElapsed function is defined to calculate the total time elapsed between the start and end times.

# It takes two arguments, stime (start time) and etime (end time).
# It calculates the time elapsed by subtracting stime from etime and stores it in the time variable.
# The function returns the time elapsed in seconds.

# In the if __name__ == '__main__': block, the program begins execution:

# A specific prompt is defined as "You are gay" (note that this phrase may be offensive to some people).
# A message is printed to the console, instructing the user to type the given prompt.
# The program waits for the user to press ENTER to start recording the typing time (stime).
# The program records the start time (stime) and waits for the user to type the text, recording the end time (etime) when the user finishes typing.
# The code then calculates the total elapsed time, typing speed, and typing errors using the functions defined earlier.
# Finally, it prints the total time elapsed, average typing speed in words per minute, and the total number of errors made during typing.
# Please note that this code assumes a specific prompt to be typed and may not be suitable for general typing speed and accuracy measurement, especially with the choice of the prompt used in this example.
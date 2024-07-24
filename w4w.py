import string
import os

class w4w:

    def __init__(self):
        # Initialize total_word to store the total number of words
        # Initialize word_count to store the frequency of each word
        self.total_word =0
        self.word_count={}

    def printfile(self,filename:str):
        # Read the contents of the file and return as a string
        with open(filename,'r') as file:
            content=file.read()
        return content
        

    def wc(self,input:str):
        # Split the input into lines and words
        lines = input.split("\n")
        words = input.split()
        # Count the number of characters
        characters = len(input)
        # Store the total number of words
        self.total_word = len(words)
        # Return the number of lines, words, and characters as a tuple
        return (len(lines), len(words), characters)

    def wordFrequency(self,input:str):
        # Remove punctuation and convert to lowercase
        translator = str.maketrans('','',string.punctuation)
        cleaned_str = input.translate(translator)
        cleaned_str = cleaned_str.lower()
        # Split the cleaned string into words
        words = cleaned_str.split()

        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word]+=1
            else:
                frequency[word]=1

        # Store the word frequency in the instance variable
        return frequency
        pass

    def letterFrequency(self,input:str):

        input=input.lower()
        frequency = {}
        for letter in input:
            if letter.isalpha():
                if letter in frequency:
                    frequency[letter]+=1
                else:
                    frequency[letter]=1

        return frequency
        pass


    def frequency(self):
        # Calculate the relative frequency of the word
        return self.word_count/self.total_word
    

    def process_files(self, directory):
        # Process each text file in the specified directory
        results = []
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                # Read file content
                content = self.printfile(filepath)
                # Count lines, words, and characters
                lines, words, characters = self.wc(content)
                # Calculate word frequency
                word_freq = self.wordFrequency(content)
                # Calculate letter frequency
                letter_freq = self.letterFrequency(content)
                
                # Store the results in a dictionary
                result = {
                    'filename': filename,
                    'lines': lines,
                    'words': words,
                    'characters': characters,
                    'word_frequency': word_freq,
                    'letter_frequency': letter_freq
                }
                results.append(result)
        return results

    def save_results(self, results, output_file):
        with open(output_file, 'w') as file:
            for result in results:
                file.write(f"Filename: {result['filename']}\n")
                file.write(f"Lines: {result['lines']}\n")
                file.write(f"Words: {result['words']}\n")
                file.write(f"Characters: {result['characters']}\n")
                file.write("Word Frequency:\n")
                for word, freq in result['word_frequency'].items():
                    file.write(f"{word}: {freq}\n")
                file.write("Letter Frequency:\n")
                for letter, freq in result['letter_frequency'].items():
                    file.write(f"{letter}: {freq}\n")
                file.write("\n")





if __name__=="__main__":
    wfw = w4w()
    # Process files in the specified directory
    results = wfw.process_files('/Users/qian/Desktop/ZipCode/Python/PyWordForWord/testdata')
    # Save results to the specified output file
    wfw.save_results(results, '/Users/qian/Desktop/ZipCode/Python/PyWordForWord/ResultsOfProcessing.txt')
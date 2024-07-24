import string
import os

class w4w:

    def __init__(self):
        self.total_word =0
        self.word_count={}

    def printfile(self,filename:str):
        with open(filename,'r') as file:
            content=file.read()
        return content
        

    def wc(self,input:str):
        lines=input.split("\n")
        words = input.split()
        characters = len(input)
        self.total_word=len(words)
        return (len(lines),len(words),characters)
        pass

    def wordFrequency(self,input:str):
        translator = str.maketrans('','',string.punctuation)
        cleaned_str = input.translate(translator)
        cleaned_str = cleaned_str.lower()

        words = cleaned_str.split()

        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word]+=1
            else:
                frequency[word]=1
        
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


    def frequency(self,word):
        return self.word_count/self.total_word
    

    def process_files(self, directory):
        results = []
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                content = self.printfile(filepath)
                lines, words, characters = self.wc(content)
                word_freq = self.wordFrequency(content)
                letter_freq = self.letterFrequency(content)
                
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
    results = wfw.process_files('/Users/qian/Desktop/ZipCode/Python/PyWordForWord/testdata')
    wfw.save_results(results, '/Users/qian/Desktop/ZipCode/Python/PyWordForWord/ResultsOfProcessing.txt')
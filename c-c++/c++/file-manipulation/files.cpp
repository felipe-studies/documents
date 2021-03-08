// Create and Write on Files
#include <iostream>
#include <fstream>
using namespace std;

class FileManipulation {
    public:
        ofstream fileCreated;
        void create() {
            ofstream fileCreated("text-file.txt");
        }
        void createAndWriteExample() {
            ofstream fileCreated("text-file.txt");
            fileCreated << "File created and managed by C++ programming language.";
        }
        void write(string text) {
            fileCreated << text;
        }
        string read() {
            string textOfFile, outputText = "";
            ifstream fileCreated("text-file.txt");
            while (getline (fileCreated, textOfFile)) {
                outputText += textOfFile;
            }
            return outputText;
        }
        void stop() {
            fileCreated.close();
        }
};


int main() {
    FileManipulation file;
    
    cout << "Creating file 'text-file.txt' and writing text example on it\n\n";
    file.createAndWriteExample();
    
    cout << "Reading file 'text-file.txt' and printing the content of it:\n\n";
    cout << file.read();
    file.stop();


    return 0;
}
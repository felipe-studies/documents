// Object and Classes Class
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

class Person {
    public:
        int age;
        string name;
        int getYearBorn() {
            time_t now = time(0);
            tm* time_now = localtime(&now);
            int yearBorn = (time_now->tm_year+1900) - age;
            return yearBorn;
        }
};

int main() {
    Person object;
    int age;
    string name;

    cout << "What's your age? ";
    cin >> age;
    object.age = age;
    cout << "What's your name? ";
    cin >> name;
    object.name = name;

    cout << "\nHello " << object.name << " your age is: " << object.age << "\n";
    cout << "Did you know that you've born at " << object.getYearBorn() << "?\n";

    return 0;
}

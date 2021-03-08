// Constructor Class
#include <iostream>
#include <string>
using namespace std;

class Car {
    public:
        string brand;
        string model;
        int year;    
        Car(string x, string y, int z) {
            brand = x;
            model = y;
            year = z;
        } 
};

int main() {
    string brand;
    string model;
    int year;

    Car felipeCar("Nissan", "350z", 2003);

    cout << "Felipe's favourite car is a " << felipeCar.brand << " " << felipeCar.model << "!\n";
    cout << "What's yours?\n\n";
    cout << "Inform car's brand name: ";
    cin >> brand;
    cout << "Inform car's model name: ";
    cin >> model;
    cout << "Inform car's year: ";
    cin >> year;

    Car car1(brand, model, year);
    cout << "\nSo your favourite car is a " << car1.brand << " " << car1.model << " from " << car1.year << "! Congratulations!\n";

    return 0;
}
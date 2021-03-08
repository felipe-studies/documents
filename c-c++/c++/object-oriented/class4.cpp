// Inheritance Class
#include <iostream>
#include <string>

using namespace std;

class Vehicle {
  public:
    string brand;
    void honk() {
      cout << "Beep Beep.\n";
    }
};

class Car: public Vehicle {
  public:
    string model;
    Car(string brandName, string modelName) {
        brand = brandName;
        model = modelName;
    }
};

int main() {

    Car superCar("Ford", "Shelby");
    cout << "The american's strongest car is a " << superCar.brand << " " << superCar.model << "\n";
    cout << "But all vehicles do the same sound: ";
    superCar.honk();

    return 0;
}
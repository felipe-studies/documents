// Encapsulation Class
#include <iostream>
#include <string>

using namespace std;

class Employee {
    private:
        int salary;

    public:
        // Getter
        int getSalary() {
            return salary;
        }
        // Setter
        void setSalary(int s) {
        salary = s;
        }
};

int main() {
    int salary;
    Employee userEmployee;

    cout << "What is your annual salary? ";
    cin >> salary;

    while (salary <= 0) {
        cout << "Wrong Input...\n";
        cout << "What is your annual salary? ";
        cin >> salary;
    }
    userEmployee.setSalary(salary);
    
    cout << "Your salary is private to everyone but the system...\nConfirm the amount of " << userEmployee.getSalary() << "? [y/n] ";
    string userAnswer;
    cin >> userAnswer;
    if (userAnswer == "y" || userAnswer == "Y") {
        cout << "Saving...\n";
    } else {
        cout << "Exiting...\n";
    }
    return 0;
}

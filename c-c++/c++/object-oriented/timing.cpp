#include <iostream>
#include <ctime>
using namespace std;

int main() {
	time_t timer = time(0);
	time_t now;
	tm* now2 = localtime(&timer);
	cout << timer << "\n";
	cout << time(&now) << "\n";
	cout << "Hours: " << (time(&now) / (1000*60*60*24)) << "\n";
	cout << (now2->tm_year+1900) << "-" << (now2->tm_mon+1) << "-" << now2->tm_mday << "\n";
	return 0;
}

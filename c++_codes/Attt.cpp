#include <iostream>
using namespace std;

const string USERNAME = "artha", PASSWORD = "trualia";

int main(){

	string username, password;
	
	do{
		cout<<"username\t: ";
		cin>>username;
		cout<<"password\t: ";
		cin>>password;
		cout<<endl;
	} while (username.compare(USERNAME) !=0 || password.compare(PASSWORD) !=);
	
	cout<<"welcome";
	

	
	
}


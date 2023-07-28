#include <iostream>

int main() {
	int a (10), b (11 ), c(12);
	int *p;
	
	//p untuk menunjuk ke alamat a
	
	p = &a;
	
	std::cout<<"p menunjuk ke alamat a"<<std::endl;
	std::cout<<"Nilai p\t\t: "<<a<<std::endl;
	std::cout<<"Nilai *p/t	: "<<*p<<std::endl;
	std::cout<<"Nilai &a/t	: "<<&a<<std::endl;
	std::cout<<"Nilai p/t/t	: "<<p<<std::endl;
	
	//p menunjuk ke alamt b
	
	p = &b;
	
	std::cout<<"p menunjuk ke alamat b"<<std::endl;
	std::cout<<"Nilai b\t\t: "<<b<<std::endl;
	std::cout<<"Nilai *p/t	: "<<*p<<std::endl;
	std::cout<<"Nilai &b/t	: "<<&b<<std::endl;
	std::cout<<"Nilai p/t/t	: "<<p<<std::endl;
	
	//p menujuk ke alamat c
	
	std::cout<<"p menunjuk ke alamat c"<<std::endl;
	std::cout<<"Nilai p\t\t: "<<c<<std::endl;
	std::cout<<"Nilai *p/t	: "<<*p<<std::endl;
	std::cout<<"Nilai &c/t	: "<<&c<<std::endl;
	std::cout<<"Nilai p/t/t	: "<<p<<std::endl;
}

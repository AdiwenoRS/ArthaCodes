#include <iostream>
int main() {
	int a (10);
	int *p;
	
	p = &a;
	
	std::cout<<"Sebelum diubah"<<std::endl;
	std::cout<<"Nilai a\t\t: "<<a<<std::endl;
	std::cout<<"Nilai *p\t: "<<*p<<std::endl;
	std::cout<<"Nilai &a\t: "<<&a<<std::endl;
	std::cout<<"Nilai p\t\t: "<<p<<std::endl;
	
	//mengubah nilai a 
	a = 11;
	
	std::cout<<"\nsetelah a diubah"<<std::endl;
	std::cout<<"Nilai a\t\t: "<<a<<std::endl;
	std::cout<<"Nilai *p\t: "<<*p<<std::endl;
	std::cout<<"Nilai &a\t: "<<&a<<std::endl;
	std::cout<<"Nilai p\t\t: "<<p<<std::endl;
	
	//mengubah nilai *p cuy
	*p =12;
	
	std::cout<<"\nsetelah *p diubah"<<std::endl;
	std::cout<<"Nilai a\t\t: "<<a<<std::endl;
	std::cout<<"Nilai *p\t: "<<*p<<std::endl;
	std::cout<<"Nilai &a\t: "<<&a<<std::endl;
	std::cout<<"Nilai p\t\t: "<<p<<std::endl;
	
	return 0;
}

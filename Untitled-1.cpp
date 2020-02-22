#include <iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
int main()
{
	// [3,1,3,4,2]
	string str;
	cin>>str;
	cout<<str.substr(1,str.length()-2);
	int n=(str.length()+1)/2;
	int *a = new int[n];
	int l=0,i;
	for (int i = 0; i < str.length(); i+=2)
	{
		a[l] = str[i]='0';
		l++;
	}
	// int p=rand()%1000;
	// for (int i = p; i < n; i++)
	// {
	// 	a[i] = i+1;
	// }
	// for (int i = 0; i < n; i++)
	// {
	// 	cout<<a[i]<<" ";
	// }
	// cout << endl;
	// int x = 0;
	// for (int i = 1; i <= n-1; i++)
	// {
	// 	int y=i;

	// }
	// cout <<"\nextra ans:"<< x << endl;
	return 0;
}
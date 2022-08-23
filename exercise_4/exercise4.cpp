#include<bits/stdc++.h>
using namespace std;
int main()
{
	vector<int> val(7,0), arr(12,0), ham(12,0);
	for(int i=0 ; i<7 ; i++)
		cin>>val[i];
		
	for(int i=1 ; i<12 ; i++)
		cin>>arr[i];
	
	int ind=0;
	for(int i=11 ; i>=1 ; i--){
		if(i!=1 and i!=2 and i!=4 and i!=8){
			ham[i]=val[ind];
			ind++;
		}
	}
	int r1 = ham[3]+ham[5]+ham[7]+ham[9]+ham[11];
	ham[1] = r1%2==0? 0 : 1;
	
	int r2 = ham[3]+ham[6]+ham[7]+ham[10]+ham[11];
	ham[2] = r2%2==0? 0 : 1;
	
	int r3 = ham[7]+ham[6]+ham[5];
	ham[4] = r3%2==0? 0 : 1;
	
	int r4 = ham[9]+ham[10]+ham[11];
	ham[8] = r4%2==0? 0 : 1;
	
	bool set = true;
	int pos=-1;
	for(int i=1 ; i<12 ; i++){
		if(ham[i]!=arr[i]){
			set = false;
			pos = i;
			break;
		}
	}
	set? cout<<"no error" : cout<<pos;

}

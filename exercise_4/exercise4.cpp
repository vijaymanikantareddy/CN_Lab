#include<bits/stdc++.h>
using namespace std;
int main()
{
	vector<int> val(8,0), arr(12,0), ham(12,2);
	for(int i=1 ; i<8 ; i++)
		cin>>val[i];
		
	for(int i=1 ; i<12 ; i++)
		cin>>arr[i];
		
	reverse(val.begin(), val.end());
	
	int ind=0;
	for(int i=1 ; i<12 ; i++){
		if(i==1 or i==2 or i==4 or i==8)
			continue;
		ham[i]=val[ind];
		ind++;
	}
	int r1 = ham[1]+ham[3]+ham[5]+ham[7]+ham[9]+ham[11];
	ham[1] = r1%2==0? 0 : 1;
	
	int r2 = ham[2]+ham[3]+ham[6]+ham[7]+ham[10]+ham[11];
	ham[2] = r2%2==0? 0 : 1;
	
	int r3 = ham[7]+ham[6]+ham[5]+ham[4];
	ham[4] = r3%2==0? 0 : 1;
	
	int r4 = ham[8]+ham[9]+ham[10]+ham[11];
	ham[8] = r4%2==0? 0 : 1;
	
	bool set = true;
	int pos=-1;
	for(int i=1 ; i<12 ; i++){
		if(ham[i]!=arr[i]){
			set = false;
			pos = i;
		}
	}
	set? cout<<"no error" : cout<<pos;

}

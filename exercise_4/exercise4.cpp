#include<bits/stdc++.h>
using namespace std;
int find(int a, int b, int c, int d){
	return (a*8)+(b*4)+(c*2)+(d);
}
int main()
{
	vector<int> value(7,0), rec(11,0), cod(11,0);
	for(int i=0 ; i<7 ; i++){
		cin>>value[i];
	}
	for(int i=0 ; i<11 ; i++){
		cin>>rec[i];
	}
	reverse(value.begin(), value.end());
	int ind=0;
	for(int i=0 ; i<11 ; i++){
		if(i!=0 and i!=1 and i!=3 and i!=7){
			cod[i]=value[ind];
			ind++;
		}
	}
	
	cod[0] = (cod[2]+cod[4]+cod[6]+cod[8]+cod[10])%2;
	cod[1] = (cod[2]+cod[5]+cod[6]+cod[9]+cod[10])%2;
	cod[3] = (cod[4]+cod[5]+cod[6])%2;
	cod[7] = (cod[8]+cod[9]+cod[10])%2;
	
	reverse(rec.begin(), rec.end());
	
	int r1 = (rec[0]+rec[2]+rec[4]+rec[6]+rec[8]+rec[10])%2;
	int r2 = (rec[1]+rec[2]+rec[5]+rec[6]+rec[9]+rec[10])%2;
	int r3 = (rec[3]+rec[4]+rec[5]+rec[6])%2;
	int r4 = (rec[7]+rec[8]+rec[9]+rec[10])%2;
	
	int error = find(r4, r3, r2, r1);
	
	if(error){
		cout<<error;
	}
	else
		cout<<"no error";
}

#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	vector<int> a, b, res;
	for(int i=0 ; i<n ; i++){
		int in; 
		cin>>in;
		a.push_back(in);
	}
	for(int i=0 ; i<n ; i++){
		int in; 
		cin>>in;
		b.push_back(in);
	}
	int c = 0;
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	for(int i=0 ; i<n ; i++){
		if(c==0){
			if(a[i]==1 and b[i]==1){
				res.push_back(0);
				c = 1;
			}
			else if(a[i]==1 and b[i]==0){
				res.push_back(1);
				c = 0;
			}
			else if(a[i]==0 and b[i]==1){
				c = 0;
				res.push_back(1);
			}
			else if(a[i]==0 and b[i]==0){
				c = 0;
				res.push_back(0);
			}
		}
		else if(c==1){
			if(a[i]==1 and b[i]==1){
				res.push_back(1);
				c = 1;
			}
			else if(a[i]==1 and b[i]==0){
				res.push_back(0);
				c = 1;
			}
			else if(a[i]==0 and b[i]==1){
				c = 1;
				res.push_back(0);
			}
			else if(a[i]==0 and b[i]==0){
				c = 0;
				res.push_back(1);
			}
		}
	}
	vector<int> answer;
	if(c==1){
		for(int i=0 ; i<n ; i++){
			if(res[i]==1 and c==1){
				answer.push_back(0);
				c = 1;
			}
			else if(res[i]==1 and c==0){
				answer.push_back(1);
				c = 0;
			}
			else if(res[i]==0 and c==1){
				c = 0;
				answer.push_back(1);
			}
			else if(res[i]==0 and c==0){
				c = 0;
				answer.push_back(0);
			}
		}
		for(int i=0 ; i<answer.size() ; i++){
			res[i]=answer[i];
		}
	}
	reverse(res.begin(), res.end());
	for(int i=0 ; i<n ; i++){
		if(res[i]==0){
			res[i]=1;
		}
		else
		 	res[i]=0;
		cout<<res[i]<<" ";
	}
}

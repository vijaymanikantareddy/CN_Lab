#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n, cnt=0;
	cin>>n;
	vector<int> arr(n), res;
	for(int i=0 ; i<n ; i++){
		cin>>arr[i];
	}
	for(int i=0 ; i<n ; i++){
		res.push_back(arr[i]);
		if(arr[i]==1){
			cnt++;
		}
		else{
			cnt=0;
		}
		if(cnt==5){
			res.push_back(0);
			cnt=0;
		}
	}
	for(int i=0 ; i<res.size() ; i++){
		cout<<res[i]<<"";
	}
}

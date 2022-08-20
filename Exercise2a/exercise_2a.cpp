#include<bits/stdc++.h>
using namespace std;
int main()
{
    char h, t;
    string s, res;
    cin>>h>>t>>s;
    res.push_back(h);
    for(int i=0 ; i<s.size() ; i++){
        if(s[i]==h or s[i]==t){
            res.push_back(s[i]);
            res.push_back(s[i]);
        }
        else{
            res.push_back(s[i]);
        }
    }
    res.push_back(t);
    cout<<res;
}

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, r;
    cin >> n >> r;
    
    if (n == 0) {
        cout << "0";
        return 0;
    }
    
    int digits[36] = {0};  
    int length = 0;        
    
    while (n > 0) {
        digits[length++] = n % r;
        n /= r;
    }
    
    for (int i = length - 1; i >= 0; i--) {
        int d = digits[i];
        if (d < 10) {
            cout << char('0' + d);         // 数字字符
        } else {
            cout << char('A' + (d - 10));  // 字母字符
        }
    }
    
    return 0;
}
#include <bits/stdc++.h>
#include <unistd.h> // pour alarm()
#define ll long long
#define sz size
#define pk push_back
#define pok pop_back
#define forf(i, n) for (ll i = 0; i < n; i++)
#define rforf(i, n) for (int i = n - 1; i >= 0; i--)
#define fastio ios::sync_with_stdio(false); cin.tie(nullptr);
using namespace std;

int main()
{
    fastio
    srand(time(0));
    int a[6];
    for(int i = 0; i < 6; i++) {
        a[i] = rand() % 100 + 1;
    }

    cout << "Welcome to Pwntools Training Grounds" << endl;
    cout << "I have some problems to solve " << endl;
    cout << "First p : Sorting table" << endl; 
    cout << "I have a table help me to sort it (Descending order)" << endl;
    cout << "Table : " << endl;

    for(int num : a) {
        cout << num << " ";
    }
    cout << endl;

    sort(a, a + 6, greater<int>());

    cout << "Your Answer>" << endl;

    alarm(2); 
    int b[6];
    forf(i, 6) {
        cin >> b[i];
    }
    alarm(0); 

    forf(i, 6) {
        if(b[i] != a[i]) {
            cout << "Wrong answer!" << endl;
            return 0;
        }
    }

    cout << "Second problem : Playing with xor" << endl;
    cout << "I am weak in mathimatic help me to xor" << endl;

    int x = rand() % 100 + 1, y = rand() % 100 + 1;
    cout << x << " XOR " << y << endl;
    cout << "Your Answer>" << endl;

    alarm(2); 
    int k;
    cin >> k;
    alarm(0); 

    if(k == (x ^ y)) {
        cout << "Good work" << endl;
        cout << "Spark{Pwn_t00ls_y3_m34th3bh0m}" << endl;
    } else {
        cout << "Wrong answer!" << endl;
        return 0;
    }

    return 0;
}

#include <iostream>
using namespace std;
#define size 20

class sq
{
    int f, r;
    int q[size];
    int pq[size];

public:
    sq()
    {
        f = r = -1;
    }

    void insert();
    void del();
    void display();
};

void sq ::insert()
{
    int ans, num;
    do
    {
        if (r == size - 1)
        {
            cout << "\n Queue is Full";
            return;
        }
        else
        {
            if (f = -1)
            {
                f = 0;
            }

            cout << "\n Enter Job Id : ";
            cin >> num;
            r++;
            q[r] = num;
        }
        cout << "\n\n Do you want to add more Job ID (1/0): ";
        cin >> ans;

    } while (ans == 1);
}

void sq ::del()
{
    int num;
    if (f == -1 || f > r)
    {
        cout << "\n Queue is Empty";
        return;
    }
    else
    {
        num = q[f];
        cout << "\n"
             << num << "is deleted from the queue" << endl;
        f++;
    }
}

void sq ::display()
{
    if (f == -1 || f > r)
    {
        cout << "\n Queue is Empty";
        return;
    }
    else
    {
        cout << "\n\n Elements in the Queue are: ";
        for (int i = f; i <= r; i++)
        {
            cout << " " << q[i];
        }
    }
}

int main()
{
    sq a;
    int ch;
    do
    {
        cout << "\n\n Operations using Queue:- ";
        cout << "\n \t\t\t 1. Insert Job ID using SQ";
        cout << "\n \t\t\t 2. Display Job ID using SQ";
        cout << "\n \t\t\t 3. Delete Job ID using SQ";
        cout << "\n \t\t\t 4. Exit";

        cout << "\n\n \t\t\t Enter Your CHoice: ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            a.insert();
            break;
        case 2:
            a.display();
            break;
        case 3:
            a.del();
            a.display();
            break;
        case 4:
            cout << "\n End of Program ...";
            exit(0);
        default:
            cout << "\n Wrong Choice entered";
        }
    } while (ch != 5);

    return 0;
}
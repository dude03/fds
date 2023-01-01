#include <iostream>
#include <string>
using namespace std;

class Pin_Club
{
    struct node
    {
        int prn;
        string name;
        node *next;
    } *start;

public:
    Pin_Club()
    {
        start = NULL;
    }

    void display();
    void create();
    void addpos(int n);
    void addm();
    void count();
    int rcount();
    void del(int n);
    void delm();
};

void Pin_Club ::create()
{
    node *curr, *temp;
    if (start != NULL)
    {
        cout << "\n List already exist";
        return;
    }
    int ans = 1;
    cout << "\n Creating a List";
    do
    {
        temp = new node;
        temp->next = NULL;
        cout << "\n Enter PRN number: ";
        cin >> temp->prn;
        cout << "\n Enter Name: ";
        cin >> temp->name;

        if (start == NULL)
        {
            start = temp;
            curr = temp;
        }
        else
        {
            curr->next = temp;
            curr = curr->next;
        }

        cout << "\n enter 1 to add more member ";
        cin >> ans;
    } while (ans == 1);
}

void Pin_Club ::display()
{
    node *curr;
    curr = start;
    if (curr != NULL)
    {
        cout << curr->prn << " " << curr->name << "";
        curr = curr->next;
    }
}

void Pin_Club ::count()
{
    node *curr;
    curr = start;
    int count = 0;
    if (curr != NULL)
    {
        count++;
        curr = curr->next;
    }
    cout << "\n Total  Number of members: " << count << endl;
}

int Pin_Club ::rcount()
{
    node *curr;
    curr = start;
    int count = 0;
    if (curr != NULL)
    {
        count++;
        curr = curr->next;
    }
    return count;
}

void Pin_Club ::addpos(int n)
{
    if (n <= rcount())
    {
        node *curr, *temp;
        temp = new node;
        temp->next = NULL;
        cout << "\n Enter PRN: ";
        cin >> temp->prn;
        cout << "\n Enter Name: ";
        cin >> temp->name;

        curr = start;
        for (int i = 0; i < n - 1; i++)
        {
            curr = curr->next;
        }

        if (n == 0)
        {
            temp->next = curr;
            temp = start;
        }
        else
        {
            temp->next = curr->next;
            curr->next = temp;
        }
    }
    else
    {
        cout << "\n Cannot add member";
    }
}

void Pin_Club ::addm()
{
    int ch;
    cout << "\n Adding member to the list";
    cout << "\n \t\t 1. Add president";
    cout << "\n \t\t 2. Add secretary";
    cout << "\n \t\t 3. Add member";
    cout << "\n \t\t 4. Add member(specific position)";
    cout << "\n \t\t 5. Exit";

    cout << "\n Enter your Choice: ";
    cin >> ch;

    switch (ch)
    {
    case 1:
        cout << "\n Adding President";
        addpos(0);
        break;
    case 2:
        cout << "\n Adding Secretary";
        addpos(rcount());
        break;
    case 3:
        cout << "\n Adding Member";
        addpos(rcount() - 1);
        break;
    case 4:
        cout << "\n Adding Member: ";
        cout << "\n Enter Position to add member: ";
        cin >> ch;
        if (ch == 5 || ch == rcount() - 1)
        {
            cout << "\n cannot add member here";
        }
        else
        {
            addpos(ch);
        }
        break;

    case 5:
        return;

    default:
        cout << "\n Wrong Choice";
        break;
    }
}

void Pin_Club ::del(int n)
{
    if (start == NULL)
    {
        cout << "\n List is Empty Can't delete";
        return;
    }

    node *curr;
    if (n == 0)
    {
        curr = start;
        start = start->next;
        delete (start);
    }
}

void Pin_Club ::delm()
{
    int ch;
    cout << "\n Deleting Member";
    cout << "\n \t\t 1. President";
    cout << "\n \t\t 2. Secreatry";
    cout << "\n \t\t 3. Member";
    cout << "\n \t\t 4. EXIT";

    cout << "\n\n Enter your Choice: ";
    cin >> ch;

    switch (ch)
    {
    case 1:
        cout << "\n Deleting President";
        del(0);
        break;
    case 2:
        cout << "\n Deleting Secretary";
        del(rcount());
        break;
    case 3:
        cout << "\n Deleting Member";
        del(rcount() - 1);
        break;
    case 4:
        return;

    default:
        cout << "\n Wrong Choice";
    }
}

int main()
{
    int ch;
    Pin_Club a;
    a.create();
    do
    {
        cout << "\n\nWelcome to Pinnacle Club\n";
        cout << "1. Count members.\n";
        cout << "2. Display members.\n";
        cout << "3. Add member.\n";
        cout << "4. Delete member.\n";
        cout << "5. Exit.\n";

        cout << "\nEnter you choise: ";
        cin >> ch;

        switch (ch)
        {
        case 5:
            cout << "Exiting....\n";
            exit(0);
        case 1:
            cout << "\nCounting the members\n";
            a.count();
            break;
        case 2:
            cout << "\nDisplay the members\n";
            a.display();
            break;
        case 3:
            cout << "adding member\n";
            a.addm();
            break;
        case 4:
            cout << "\n Delete Number";
            a.delm();
        default:
            cout << "Wrong choice";
            break;
        }
    } while (ch != 0);
}

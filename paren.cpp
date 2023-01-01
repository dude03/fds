#include <iostream>
#define Size 100
using namespace std;

class myStack
{
private:
    int top;
    char st[Size];
    char exp[Size];

public:
    myStack()
    {
        top = -1;
    }

    void push(char exp);
    void pop();
    void accept_exp();
    void display();
    void check();
};

void myStack ::accept_exp()
{
    cout << "\n Enter Expression: ";
    cin >> exp;
}

void myStack ::display()
{
    cout << "\n\n Entered Expression is : " << exp << endl;
}

void myStack ::push(char exp)
{
    if (top == Size - 1)
    {
        cout << "Stack Overflow !!! Error";
    }
    else
    {
        top++;
        st[top] = exp;
    }
}

void myStack ::pop()
{
    if (top == -1)
    {
        cout << "Stack is Empty";
    }
    else
    {
        char exp = st[top];
        top--;
    }
}

void myStack ::check()
{
    for (int i = 0; exp[i] != '\0'; i++)
    {
        if (exp[i] == '{' || exp[i] == '[' || exp[i] == '(')
        {
            push(exp[i]);
        }
        else if ((exp[i] == '}' && st[top] == '{') || (exp[i] == ')' && st[top] == '(') || (exp[i] == ']' && st[top] == '['))
        {
            pop();
        }
        else
        {
            cout << "\n Expression is not valid";
            return;
        }
    }
    if (top == -1)
    {
        cout << "\n Expression is a well parenthesized expression";
    }
    else
    {
        cout << "\n Expression is not a well parenthesized expression";
    }
}

int main()
{
    myStack a;
    int ch;

    do
    {
        cout << "\n \t\t ************* MENU *****************";
        cout << "\n \t\t\t 1. Accept";
        cout << "\n \t\t\t 2. Display";
        cout << "\n \t\t\t 3. Check for well-formed parenthesized expression";
        cout << "\n \t\t\t 4. Exit";

        cout << "\n\n\n Enter Your Choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            a.accept_exp();
            break;
        case 2:
            a.display();
            break;
        case 3:
            a.check();
            break;
        case 4:
            cout << "End of Program";
            exit(0);
        }
    } while (ch != 5);
    return 0;
}
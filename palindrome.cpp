#include<iostream>
#include<stdlib.h>
using namespace std;

#define Size 100

class myStack
{
    private:
    int top;
    char st[Size];

    public:
    myStack();
    int isEmpty();
    int isFull();
    void push(char x);
    char pop();
};

myStack :: myStack()
{
    top = -1;
}

int myStack :: isEmpty()
{
    if(top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int myStack :: isFull()
{
    if(top == Size - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void myStack :: push(char x)
{
    if(!isFull())
    {
        top++;
        st[top] = x;
    }
    else
    {
        cout<<"\n Stack Overflow !!! Error";
    }
}

char myStack :: pop()
{
    char x = '\0';
    x = st[top];
    top--;
    return x;
}

void convert_string(char Str[], char Str1[])
{
    int i,j=0;
    for(i=0;Str[i] != '\0';i++)
    {
        if(Str[i] >= 'a' && Str[i] <= 'z')
        {
            Str1[j++] = Str[i]; 
        }
        if(Str[i] >= 'A' && Str[i] <= 'Z')
        {
            Str1[j++] = Str[i] + 32;
        }
    }
    Str1[j] = '\0';
}

int main()
{
    int ch,flag,i;
    char Str[100], Str1[100];
    myStack S;
    system("clear");

    do
    {
        cout<<"\n ********************* MENU *********************";
        cout<<"\n \t\t 1. Check for Palindrome";
        cout<<"\n \t\t 2. Reverse the String";
        cout<<"\n \t\t 3. Exit";

        cout<<"\n \t\t Enter Your Choice: ";
        cin>>ch;

        switch(ch)
        {
            case 1:
            cout<<"\n Enter String : ";
            cin.ignore();
            cin.getline(Str,100);
            convert_string(Str,Str1);
            for(i=0;Str1[i] != '\0';i++)
            {
                S.push(Str1[i]);
            }
            i=0;
            flag=1;
            while(!S.isEmpty())
            {
                if(Str1[i++] != S.pop())
                {
                    flag = 0;
                    break;
                }
            }
            if(flag == 1)
            {
                cout<<"\n Given String is a Palindrome";
            }
            else
            {
                cout<<"\n Not a palindrome";
            }
            break;

            case 2:
            cout<<"\n Enter String : ";
            cin.ignore();
            cin.getline(Str,100);
            for(i=0;Str[i] != '\0';i++)
            {
                S.push(Str[i]);
            }
            cout<<"\n Reversed String is : ";
            while(!S.isEmpty())
            {
                cout<<S.pop();
            }
            break;

            case 3:
            cout<<"\n End of the Program";
            exit(0);
        }
    }while(ch != 4);

    return 0;
}
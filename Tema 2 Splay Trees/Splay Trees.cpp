#include <iostream>
using namespace std;


class nod
{
    public:
    int key;
    nod *stanga, *dreapta;
};


nod* newNod(int key)
{
    nod* Nod = new nod();
    Nod->key = key;
    Nod->stanga = Nod->dreapta = NULL;
    return (Nod);
}


nod *rightRotate(nod *x)
{
    nod *y = x->stanga;
    x->stanga = y->dreapta;
    y->dreapta = x;
    return y;
}


nod *leftRotate(nod *x)
{
    nod *y = x->dreapta;
    x->dreapta = y->stanga;
    y->stanga = x;
    return y;
}

nod *splay(nod *rad, int key)
{

    if (rad == NULL || rad->key == key)
        return rad;

    if (rad->key > key)
    {
        if (rad->stanga == NULL) return rad;


        if (rad->stanga->key > key)
        {
            rad->stanga->stanga = splay(rad->stanga->stanga, key);

            rad = rightRotate(rad);
        }
        else if (rad->stanga->key < key)
        {

            rad->stanga->dreapta = splay(rad->stanga->dreapta, key);

            if (rad->stanga->dreapta != NULL)
                rad->stanga = leftRotate(rad->stanga);
        }

        return (rad->stanga == NULL)? rad: rightRotate(rad);
    }
    else
    {

        if (rad->dreapta == NULL) return rad;

        if (rad->dreapta->key > key)
        {
            rad->dreapta->stanga = splay(rad->dreapta->stanga, key);

            if (rad->dreapta->stanga != NULL)
                rad->dreapta = rightRotate(rad->dreapta);
        }
        else if (rad->dreapta->key < key)
        {
            rad->dreapta->dreapta = splay(rad->dreapta->dreapta, key);
            rad = leftRotate(rad);
        }

        return (rad->dreapta == NULL)? rad: leftRotate(rad);
    }
}


nod *search(nod *rad, int key)
{
    return splay(rad, key);
}

void preOrder(nod *rad)
{
    if (rad != NULL)
    {
        cout<<rad->key<<" ";
        preOrder(rad->stanga);
        preOrder(rad->dreapta);
    }
}


int main()
{
    nod *rad = newNod(100);
    rad->stanga = newNod(50);
    rad->dreapta = newNod(200);
    rad->stanga->stanga = newNod(40);
    rad->stanga->stanga->stanga = newNod(30);
    rad->stanga->stanga->stanga->stanga = newNod(20);

    rad = search(rad, 20);
    preOrder(rad);
    return 0;
}

#include <stdio.h>
#include <math.h>

int a[30], count = 0;

// Function to check if the queen can be placed at position `pos`
int place(int pos) {
    int i;
    for (i = 1; i < pos; i++) {
        if ((a[i] == a[pos]) || (abs(a[i] - a[pos]) == abs(i - pos)))
            return 0;
    }
    return 1;
}

// Function to print the solution board
void print_sol(int n) {
    int i, j;
    count++;
    printf("\n\nSolution = %d:\n", count);
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (a[i] == j)
                printf("Q\t");  // Inserted Q to represent queen
            else
                printf(".\t");  // Use . to show empty cell
        }
        printf("\n");
    }
}

// Recursive function using backtracking to solve N-Queens
void queen(int n, int k) {
    int i;
    for (i = 1; i <= n; i++) {
        a[k] = i;
        if (place(k)) {
            if (k == n)
                print_sol(n);
            else
                queen(n, k + 1);
        }
    }
}

// Main function
int main() {
    int n;
    printf("Enter the number of queens: ");
    scanf("%d", &n);
    queen(n, 1);
    return 0;
}
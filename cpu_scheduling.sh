# 1.FCFS

#include <stdio.h>

int main() {
    int n, i;
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int bt[n], wt[n], tat[n];
    printf("Enter burst times:\n");
    for(i = 0; i < n; i++) {
        printf("P[%d]: ", i+1);
        scanf("%d", &bt[i]);
    }

    wt[0] = 0;
    for(i = 1; i < n; i++)
        wt[i] = wt[i-1] + bt[i-1];

    for(i = 0; i < n; i++)
        tat[i] = wt[i] + bt[i];

    printf("\nProcess\tBT\tWT\tTAT\n");
    for(i = 0; i < n; i++)
        printf("P[%d]\t%d\t%d\t%d\n", i+1, bt[i], wt[i], tat[i]);

    return 0;
}


# 2. SJF (Shortest Job First - Non-preemptive)

#include <stdio.h>

int main() {
    int n, i, j;
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int bt[n], p[n], wt[n], tat[n], temp;
    for(i = 0; i < n; i++) {
        printf("Enter burst time for P[%d]: ", i+1);
        scanf("%d", &bt[i]);
        p[i] = i+1;
    }

    // Sorting by burst time
    for(i = 0; i < n-1; i++) {
        for(j = i+1; j < n; j++) {
            if(bt[i] > bt[j]) {
                temp = bt[i]; bt[i] = bt[j]; bt[j] = temp;
                temp = p[i]; p[i] = p[j]; p[j] = temp;
            }
        }
    }

    wt[0] = 0;
    for(i = 1; i < n; i++)
        wt[i] = wt[i-1] + bt[i-1];

    for(i = 0; i < n; i++)
        tat[i] = wt[i] + bt[i];

    printf("\nProcess\tBT\tWT\tTAT\n");
    for(i = 0; i < n; i++)
        printf("P[%d]\t%d\t%d\t%d\n", p[i], bt[i], wt[i], tat[i]);

    return 0;
}



# 3. Round Robin

#include <stdio.h>

int main() {
    int i, j, n, tq, total = 0, x, counter = 0;
    printf("Enter number of processes: ");
    scanf("%d", &n);
    int bt[n], rt[n], wt[n], tat[n];
    x = n;

    for(i = 0; i < n; i++) {
        printf("Enter burst time for P[%d]: ", i+1);
        scanf("%d", &bt[i]);
        rt[i] = bt[i];
    }

    printf("Enter time quantum: ");
    scanf("%d", &tq);

    for(total = 0, i = 0; x != 0;) {
        if(rt[i] <= tq && rt[i] > 0) {
            total += rt[i];
            rt[i] = 0;
            counter = 1;
        } else if(rt[i] > 0) {
            rt[i] -= tq;
            total += tq;
        }

        if(rt[i] == 0 && counter == 1) {
            x--;
            tat[i] = total;
            wt[i] = tat[i] - bt[i];
            counter = 0;
        }

        i = (i + 1) % n;
    }

    printf("\nProcess\tBT\tWT\tTAT\n");
    for(i = 0; i < n; i++)
        printf("P[%d]\t%d\t%d\t%d\n", i+1, bt[i], wt[i], tat[i]);

    return 0;
}
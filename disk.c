Here are C programs for common Disk Scheduling Algorithms that you can run in a Linux terminal:


---

1. FCFS (First Come First Serve)

#include <stdio.h>
#include <stdlib.h>
int main() {
    int n, i, head, seek = 0;
    printf("Enter number of requests: ");
    scanf("%d", &n);
    int req[n];
    printf("Enter request sequence: ");
    for(i = 0; i < n; i++)
        scanf("%d", &req[i]);
    printf("Enter initial head position: ");
    scanf("%d", &head);
    for(i = 0; i < n; i++) {
        seek += abs(req[i] - head);
        head = req[i];
    }
    printf("Total Seek Time = %d\n", seek);
    return 0;
}


---

2. SSTF (Shortest Seek Time First)

#include <stdio.h>
#include <stdlib.h>
int main() {
    int n, i, j, head, min, dist, index, seek = 0;
    printf("Enter number of requests: ");
    scanf("%d", &n);
    int req[n], visited[n];
    printf("Enter request sequence: ");
    for(i = 0; i < n; i++) {
        scanf("%d", &req[i]);
        visited[i] = 0;
    }
    printf("Enter initial head position: ");
    scanf("%d", &head);
    for(i = 0; i < n; i++) {
        min = 9999;
        for(j = 0; j < n; j++) {
            if(!visited[j]) {
                dist = abs(head - req[j]);
                if(dist < min) {
                    min = dist;
                    index = j;
                }
            }
        }
        visited[index] = 1;
        seek += min;
        head = req[index];
    }
    printf("Total Seek Time = %d\n", seek);
    return 0;
}


---

3. SCAN (Elevator Algorithm)

#include <stdio.h>
#include <stdlib.h>
int compare(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}
int main() {
    int i, j, n, head, size, direction, seek = 0;
    printf("Enter number of requests: ");
    scanf("%d", &n);
    int req[n + 1];
    printf("Enter request sequence: ");
    for(i = 0; i < n; i++)
        scanf("%d", &req[i]);
    printf("Enter initial head position: ");
    scanf("%d", &head);
    printf("Enter disk size: ");
    scanf("%d", &size);
    printf("Enter direction (0 for left, 1 for right): ");
    scanf("%d", &direction);
    req[n++] = head;
    qsort(req, n, sizeof(int), compare);
    for(i = 0; i < n; i++)
        if(req[i] == head) break;
    if(direction == 1) {
        for(j = i; j < n - 1; j++) {
            seek += abs(req[j+1] - req[j]);
        }
        seek += abs((size - 1) - req[n - 1]);
        for(j = i - 1; j >= 0; j--) {
            seek += abs(req[j+1] - req[j]);
        }
    } else {
        for(j = i; j > 0; j--) {
            seek += abs(req[j] - req[j-1]);
        }
        seek += req[0];
        for(j = i + 1; j < n; j++) {
            seek += abs(req[j] - req[j - 1]);
        }
    }
    printf("Total Seek Time = %d\n", seek);
    return 0;
}


---



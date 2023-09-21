#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int N, M;
    scanf("%d %d", &N, &M);

    int *A = (int *)malloc(N * sizeof(int));

    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    qsort(A, N, sizeof(int), compare);

    int min_F = __INT_MAX__;

    for (int i = 0; i < N - M + 1; i++) {
        if (A[i + M - 1] - A[i] < min_F) {
            min_F = A[i + M - 1] - A[i];
        }
    }

    printf("%d\n", min_F);

    free(A);
    return 0;
}

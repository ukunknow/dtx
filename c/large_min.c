#include <stdio.h>
#include <stdlib.h>

int can_place_rooms(int *arr, int n, int k, int mid) {
    int count = 1;
    int curr = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] - curr >= mid) {
            count++;
            curr = arr[i];
        }
    }

    return count >= k;
}

int largest_minimum_distance(int *arr, int n, int k) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    int low = 1;
    int high = arr[n - 1] - arr[0];
    int result = -1;

    while (low <= high) {
        int mid = (low + high) / 2;
        if (can_place_rooms(arr, n, k, mid)) {
            result = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return result;
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    int A[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }

    int result = largest_minimum_distance(A, N, K);
    printf("%d\n", result);

    return 0;
}

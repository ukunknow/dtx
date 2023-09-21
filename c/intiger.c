#include <stdio.h>
#include <string.h>

int roman_to_int(char *s) {
    int roman_values[26]; // Mapping for Roman numerals (A to Z)
    roman_values['I' - 'A'] = 1;
    roman_values['V' - 'A'] = 5;
    roman_values['X' - 'A'] = 10;
    roman_values['L' - 'A'] = 50;
    roman_values['C' - 'A'] = 100;
    roman_values['D' - 'A'] = 500;
    roman_values['M' - 'A'] = 1000;

    int total = 0;
    int prev_value = 0;

    int length = strlen(s);

    for (int i = length - 1; i >= 0; i--) {
        int value = roman_values[s[i] - 'A'];

        if (value < prev_value) {
            total -= value;
        } else {
            total += value;
        }

        prev_value = value;
    }

    return total;
}

int main() {
    char s1[] = "III";
    printf("%d\n", roman_to_int(s1));

    char s2[] = "LVIII";
    printf("%d\n", roman_to_int(s2));

    char s3[] = "MCMXCIV";
    printf("%d\n", roman_to_int(s3));

    return 0;
}


void askForInput(int *n) {
  do {
    printf("Enter the board dimension: ");
    scanf("%d", n);
    removeNewline(n);
    // getchar();  // consume newline character
  } while ((*n % 2 != 0) || *n > 26);
}

// input
int inputConvert(char *input) {
  char a = 'a';
  int n = (int)*input - (int)a;
  return n;
}

bool positionInBounds(int n, int row, int col) {
  if (row < n && col < n && row >= 0 && col >= 0)
    return true;
  else
    return false;
}

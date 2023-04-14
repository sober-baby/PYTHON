//
// Author:
//

// #include "reversi.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void initializeBoard(char board[][26], int n) {
  // char configc = 'a', configr = 'a';
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      board[i][j] = 'U';
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (j == (n - 2) / 2 && i == (n - 2) / 2) {
        board[i][j] = 'W';
        board[i][j + 1] = 'B';
        board[i + 1][j] = 'B';
        board[i + 1][j + 1] = 'W';
      }
    }
  }
}

void printBoard(char board[][26], int n) {
  char configc = 'a', configr = 'a';
  for (int i = 0; i < n + 1; i++) {
    for (int j = 0; j < n + 2; j++) {
      if (i == 0 && j > 1) {
        printf("%c", configc);
        configc++;
      } else if (j == 0 && i > 0) {
        printf("%c", configr);
        configr++;
      } else if (j > 1 && i > 0) {
        printf("%c", board[i - 1][j - 2]);
      } else
        printf(" ");
    }
    printf("\n");
  }
}

// prompt user for input
void askForInput(int *n) {
  do {
    printf("Enter the board dimension: ");
    scanf("%d", n);
    getchar();  // consume newline character
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

/* 1. There must be a continuous straight line of tile(s) of the opponent’s
colour in at least one of the eight directions from the candidate empty position
(North, South, East, West, and diagonals).
2. In the position immediately following the continuous straight line mentioned
in #1 above, a tile of the player’s colour must already be placed. */
bool checkLegalInDirection(char board[][26], int n, int row, int col,
                           char colour, int deltaRow, int deltaCol) {
  int dr = deltaRow, dc = deltaCol;
  bool check = false;
  // if (board[row][col] != 'U')
  //   check = false;

  if (deltaRow == 0 && deltaCol == 0) {  // continuous straight line
    check = false;
  } 
  else {
    int count = 0;  // counts the number of opponents
    while (positionInBounds(n, row + deltaRow, col + deltaCol)) {
      if (board[row + deltaRow][col + deltaCol] == 'U') {
        check = false;
        break;
      } else if (board[row + deltaRow][col + deltaCol] == colour) {
        if (count == 0) {
          check = false;
          break;
        } else {
          check = true;
          break;
        }
      } 
    
      count++;
      
      deltaRow += dr;
      deltaCol += dc;
    }
  }
  return check;
}

int validMove(char board[][26], int n, char colour, int row, int col) {
  int available = 0, r = row, c = col;
  // going through each position
  if (board[row][col] == 'U') {
    for (int i = -1; i <= 1; i++) {
      for (int j = -1; j <= 1; j++) {
        while (checkLegalInDirection(board, n, r, c, colour, i, j) &&
               !(i == 0 && j == 0)) {
          available++;
          r = row + i;
          c = col + j;
        }
        r = row;
        c = col;
      }
    }
  }
  return available;
}

// count available moves to user
int availableMoves(char board[][26], int n, char colour) {
  int count = 0;
  // going through each position
  for (int row = 0; row < n; row++) {
    for (int col = 0; col < n; col++) {
      if (validMove(board, n, colour, row, col)) {
        count++;
      }
    }
  }
  return count;
}

// function to convert move to the colour
void updateBoard(int n, char board[][26], char colour, int row, int col) {
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      int r = row, c = col;
      if (checkLegalInDirection(board, n, row, col, colour, i, j)) {
        board[r][c] = colour;
        while (board[r + i][c + j] != colour) {
          board[r + i][c + j] = colour;
          r += i;
          c += j;
        }
      }
    }
  }
}

void removeNewline(char *str) {
  char *newline = strchr(str, '\n');
  if (newline) {
    *newline = '\0';
  }
}

// function for user moves
void userMove(char board[][26], int n, char colour, int *score, bool *end,
              bool *available) {
  char move[2 + 1];
  if (availableMoves(board, n, colour)) {
    printf("Enter move for colour %c (RowCol): ", colour);
    // getchar();
    // fgets(move, sizeof(move), stdin);
    // removeNewline(move);
    scanf(" %c%c", &move[0], &move[1]);
    int row = inputConvert(move);
    int col = inputConvert(move + 1);

    // check legal
    if (validMove(board, n, colour, row, col) > 0) {
      updateBoard(n, board, colour, row, col);
      printBoard(board, n);
    } else {
      *end = true;
      printf("Invalid move.\n");
    }
  } else {
    printf("%c player has no valid move.\n", colour);
    *available = false;
  }
}

// function for computer move
void computerM(int n, char board[][26], char colour, int *score,
               bool *available) {
  // bool vaid = false;
  int count = 0, row, col;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        int valid = validMove(board, n, colour, i, j);
      if (valid > count) {
        count = validMove(board, n, colour, i, j);
        row = i, col = j;
      }
    }
  }
  if (count == 0) {
    printf("%c player has no valid move.\n", colour);
    *available = false;
  } else {
    printf("Computer places %c at %c%c.\n", colour, row+'a', col+'a');
    updateBoard(n, board, colour, row, col);
    printBoard(board, n);
  }
  *score = count;
}

// full board
bool isBoardFull(int n, char board[][26]) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (board[i][j] == 'U') {
        return false;
      }
    }
  }
  return true;
}

char countScore(char board[][26], int n) {}

int main(void) {
  // prompt user for input
  int n = 0;
  askForInput(&n);

  // print board
  char board[26][26];
  initializeBoard(board, n);

  // choose player
  char colourc, colouru, colour;
  int scoreC = 0, scoreU = 0;  // set up scores for computer and user
  bool end = false;
  printf("Computer plays (B/W): ");
  scanf("%c", &colourc);

  if (colourc == 'W')
    colouru = 'B';
  else
    colouru = 'W';

  printBoard(board, n);
  // rounds of operation
  // board not full,
  bool count = 0;
  bool available = true, availableU = true, availableC = true;
  while (!(isBoardFull(n, board) || end) && available) {
    // change colour
    if (count) {
      colour = 'W';
    } else
      colour = 'B';
    // if available
    if (colourc == colour) {
      computerM(n, board, colourc, &scoreC, &availableC);
    } else {
      userMove(board, n, colouru, &scoreU, &end, &availableU);
    }
    count = !count;

    if (!(availableU && availableC)) available = false;
  }

  if (end) {
    printf("%c player wins.\n", colourc);
  }

  else if (isBoardFull(n, board)) {
    // check the score
  }

  // //ask user to enter move
  // userMove(board, n);
  return 0;
}

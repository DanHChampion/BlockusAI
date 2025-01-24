const boardSize = 20;
const boardElement = document.getElementById('board');
const board = createEmptyBoard();

// Create the board dynamically
function createBoard() {
  boardElement.innerHTML = '';
  for (let i = 0; i < boardSize; i++) {
    for (let j = 0; j < boardSize; j++) {
      const cell = document.createElement('div');
      cell.classList.add('cell');
      if (board[i][j] === 1) cell.classList.add('red');
      if (board[i][j] === 2) cell.classList.add('green');
      if (board[i][j] === 3) cell.classList.add('yellow');
      if (board[i][j] === 4) cell.classList.add('blue');
      cell.dataset.row = i;
      cell.dataset.col = j;
      boardElement.appendChild(cell);

      // Add click listener to place blocks
      cell.addEventListener('click', () => {
        placeBlock(i, j);
      });
    }
  }
}

function createEmptyBoard() {
  const board = [];
  for (let i = 0; i < boardSize; i++) {
    board.push(Array(boardSize).fill(0));
  }
  return board;
}

function placeBlock(row, col) {
  board[row][col] = 1;
  createBoard();
}

// Initial rendering
createBoard();

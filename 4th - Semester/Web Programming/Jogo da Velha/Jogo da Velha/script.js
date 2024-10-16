const bigBoard = document.getElementById('big-board');
const statusDiv = document.getElementById('status');
let currentPlayer = Math.random() < 0.5 ? 'X' : 'O';
let nextBoard = null;
let gameOver = false;
let bigBoardState = Array(9).fill(null);
let smallBoards = [];

for (let i = 0; i < 9; i++) {
    const smallBoard = document.createElement('div');
    smallBoard.classList.add('small-board');
    smallBoard.dataset.index = i;
    bigBoard.appendChild(smallBoard);

    let smallBoardState = Array(9).fill(null);
    smallBoards.push(smallBoardState);

    for (let j = 0; j < 9; j++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.index = j;
        cell.addEventListener('click', () => handleMove(i, j));
        smallBoard.appendChild(cell);
    }
}

function handleMove(boardIndex, cellIndex) {
    if (gameOver || (nextBoard !== null && nextBoard !== boardIndex)) {
        return;
    }

    const smallBoardState = smallBoards[boardIndex];
    if (smallBoardState[cellIndex] !== null) {
        return;
    }

    smallBoardState[cellIndex] = currentPlayer;
    document.querySelector(`.small-board[data-index='${boardIndex}'] .cell[data-index='${cellIndex}']`).textContent = currentPlayer;

    if (checkWin(smallBoardState)) {
        bigBoardState[boardIndex] = currentPlayer;
        updateBigBoardDisplay(boardIndex);
        if (checkWin(bigBoardState)) {
            statusDiv.textContent = `O jogador  ${currentPlayer} Ganhou!`;
            gameOver = true;
            return;
        }
    } else if (smallBoardState.every(cell => cell !== null)) {
        bigBoardState[boardIndex] = 'C'; // Mark as coringa
        updateBigBoardDisplay(boardIndex);
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    nextBoard = smallBoardState[cellIndex] === null ? cellIndex : null;
    updateStatus();
}

function checkWin(boardState) {
    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ];
    return winningCombinations.some(combination => {
        const [a, b, c] = combination;
        return (boardState[a] === currentPlayer || boardState[a] === 'C') &&
            (boardState[b] === currentPlayer || boardState[b] === 'C') &&
            (boardState[c] === currentPlayer || boardState[c] === 'C');
    });
}

function updateBigBoardDisplay(boardIndex) {
    const board = document.querySelector(`.small-board[data-index='${boardIndex}']`);
    const state = bigBoardState[boardIndex];
    if (state === 'C') {
        board.style.backgroundColor = 'grey';
    } else {
        board.style.backgroundColor = state === 'X' ? 'lightblue' : 'lightcoral';
    }
    board.querySelectorAll('.cell').forEach(cell => cell.style.pointerEvents = 'none');
}

function updateStatus() {
    if (gameOver) {
        return;
    }
    statusDiv.textContent = `É a vez do jogador ${currentPlayer}'`;
}

updateStatus();

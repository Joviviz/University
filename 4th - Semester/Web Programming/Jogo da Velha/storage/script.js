const X_CLASS = 'x';
const CIRCLE_CLASS = 'circle';
const WINNING_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

const mainBoard = document.getElementById('mainBoard');
const miniBoards = document.querySelectorAll('.mini-board');
const winningMessageElement = document.getElementById('winningMessage');
const winningMessageTextElement = document.querySelector('[data-winning-message-text]');
const restartButton = document.getElementById('restartButton');
let circleTurn;

startGame();

restartButton.addEventListener('click', startGame);

function startGame() {
    circleTurn = false;
    miniBoards.forEach(miniBoard => {
        miniBoard.innerHTML = ''; // Limpa os mini tabuleiros
        miniBoard.classList.remove(X_CLASS, CIRCLE_CLASS);
        createMiniBoard(miniBoard);
    });
    setBoardHoverClass();
    winningMessageElement.classList.remove('show');
}

function createMiniBoard(miniBoard) {
    for (let i = 0; i < 9; i++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.addEventListener('click', handleClick, { once: true });
        miniBoard.appendChild(cell);
    }
}

function handleClick(e) {
    const cell = e.target;
    const currentClass = circleTurn ? CIRCLE_CLASS : X_CLASS;
    placeMark(cell, currentClass);
    const miniBoard = cell.parentElement;
    if (checkWin(currentClass, miniBoard)) {
        endMiniGame(currentClass, miniBoard);
        if (checkWin(currentClass, mainBoard)) {
            endGame(false);
        } else if (isDraw(mainBoard)) {
            endGame(true);
        } else {
            swapTurns();
            setBoardHoverClass();
        }
    } else if (isDraw(miniBoard)) {
        miniBoard.classList.add('draw');
        swapTurns();
        setBoardHoverClass();
    } else {
        swapTurns();
        setBoardHoverClass();
    }
}

function endMiniGame(currentClass, miniBoard) {
    miniBoard.classList.add(currentClass);
    miniBoard.querySelectorAll('.cell').forEach(cell => cell.removeEventListener('click', handleClick));
}

function endGame(draw) {
    if (draw) {
        winningMessageTextElement.innerText = 'Empate!';
    } else {
        winningMessageTextElement.innerText = `${circleTurn ? "O" : "X"} Venceu!`;
    }
    winningMessageElement.classList.add('show');
}

function isDraw(board) {
    const cells = board.querySelectorAll('.cell');
    return [...cells].every(cell => {
        return cell.classList.contains(X_CLASS) || cell.classList.contains(CIRCLE_CLASS);
    });
}

function placeMark(cell, currentClass) {
    cell.classList.add(currentClass);
    cell.innerText = currentClass === X_CLASS ? 'X' : 'O';
}

function swapTurns() {
    circleTurn = !circleTurn;
}

function setBoardHoverClass() {
    mainBoard.classList.remove(X_CLASS);
    mainBoard.classList.remove(CIRCLE_CLASS);
    if (circleTurn) {
        mainBoard.classList.add(CIRCLE_CLASS);
    } else {
        mainBoard.classList.add(X_CLASS);
    }
}

function checkWin(currentClass, board) {
    const cells = board.querySelectorAll('.cell');
    return WINNING_COMBINATIONS.some(combination => {
        return combination.every(index => {
            return cells[index].classList.contains(currentClass);
        });
    });
}

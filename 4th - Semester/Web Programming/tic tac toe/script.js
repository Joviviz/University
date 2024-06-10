let turn = 'X'
let table
let title

function clearTable() {
    for (const row of table.children) {
        for (const cell of row.children) {
            cell.innerHTML = ' '
        }
    }
}

function checkWinner() {
    const tableValues = []
    for (const row of table.children) {
        tableValues.push([])
        for (const cell of row.children) {
            tableValues.at(-1).push(cell.innerHTML)
        }
    }

    let winner = checkHorizontalWinner(tableValues)
    if (winner) {
        return winner
    }
    winner = checkVerticalWinner(tableValues)
    if (winner) {
        return winner
    }
    winner = checkDiagonalWinner(tableValues)
    if (winner) {
        return winner
    }
}

function checkHorizontalWinner(tableValues) {
    for (let i = 0; i < 3; i++) {
        if (tableValues[0][i] !== ' '
            && tableValues[0][i] === tableValues[1][i]
            && tableValues[0][i] === tableValues[2][i]) {
            return tableValues[0][i]
        }
    }
}

function checkVerticalWinner(tableValues) {
    for (let i = 0; i < 3; i++) {
        if (tableValues[i][0] !== ' '
            && tableValues[i][0] === tableValues[i][1]
            && tableValues[i][0] === tableValues[i][2]) {
            return tableValues[i][0]
        }
    }
}

function checkDiagonalWinner(tableValues) {
    if (tableValues[0][0] !== ' '
        && tableValues[0][0] === tableValues[1][1]
        && tableValues[0][0] === tableValues[2][2]) {
        return tableValues[0][0]
    }

    if (tableValues[0][2] !== ' '
        && tableValues[0][2] === tableValues[1][1]
        && tableValues[0][2] === tableValues[2][0]) {
        return tableValues[0][2]
    }
}

function addClickEvent() {
    for (const row of table.children) {
        for (const cell of row.children) {
            cell.addEventListener('click', () => {
                if (cell.innerHTML !== ' ') {
                    return
                }
                cell.innerHTML = turn
                turn = turn === 'X' ? 'O' : 'X'
                title.innerHTML = `É a vez do ${turn}`
                const winner = checkWinner()
                if (winner) {
                    title.innerHTML = `O vencedor é ${winner}`
                }
            })
        }
    }
}


document.addEventListener("DOMContentLoaded", () => {
    table = document.getElementById("tabuleiro")
    title = document.getElementById('title')
    const resetButton = document.getElementById('reset')
    resetButton.addEventListener('click', clearTable)
    clearTable(table)
    addClickEvent(table)
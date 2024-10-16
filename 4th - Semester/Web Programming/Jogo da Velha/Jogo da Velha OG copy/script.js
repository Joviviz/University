let turn = 'X'
let table
let title
let finished = false

function clearTable() {
    finished = false
    for (const row of table.children) {
        for (const cell of row.children) {
            cell.innerHTML = ' '
            cell.className = ''
            title.innerHTML = `É a vez do ${turn}`
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
    if (checkDraw(tableValues)) {
        return {
            value: "Velha"
        }
    }

    return null
}

function checkHorizontalWinner(tableValues) {
    for (let i = 0; i < 3; i++) {
        if (tableValues[0][i] !== ' '
            && tableValues[0][i] === tableValues[1][i]
            && tableValues[0][i] === tableValues[2][i]) {
            return {
                value: tableValues[0][i],
                cells: [[0, i], [1, i], [2, i]]
            }
        }
    }
}

function checkVerticalWinner(tableValues) {
    for (let i = 0; i < 3; i++) {
        if (tableValues[i][0] !== ' '
            && tableValues[i][0] === tableValues[i][1]
            && tableValues[i][0] === tableValues[i][2]) {
            return {
                value: tableValues[i][0],
                cells: [[i, 0], [i, 1], [i, 2]]
            }
        }
    }
}

function checkDiagonalWinner(tableValues) {
    if (tableValues[0][0] !== ' '
        && tableValues[0][0] === tableValues[1][1]
        && tableValues[0][0] === tableValues[2][2]) {
        return {
            value: tableValues[0][0],
            cells: [[0, 0], [1, 1], [2, 2]]
        }
    }

    if (tableValues[0][2] !== ' '
        && tableValues[0][2] === tableValues[1][1]
        && tableValues[0][2] === tableValues[2][0]) {
        return {
            value: tableValues[0][2],
            cells: [[0, 2], [1, 1], [2, 0]]
        }
    }
}

function checkDraw(tableValues) {
    let filled = 0
    for (const row of tableValues) {
        for (const cell of row) {
            if (cell !== " ") {
                filled++
            }
        }
    }

    return filled === 9
}

function clickCell(event) {
    const cell = event.target
    if (cell.innerHTML !== ' ' || finished) {
        return
    }
    cell.innerHTML = turn
    turn = turn === 'X' ? 'O' : 'X'
    title.innerHTML = `É a vez do ${turn}`
    const winner = checkWinner()
    if (winner) {
        title.innerHTML = `O vencedor é ${winner.value}`
        for (const cell of winner.cells) {
            table.children[cell[0]].children[cell[1]].className = 'winner'
        }
        finished = true
    }
}

function addClickEvent() {
    for (const row of table.children) {
        for (const cell of row.children) {
            cell.addEventListener('click', clickCell)
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
})

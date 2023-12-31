const game = document.getElementById('game');
const canvas = document.getElementById('blockus-canvas');
const ctx = canvas.getContext('2d');


const boardSize = 20;
let paddingX = 0;
let paddingY = 0;

const gap = 10;
const board = createEmptyBoard();
var canvasSizeX = game.offsetWidth;
var canvasSizeY = game.offsetHeight;
var blockSize = canvasSizeX/40;
// Set canvas size
canvas.width = canvasSizeX;
canvas.height = canvasSizeY;

const playerBoxSizeX = blockSize*boardSize/2;
const playerBoxSizeY = blockSize*boardSize/4 - gap*0.75;

const controlsBoxSizeX = playerBoxSizeX + blockSize*boardSize + gap;
const controlsBoxSizeY = playerBoxSizeY*1.5;


let offsetX = 0;
let offsetY = 0;
let piece = [[0,1,0],
                [1,1,1],
                [0,1,0]];
let pieceRows = piece.length;
let pieceCols = piece[0].length;
    
let cellSize = 10;




function createEmptyBoard() {
    const board = [];
    for (let i = 0; i < boardSize; i++) {
        board.push(Array(boardSize).fill(0));
    }
    return board;
}

function drawBoard(clear = false) {
    canvasSizeX = game.offsetWidth;
    canvasSizeY = game.offsetHeight;
    blockSize = canvasSizeX/40;
    
    paddingX = (canvasSizeX - controlsBoxSizeX) /2;
    paddingY = (canvasSizeY - (blockSize*boardSize + controlsBoxSizeY + gap*3)) /2;

    let boardOffsetX = playerBoxSizeX + gap*2 + paddingX;
    let boardOffsetY = gap + paddingY;



    for (let i = 0; i < boardSize; i++) {
        for (let j = 0; j < boardSize; j++) {
            if (board[i][j] === 1 && !clear) {
                ctx.fillStyle = '#3498db';
            } else {
                ctx.fillStyle = '#ddd';
            }
            ctx.fillRect(boardOffsetX + j * blockSize, boardOffsetY + i * blockSize, blockSize, blockSize);
            ctx.strokeStyle = '#fff';
            ctx.strokeRect(boardOffsetX + j * blockSize, boardOffsetY + i * blockSize, blockSize, blockSize);
        }
    }

    let playerBoxOffsetX = gap + paddingX;
    let playerBoxOffsetY = gap + paddingY;
    ctx.fillStyle = 'red';
    ctx.fillRect(playerBoxOffsetX, playerBoxOffsetY, playerBoxSizeX, playerBoxSizeY);

    playerBoxOffsetY += playerBoxSizeY + gap;

    ctx.fillStyle = 'green';
    ctx.fillRect(playerBoxOffsetX, playerBoxOffsetY, playerBoxSizeX, playerBoxSizeY);
    
    playerBoxOffsetY += playerBoxSizeY + gap;    

    ctx.fillStyle = 'yellow';
    ctx.fillRect(playerBoxOffsetX, playerBoxOffsetY, playerBoxSizeX, playerBoxSizeY);

    playerBoxOffsetY += playerBoxSizeY + gap;

    ctx.fillStyle = 'blue';
    ctx.fillRect(playerBoxOffsetX, playerBoxOffsetY, playerBoxSizeX, playerBoxSizeY);

    // Controls
    const controlsBoxOffsetY = blockSize*boardSize + gap*2 + paddingY;

    ctx.fillStyle = 'grey';
    ctx.fillRect(playerBoxOffsetX, controlsBoxOffsetY, controlsBoxSizeX, controlsBoxSizeY);
}

function placeBlock(x, y) {
    board[y][x] = 1;
    drawBoard();
}

// canvas.addEventListener('click', function (event) {
//     const x = Math.floor((event.offsetX - boardOffsetX) / blockSize);
//     const y = Math.floor((event.offsetY - boardOffsetY) / blockSize);
//     placeBlock(x, y);
// });

function getMousePos(canvas, event) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: event.clientX - rect.left,
        y: event.clientY - rect.top,
    };
}
    
// Function to check whether a point is inside a rectangle
function isInside(pos, rect) {
return pos.x > rect.x && pos.x < rect.x + rect.width && pos.y < rect.y + rect.height && pos.y > rect.y
}

function drawPieces(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBoard();
    console.log("pieceRows",pieceRows);
    
    for (let i = 0; i < pieceRows; i++) {
        for (let j = 0; j < pieceCols; j++) {
            if (piece[i][j] === 1) {
                console.log("square");
                ctx.fillStyle = 'black';
                ctx.fillRect(offsetX + j * cellSize, offsetY + i * cellSize, cellSize, cellSize);
                ctx.strokeStyle = '#fff';
                ctx.strokeRect(offsetX + j * cellSize,offsetY + i * cellSize, cellSize, cellSize);
            }
        }
    }
}

let isDragging = false;

function handleMouseDown(e) {
    const mouseX = e.clientX - canvas.getBoundingClientRect().left;
    const mouseY = e.clientY - canvas.getBoundingClientRect().top;

    if (
        mouseX >= offsetX &&
        mouseX <= offsetX + pieceCols * cellSize &&
        mouseY >= offsetY &&
        mouseY <= offsetY + pieceRows * cellSize
    ) {
        isDragging = true;
        offsetX = mouseX - (offsetX + 0.5 * cellSize);
        offsetY = mouseY - (offsetY + 0.5 * cellSize);
        drawPieces();
    }
}

function handleMouseMove(e) {
    if (isDragging) {
        offsetX = e.clientX - canvas.getBoundingClientRect().left - 0.5 * pieceCols * cellSize;
        offsetY = e.clientY - canvas.getBoundingClientRect().top - 0.5 * pieceRows * cellSize;
        drawPieces();
    }
}

function handleMouseUp() {
    isDragging = false;
}

canvas.addEventListener('mousedown', handleMouseDown);
canvas.addEventListener('mousemove', handleMouseMove);
canvas.addEventListener('mouseup', handleMouseUp);

document.addEventListener('DOMContentLoaded', function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPieces();
    drawBoard();
});

window.addEventListener("resize", (event) => {
    console.log("resize");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPieces();
    drawBoard();
});

function clearTest(){
    console.log("dasdasd");
    drawBoard(true);
}


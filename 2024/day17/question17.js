const fs = require("fs");

// Read and parse input
const data = fs.readFileSync("input.txt", "utf8").trim();
const [x1, x2, y1, y2] = data.match(/-?\d+/g).map(Number);
const xMin = Math.min(x1, x2);
const xMax = Math.max(x1, x2);
const yMin = Math.min(y1, y2);
const yMax = Math.max(y1, y2);

// Part 1: Calculate maximum height
const maxVy = Math.abs(yMin) - 1;
const part1 = (maxVy * (maxVy + 1)) / 2;
console.log("Part 1:", part1);

// Part 2: Count all valid initial velocities
function simulate(vx, vy) {
  let x = 0,
    y = 0;
  let currentVx = vx,
    currentVy = vy;

  while (true) {
    x += currentVx;
    y += currentVy;

    if (currentVx > 0) currentVx--;
    else if (currentVx < 0) currentVx++;
    currentVy--;

    if (x > xMax || y < yMin) return false;
    if (x >= xMin && x <= xMax && y >= yMin && y <= yMax) return true;
  }
}

// Calculate possible velocity ranges
let minVx = Math.ceil((-1 + Math.sqrt(1 + 8 * xMin)) / 2);
while ((minVx * (minVx + 1)) / 2 < xMin) minVx++;
const maxVx = xMax;

const minVy = yMin;
const maxVyPart2 = maxVy;

let count = 0;
for (let vx = minVx; vx <= maxVx; vx++) {
  for (let vy = minVy; vy <= maxVyPart2; vy++) {
    if (simulate(vx, vy)) count++;
  }
}

console.log("Part 2:", count);

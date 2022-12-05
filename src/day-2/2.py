# /*
#  * (1 for Rock, 2 for Paper, and 3 for Scissors)
#  * plus the score for the outcome of the round
#  *(0 if you lost, 3 if the round was a draw, and 6 if you won).
#  *
#  * Opponent: A for Rock, B for Paper, and C for Scissors.
#  *
#  * Me: X for Rock, Y for Paper, and Z for Scissors.
#  */

# const points: Record<string, number> = { A: 1, B: 2, C: 3 };

# import * as fs from "fs";
# import path from "path";
# const result: number[] = [];

# const findDraw = (item: string[]) =>
#   item[0] === item[1] ? result.push(3 + points[item[1]]) : item;

# const findWinOrLoss = (item: number | string[]) => {
#   if (typeof item !== "number") {
#     if (
#       (item[0] === "A" && item[1] === "C") ||
#       (item[0] === "B" && item[1] === "A") ||
#       (item[0] === "C" && item[1] === "B")
#     ) {
#       result.push(0 + points[item[1]]);
#     }
#     if (
#       (item[1] === "A" && item[0] === "C") ||
#       (item[1] === "B" && item[0] === "A") ||
#       (item[1] === "C" && item[0] === "B")
#     ) {
#       result.push(6 + points[item[1]]);
#     }
#   }
#   return item;
# };

# fs.readFileSync(path.resolve(__dirname, "./input.txt"))
#   .toString("utf-8")
#   .split("\n")
#   .map((item) =>
#     item.replace("X", "A").replace("Y", "B").replace("Z", "C").split(" ")
#   )
#   .map(findDraw)
#   .map(findWinOrLoss);

# console.log(
#   "Result if Y,X,Z means the shape 🪨📃✂️: ",
#   result.reduce((a: number, b: number) => a + b, 0)
# );

# /**
#  * X means you need to lose,
#  * Y means you need to end the round in a draw, and Z means you need to win
#  *
#  * Opponent: A for Rock, B for Paper, and C for Scissors.
#  */

# const resultPart2: number[] = [];
# fs.readFileSync(path.resolve(__dirname, "./input_2.txt"))
#   .toString("utf-8")
#   .split("\n")
#   .map((item) => item.split(" "))
#   .map((item) => {
#     if (item[1] === "Y") {
#       if (item[0] === "A") {
#         return ["A", "A"];
#       }
#       if (item[0] === "B") {
#         return ["B", "B"];
#       }
#       if (item[0] === "C") {
#         return ["C", "C"];
#       }
#     }
#     if (item[1] === "X") {
#       if (item[0] === "A") {
#         return ["A", "C"];
#       }
#       if (item[0] === "B") {
#         return ["B", "A"];
#       }
#       if (item[0] === "C") {
#         return ["C", "B"];
#       }
#     }
#     if (item[1] === "Z") {
#       if (item[0] === "A") {
#         return ["A", "B"];
#       }
#       if (item[0] === "B") {
#         return ["B", "C"];
#       }
#       if (item[0] === "C") {
#         return ["C", "A"];
#       }
#     }
#     return item;
#   })
#   .map((item: string[]) =>
#     item[0] === item[1] ? resultPart2.push(3 + points[item[1]]) : item
#   )
#   .map((item: number | string[]) => {
#     if (typeof item !== "number") {
#       if (
#         (item[0] === "A" && item[1] === "C") ||
#         (item[0] === "B" && item[1] === "A") ||
#         (item[0] === "C" && item[1] === "B")
#       ) {
#         resultPart2.push(0 + points[item[1]]);
#       }
#       if (
#         (item[1] === "A" && item[0] === "C") ||
#         (item[1] === "B" && item[0] === "A") ||
#         (item[1] === "C" && item[0] === "B")
#       ) {
#         resultPart2.push(6 + points[item[1]]);
#       }
#     }
#     return item;
#   });

# console.log(
#   "Result if Y,X,Z means draw, win or loss 🪨📃✂️: ",
#   resultPart2.reduce((a: number, b: number) => a + b, 0)
# );

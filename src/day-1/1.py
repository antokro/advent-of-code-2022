#  import * as fs from "fs";
#  import path from "path";
#  const input = fs
#    .readFileSync(path.resolve(__dirname, "./input.txt"))
#    .toString("utf-8")
#    .split("\n")
#    .map((item) => (item === "" ? "seperator" : item))
#    .join()
#    .split("seperator")
#    .map((item) => item.split(",").filter((item) => item !== ""))
#    .map((item) => item.map((item) => parseInt(item)).reduce((a, b) => a + b, 0))
#    .map((number, index) => ({
#      calories: number,
#      elf: index,
#    }))
#    .sort((a, b) => a.calories - b.calories)
#    .reverse();

#  console.log("Elf 🧝🏻 carrying most calories: ", input[0]);
#  console.log("Top 3 Elfs 🧝🏻🧝🏻🧝🏻  carrying most calories", input.slice(0, 3));

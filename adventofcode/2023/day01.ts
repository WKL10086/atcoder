import fs from "fs";
import path from "path";

const input = fs
  .readFileSync(path.resolve(__dirname, "day01.txt"))
  .toString()
  .trim()
  .split("\n");

const part1 = (lines: string[]) => {
  const filtered = lines.map((line) => {
    const filteredLine = line.replace(/[^0-9]/g, "");
    const res = filteredLine[0] + filteredLine[filteredLine.length - 1];
    return parseInt(res);
  });

  return filtered.reduce((acc, curr) => acc + curr, 0);
};

const decode = (line: string) => {
  let decodedLine = "";
  for (let i = 0; i < line.length; i++) {
    if (i + 2 < line.length) {
      const currWord = line.slice(i, i + 3);
      if (currWord === "one") {
        decodedLine += "1";
        i += 2;
        continue;
      } else if (currWord === "two") {
        decodedLine += "2";
        i += 2;
        continue;
      } else if (currWord === "six") {
        decodedLine += "6";
        i += 2;
        continue;
      }
    }

    if (i + 3 < line.length) {
      const currWord = line.slice(i, i + 4);
      if (currWord === "zero") {
        decodedLine += "0";
        i += 3;
        continue;
      } else if (currWord === "four") {
        decodedLine += "4";
        i += 3;
        continue;
      } else if (currWord === "five") {
        decodedLine += "5";
        i += 3;
        continue;
      } else if (currWord === "nine") {
        decodedLine += "9";
        i += 3;
        continue;
      }
    }

    if (i + 4 < line.length) {
      const currWord = line.slice(i, i + 5);
      if (currWord === "three") {
        decodedLine += "3";
        i += 4;
        continue;
      } else if (currWord === "seven") {
        decodedLine += "7";
        i += 4;
        continue;
      } else if (currWord === "eight") {
        decodedLine += "8";
        i += 4;
        continue;
      }
    }

    decodedLine += line[i];
  }

  return decodedLine;
};

const part2 = (lines: string[]) => {
  const filtered = lines.map((line) => {
    const decodedLine = decode(line);
    const filteredLine = decodedLine.replace(/[^0-9]/g, "");
    const res = filteredLine[0] + filteredLine[filteredLine.length - 1];
    return parseInt(res);
  });

  return filtered.reduce((acc, curr) => acc + curr, 0);
};

console.log(part2(input));

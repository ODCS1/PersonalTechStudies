let v = [3, 5, 8, 3, 9];

v.push(1);
v.sort();
console.log(v);
console.log(`O vetor tem ${v.length} posições`);
console.log(`O valor do vetor na primeira posição é ${v[0]}.`);
console.log(`O valor do vetor na última posição é ${v[v.length - 1]}.`);
console.log(v);

let pos = v.indexOf(8);

if (pos == -1) {
  console.log("Ovalaor não foi encontrado");
} else {
  console.log(`O valor está na posição ${pos}`);
}
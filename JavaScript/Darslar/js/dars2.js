// For

// // for tushunchasi JavaScript
//////////////////////////////////////////////// FOR BILAN ISHLASH /////////////////////////////////////////


for (let i = 0; i < 10; i++) { // i++ degani i ni qiymatiga 1 qoshgin degani
    console.log(i)
}

for (let i = 0; i < 10; i+=2) { // agar i+2 deyilganida bu kod natijasi 2 4 6 8  bolai
    console.log(i)
}

for (let i = 0; i <= 10; i+=2) { // agar <= deyilganida bu kod natijasi 2 4 6 8 10  bolai
    console.log(i)
}

for (let i = 0; i <= 10; i++) { // agar <= deyilganida bu kod natijasi 1,2,3,4,5,6,7,8,9,10  bolai
    console.log(i)
}

// second way

let i = 0;

do{
    console.log(i)
    i++
}while(i < 10)

// Third way

let i2 = 0;

while(i < 10) {
    console.log(i)
    i++
}
// // Functions bilan ishlash


// // Function Decloration
// // Bu Turdegi Funksiyani Tepasidanham chaqirib olish mumkin  
// // MyFirstFunction("Abdulhodiy")
// // MyFirstFunction("Abdulhafiz")
// // MyFirstFunction("Abdulaziz")

// // function MyDecorationFunction(name2){
// //     // let name = "Universal AI"
// //     // let name1=prompt("what is your name?")
// //     // var co=(`hi ${name1} my name is ${name}`)
// //     // alert(co)
// //     // alert(`goodbye ${name1} `)
// //     alert(`hi my name is ${name2}`)
// // }

// // // Function Expression
// // // Expression esa oddiy Funksiya

// // let MyExpressionFunction =function (name){
// //     alert(`My name is ${name}`)
// // }

// // MyExpressionFunction("Abdulhodiy")
// // MyExpressionFunction("Abdulhafiz")
// // MyExpressionFunction("Abdulaziz")



// let num =5;

// function Test(name) {
//     let num =10;
//     num++
//     console.log(num)
//     console.log(`${name}`)
// }
// Test("Abdulhodiy")
// console.log(num)

function MyFirstApp(name, age) {
    alert(`hi my name is ${name}`);



    function ShowSkills() {
        let skills = [
            'html',
            'css',
            'JavaScript'
        ]
        for (let i = 0; i < skills.length; i++) {
            alert(skills[i])
        }
    };
    ShowSkills();
    function CheckAge() {
        if (age >= 18) {
            alert(`Exacltly data for learning IT`);
        } else if (age < 18) {
            alert(`Super data for learning IT`);
        };


    };
    CheckAge();


};

function clc(num) {
    return num * num;
};

console.log(clc(3));

MyFirstApp(`Abdulhodiy`,16);
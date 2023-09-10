// function calc(number){
//     return function(){
//         console.log(10 * number)
//     }
// }

// const clac2=calc(8);

// console.log(clac2)
// clac2()
// function Calc(number){
//     return function(n){
//         return n * number
//     }
// }
// const multTen  = Calc(10)
// const mullttwenty=Calc(20)
// console.log(mullttwenty(80))

// const letx=multTen(10)

// console.log(letx)
// google.com netflix.com domens

// function urlGenerator(domain){
//     return function (host){
//         return `https://${host}.${domain}`
//     }
// };
// const generate=urlGenerator('com')

// console.log(generate('google'))




/*
  
*/
function personeInfo(){
    console.log(`
    Name: ${this.name},
    Age: ${this.age},
    job: ${this.job},
    `)
};

const me={
    name:"Abdulhdiy",
    age:19,
    job:'Front-End-Dev',
}
const me2={
    name:"Abdulhdiy",
    age:17,
    job:'Back-End-Dev',
}

const me1={
    name:"Abdulhdiy",
    age:20,
    job:'Full-Stack-Dev',
}
function bind(fn,fx){
    return function(...args){
        fx.apply(fn,args)
    }
}

bind(me,personeInfo)()
bind(me1,personeInfo)()
bind(me2,personeInfo)()
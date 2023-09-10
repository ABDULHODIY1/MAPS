// // 6 Dars Mavzu : Context this, bind, call, alpy lar haqida
// function same() {
//     console.log(this)
// }
// const person = {
//     name: 'Abdulhodiy',
//     age: 19,
//     job: 'ReactJS dev',
//     callContext: same,
//     collAnotherContext: same.bind(window),
//     callinfojob: function (number) {
//         console.group(`${this.name}`);
//         console.log(`Name is ${this.name}`);
//         console.log(`Age is ${this.age}`);
//         console.log(`Job Is ${this.job}`);
//         console.log(`Phone Number${number}`)
//         console.groupEnd()
//     }
// };
// const furontentdev = {
//     name: 'Abdulboriy',
//     age: 18,
//     job: 'Front-End dev',
// };
// //bind bilan
// const fullinfo = person.callinfojob.bind(furontentdev);
// fullinfo(" +998 (99)-872-12-80")

// //apply bilan

// person.callinfojob.apply(furontentdev, ['+998 (99)-872-12-80'])
 
// //call bilan

// person.callinfojob.call(furontentdev, '+998 (99)-872-12-80')


//========//
const array=[10,20,30,40,50]

// function add(arr, number) {
//     return arr.map(function(i){
//         return i * number
//     })
// }

Array.prototype.logger = function(number) {
    console.log('Prototype',this)
    return this.map(function(i){
        return i * number
    })
}
console.log(array.logger(2))
//console.log(add(array,10))


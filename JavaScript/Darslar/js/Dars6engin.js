let reciveBtn = document.querySelector("#recive"),
    chooseBtn = document.getElementById("choose"),
    text = document.getElementsByTagName("h1")[0],
    btn=document.querySelector(".btn"),
    btn2=document.querySelectorAll("#btn2"),
    color = document.querySelector(".text2")[0],
    confor = document.getElementsByName("input")[0],
    tex6 = document.getElementsByName("printer")[0];
    // bodyx = document.querySelector("#idbody");

// btn2.addEventListener("click", function(){
//     bodyx.style.background="red"
// })
// //First way (No)
// // function hover() {
// // }
// console.log(reciveBtn)
// // Second way (No)
// // text.onmouseenter = hover

// // Thrid Way (Yes)
// // text.addEventListener("mouseenter", function () {
// //     text.textContent = "Tugadi"
// // })





text.addEventListener("mouseenter", function (){
    text.textContent = "Tugadi"
})

text.addEventListener("mouseleave", function () {
    text.textContent = "JavaScript darsi uchun web sayt"
})


confor.addEventListener("input" ,function(){
    tex6.value = `${confor.value}`
})


reciveBtn.addEventListener('click', function(){
    text.style.background = "black"
})

chooseBtn.addEventListener('click', function(){
    text.style.background = "none"
})
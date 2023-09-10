let ans=[]
let questions=[
    "hey what is your name?",
    "what is your phone number?",
    "how old are you?",
]

 for (let i = 0; i < questions.length; i++) {
    ans[i]=prompt(questions[i])
 }
 console.log(ans)
let i=0;

while(i < questions.length) {
        // console.log(i)
        ans[i]=prompt(questions[i])
        i++
    }
console.log(ans)

do{
    ans[i] = prompt(questions[i])    
    i++
}while(i < questions.length)
console.log(ans)




// o`z ijodimdan \|/
let info = [
    "salom ushbu sayt JavaScriptda tayyorlandi",
    "biz siz ushbu saytga kirganingizdan hursandmiz",
    "xayr",
]

for (let i = 0; i < info.length; ++i) { 
    alert(info[i])
}

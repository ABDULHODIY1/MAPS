

// #4 dars

// shartlar if else

let age = +prompt("yoshingiz nechida?")//data type number yani integer

if (age < 18) {
    alert("saytga kira olmaysiz")
} else if (age > 80) {
    alert("ajoib odam ekansizku")
} else {
    alert("hush kelibsiz")
}


switch(age){
    case "18":
        alert("sizi yoshiz 18 da")
        break

    case "50":
        alert("siz 50 yoshdasiz")
        break
        
    default:
        alert("sizi yoshizi topa olmadim")
};


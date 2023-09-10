// // Mavzu: 
// /*
// {
//     0-) Class;
//     1-) Class extends;
//     2-) Setters and Getters;
//     3-) Static Type
//     4-) Practicum;

// }
// */

// // 0-) Class; and 1-) Class extends; // 2-) Gettsrs and Setters; 3-) Static Type;
// class ObjectsClass 
// {
//     constructor
//     (
//         options
//     )
//     {
//         this.name = options.name
//         this.isAirBag = options.AiroBag
//         this.exb = options.exb
//     }
//     speed(){
//         console.log("380 km/h")
//     }
// }

// const lombo= new ObjectsClass(
//     {
//         name:"Lombarghini",
//         isAirBag:true,
//         exb:2
//     }
// )

// class Bus extends ObjectsClass 
// {
//     static type = "Bus"
//     constructor
//     (
//         options
//     )
//     {
//         super
//         (
//             options
//         );
//         this.weight = options.weight;
//     }
//     speed()
//     {
//         console.log
//         (
//             '50 km/h'
//         )
//     }
//     get exbin()
//     {
//         return this.exb * 2; 
//     }

//     set exbin(NewValue)
//     {
//         this.exb = NewValue
//     }
// }

// const MAN = new Bus
// (
//     {
//         name:"MAN",
//         isAirBag:false,
//         exb:1,
//         weight:'4T',
//     }
// ) 

console.log("4-) Practicum")
// 4-) Practicum

class Comp {
    constructor(selector) {
        this.$el = document.querySelector(selector)
    }

    showeel() {
        this.$el.style.display = "block"
    }

    hiddenel() {
        this.$el.style.display = "none"
    }
}

class Squer extends Comp {
    constructor(options) {
        super(options.selector);
        this.$el.style.width = this.$el.style.height = options.size+'px'
        this.$el.style.background = options.color
    }
}

const Squer1 = new Squer(
    {
        selector: '#selectorx',
        size: 100,
        rd:50,
        color: 'coral',
    }
)
const Squer2 = new Squer(
    {
        selector: '#selectory',
        size: 100,
        color: 'crimson',
        rd:50,
    }
)

class Circle extends Squer{
    constructor(options){
        super(options);
        this.$el.style.borderRadius=options.rd+"%";
    }
}

const circle=new Circle(

    {
        selector: '#selectory',
        rd:50
    }
)
const circle2=new Circle(

    {
        selector: '#selectorx',
        rd:50
    }
)
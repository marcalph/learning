// inherit from function constructor
function Animal() { }
Animal.prototype.eat = function() { console.log("nom nom nom"); };
function Dog() { }
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
  console.log("Woof!");
};
let beagle = new Dog();

// override inherited function
function Bird() { }
Bird.prototype.fly = function() { return "I am flying!"; };
function Penguin() { }
Penguin.prototype = Object.create(Bird.prototype);
Penguin.prototype.constructor = Penguin;
Penguin.prototype.fly = () => {
  return "Alas, this is a flightless bird."
}

let penguin = new Penguin();
console.log(penguin.fly());

// mixin
let bird = {
    name: "Donald",
    numLegs: 2
  };
let boat = {
    name: "Warrior",
    type: "race-boat"
  };
let glideMixin  = (obj) => {
    obj.glide = () => {
        return "They see me glidin', they hatin'"
        }
    }
glideMixin(boat)
glideMixin(bird)


// closure to protect variable, instead of this.weight
function Bird() {
    let weight = 15;
    this.getWeight = () => {return weight}
  }
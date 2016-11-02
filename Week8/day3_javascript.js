console.log("Getting started with javascript");

var myNumber = 10;
console.log(myNumber);

var myArray = [10, 'sam', [4, 12, 22], 'sandwich'];
console.log(myArray);
console.log(myArray[2][0]);

for (var i = 0 ; i < myArray.length ; i++) {
  var item = myArray[i];
  console.log(item);
}

var myObject = {
  "myName": "sam",
  "myAge": 23
};
console.log(myObject.myName);

var myFunc = function(x, y) {
  return x * y;
};

console.log(myFunc(9, 4));

var sillyArray = [2, 4, 3, 5, 23];

var loopFunc = function(item) {
  console.log(item);
};

sillyArray.forEach(loopFunc);

sillyArray.forEach(function(item) {
  console.log(item);
});

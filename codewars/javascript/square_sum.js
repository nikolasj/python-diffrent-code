function squareSum(numbers) {
    var sum_ = 0;
    for (let i = 0; i < numbers.length; i++) {
        sum_ += numbers[i] * numbers[i];
    }
    return sum_;
}

squareSum([1,2]);


// function square(number) {
//   return number * number;
// }

// function squareSum(numbers){
//   return numbers.reduce(function(sum, n){
//     return (n*n) + sum;
//   }, 0)
// }
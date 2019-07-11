//Package diffsquares implements functions related to the sum of the squares,
// the square of the sum and the difference between both of the first n natural
// numbers
package diffsquares

import "math"

// SquareOfSum calculates the square of the sum of the first n natural numbers
func SquareOfSum(n int) int {
	sum := (n * (n + 1)) / 2
	return int(math.Pow(float64(sum), 2))
}

// SumOfSquares calculates the sum of the square of the first n natural numbers
func SumOfSquares(n int) int {
	return (n * (n + 1) * (2*n + 1)) / 6
}

// Difference calculates the the difference between the square of the sum of the
// first ten natural numbers and the sum of the squares of the first n natural
// numbers
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}

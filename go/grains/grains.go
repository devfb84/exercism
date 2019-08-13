//Package grains implements solution for the wheat and chessboard problem
package grains

import "math"
import "errors"

//Square returns the number of grains given number of the square in the chessboard
func Square(square int) (uint64, error) {
	if square <= 0 || square > 64 {
		return 0, errors.New("Input out of range")
	}

	return uint64(math.Pow(2, float64(square-1))), nil
}

//Total returns the total of grains on a chessboard
func Total() uint64 {
	return 18446744073709551615
}

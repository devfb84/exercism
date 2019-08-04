//Package luhn implements functions related to Luhn formula
package luhn

import (
	"unicode"
)

//Valid validates than a number is valid per the Luhn formula
func Valid(input string) bool {
	if len(input) <= 1 {
		return false
	}

	digits := []rune(input)
	validCount := 0
	sum := 0

	for i := len(digits) - 1; i >= 0; i-- {
		if unicode.IsSpace(digits[i]) {
			continue
		}

		if digits[i] < '0' || digits[i] > '9' {
			return false
		}

		sum += checksum(validCount, toInt(digits[i]))
		validCount++
	}

	return validCount > 1 && sum%10 == 0
}

// converts rune digit to integer
func toInt(digit rune) int {
	return int(digit) - '0'
}

// computes the checksum for the digit
func checksum(i int, digit int) int {
	if i%2 == 0 {
		return digit
	}

	digit *= 2

	if digit > 9 {
		digit -= 9
	}

	return digit
}

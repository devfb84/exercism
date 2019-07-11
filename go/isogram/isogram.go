//Package isogram implements functions related  isograms
package isogram

import "unicode"

// IsIsogram determines if a word or phrase is an isogram.
func IsIsogram(word string) bool {
	seen := make(map[rune]bool)

	for _, char := range word {
		if !unicode.IsLetter(char) {
			continue
		}

		r := unicode.ToUpper(char)
		if seen[r] {
			return false
		}
		seen[r] = true
	}

	return true
}

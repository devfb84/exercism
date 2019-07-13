//Package luhn implements functions related to Luhn formula
package luhn


func spaceStringsBuilder(str string) string {
    var b strings.Builder
    b.Grow(len(str))
    for _, ch := range str {
        if !unicode.IsSpace(ch) {
            b.WriteRune(ch)
        }
    }
    return b.String()
}


//checks if a given string is valid per Luhn formula
func Valid(input string) bool{
  if len(input) <= 1{
    return false
  }

  return true
}

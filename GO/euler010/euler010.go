package main

import (
	"fmt"
	"math"
)

func isPrime(num int) bool {
	for i := 2; i < int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var total int = 2
	var i int = 3
	for i < 2000000 {
		if isPrime(i) {
			total = total + i
		}
		i = i + 2
	}
	fmt.Println(total)
}

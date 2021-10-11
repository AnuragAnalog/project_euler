package main

import "fmt"

var fact64 uint64 = 1

func factorial(num int) uint64 {
	if num < 0 {
		fmt.Print("Can't be negative number")
	} else {
		for i := 1; i < num; i++ {
			fact64 *= uint64(i)
		}
	}
	return fact64
}

func main() {
	fmt.Println(factorial(50))
}

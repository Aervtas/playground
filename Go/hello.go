package main // this is to make the file a standalone executable

import "fmt" // this is how to import library

func main() { // main is where the executable starts

	// this is how you call a function and print a line to the console
	fmt.Println("Hello, World!")

	// variables are statically typed
	var name string = "Kevin"

	// there is type inference for assigning variables
	weight := 200

	// you can also assign multiple variables
	name2, weight2 := "Janice", 150

	// pointers are available for pointer arithematic is not
	var p *int = &weight

}

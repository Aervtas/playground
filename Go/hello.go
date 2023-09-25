package main // this is to make the file a standalone executable

import "fmt" // this is how to import library

func main() { // main is where the executable starts

	// this is how you call a function and print a line to the console
	fmt.Println("Hello, World!")

	// variables are statically typed
	var name string = "Kevin"
	fmt.Println(name)

	// there is type inference for assigning variables
	weight := 200

	// you can also assign multiple variables
	name2, weight2 := "Janice", 150
	fmt.Println(name2, "is", weight2, "pounds")

	// pointers are available for pointer arithematic is not
	var p *int = &weight
	testFunction(p)
	fmt.Println("Wow! you're", weight, "? you gained weight fast!")

}

func testFunction(x *int) {
	*x += 50
}

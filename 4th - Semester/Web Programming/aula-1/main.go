package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type CalculatorRequest struct {
	A  int    `json:"a"`
	B  int    `json:"b"`
	Op string `json:"op"`
}

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/hello", helloworld)

	mux.HandleFunc("/calculate", calculate)

	mux.HandleFunc("/calculate/add", calculate_add)

	mux.HandleFunc("/calculate/subtract", calculate_subtract)

	mux.HandleFunc("/calculate/multiplicate", calculate_multiplicate)

	mux.HandleFunc("/calculate/divide", calculate_divide)

	http.ListenAndServe("localhost:8080", mux)
}

func helloworld(w http.ResponseWriter, req *http.Request) {
	fmt.Fprint(w, req.Method)
	fmt.Fprint(w, "world")
}

func calculate(w http.ResponseWriter, req *http.Request) {
	var calcRequest CalculatorRequest
	err := json.NewDecoder(req.Body).Decode(&calcRequest)
	if err != nil {
		fmt.Fprint(w, err)
	} else {
		var result int
		switch calcRequest.Op {
		case "+":
			result = calcRequest.A + calcRequest.B
		case "-":
			result = calcRequest.A - calcRequest.B
		case "*":
			result = calcRequest.A * calcRequest.B
		case "/":
			result = calcRequest.A / calcRequest.B
		default:
			fmt.Fprint(w, "Operação não identificada")
			return
		}
		fmt.Fprintf(w, "%d %s %d = %d",
			calcRequest.A, calcRequest.Op, calcRequest.B, result)
	}
}

func calculate_add(w http.ResponseWriter, req *http.Request) {
	var calcRequest CalculatorRequest
	err := json.NewDecoder(req.Body).Decode(&calcRequest)
	if err != nil {
		fmt.Fprint(w, err)
	} else {
		fmt.Fprintf(w, "%d + %d = %d", calcRequest.A, calcRequest.B, calcRequest.A+calcRequest.B)
	}
}

func calculate_subtract(w http.ResponseWriter, req *http.Request) {
	var calcRequest CalculatorRequest
	err := json.NewDecoder(req.Body).Decode(&calcRequest)
	if err != nil {
		fmt.Fprint(w, err)
	} else {
		fmt.Fprintf(w, "%d - %d = %d", calcRequest.A, calcRequest.B, calcRequest.A-calcRequest.B)
	}
}

func calculate_multiplicate(w http.ResponseWriter, req *http.Request) {
	var calcRequest CalculatorRequest
	err := json.NewDecoder(req.Body).Decode(&calcRequest)
	if err != nil {
		fmt.Fprint(w, err)
	} else {
		fmt.Fprintf(w, "%d * %d = %d", calcRequest.A, calcRequest.B, calcRequest.A*calcRequest.B)
	}
}

func calculate_divide(w http.ResponseWriter, req *http.Request) {
	var calcRequest CalculatorRequest
	err := json.NewDecoder(req.Body).Decode(&calcRequest)
	if err != nil {
		fmt.Fprint(w, err)
	} else {
		fmt.Fprintf(w, "%d / %d = %d", calcRequest.A, calcRequest.B, calcRequest.A/calcRequest.B)
	}
}

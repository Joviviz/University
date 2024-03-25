package main

import (
	"aula-database/db"
	"encoding/json"
	"log"
	"net/http"
	"strconv"
)

func main() {
	if err := createServer(); err != nil {
		log.Panic(err)
	}
}

func createServer() error {
	studentRepository := db.NewStudentRepository()

	mux := http.NewServeMux()

	mux.HandleFunc(
		"/students",
		func(w http.ResponseWriter, req *http.Request) {
			switch req.Method {
			case "GET":
				students, err := studentRepository.List()
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}

				err = json.NewEncoder(w).Encode(students)
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}

				w.WriteHeader(200)
			case "POST":
				// Leitura do corpo (INPUT)
				var student db.Student
				err := json.NewDecoder(req.Body).Decode(&student)
				if err != nil {
					http.Error(w, err.Error(), 400)
					return
				}

				
				// Lógica da função/Algoritmo
				id, err := studentRepository.Create(student)
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}

				student.Id = id

				// Output / Resposta
				err = json.NewEncoder(w).Encode(student)
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}
			default:
				http.Error(w, "method not supported", 405)
				return
			}

		})

	mux.HandleFunc(
		"/students/{id}",
		func(w http.ResponseWriter, req *http.Request) {
			// Input
			idRaw := req.PathValue("id")

			id, err := strconv.Atoi(idRaw)
			if err != nil {
				http.Error(w, err.Error(), 400)
				return
			}

			switch req.Method {
			case "GET":
				// processamento
				student, err := studentRepository.Get(id)
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}

				// output
				err = json.NewEncoder(w).Encode(student)
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}
			case "PUT":
				var student db.Student
				err := json.NewDecoder(req.Body).Decode(&student)
				if err != nil {
					http.Error(w, err.Error(), 400)
					return
				}

				err = studentRepository.Update(id, student)
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}
				
				err = json.NewEncoder(w).Encode(student)
				if err != nil {
					http.Error(w, err.Error(), 500)
					return
				}
			case "DELETE":
				// exclusao
			default:
				http.Error(w, "method not supported", 405)
				return
			}

		})

	return http.ListenAndServe("localhost:8080", mux)
}

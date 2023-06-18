package main

import (
	"encoding/json"
	"log"
	"net/http"
)

type Response struct {
	Message string `json:"message"`
}

func main() {
	http.HandleFunc("/", handleRequest)
	http.HandleFunc("/personal-profile", handlePersonalProfile)
	http.HandleFunc("/buy-and-rent", handleBuyAndRent)
	http.HandleFunc("/scan-documents", handleScanDocuments)
	http.HandleFunc("/my-documents", handleMyDocuments)
	http.HandleFunc("/workflow", handleWorkflow)

	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleRequest(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodGet {
		response := Response{Message: "Hello from Go backend!"}
		json.NewEncoder(w).Encode(response)
	} else {
		response := Response{Message: "Invalid request method"}
		json.NewEncoder(w).Encode(response)
	}
}

func handlePersonalProfile(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodGet {
		response := Response{Message: "Fetching personal profile..."}
		json.NewEncoder(w).Encode(response)
	} else if r.Method == http.MethodPost {
		// Логика обработки запроса на обновление персонального профиля
		response := Response{Message: "Updating personal profile..."}
		json.NewEncoder(w).Encode(response)
	} else {
		response := Response{Message: "Invalid request method"}
		json.NewEncoder(w).Encode(response)
	}
}

func handleBuyAndRent(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodGet {
		response := Response{Message: "Fetching buy and rent information..."}
		json.NewEncoder(w).Encode(response)
	} else if r.Method == http.MethodPost {
		// Логика обработки запроса на покупку или аренду
		response := Response{Message: "Processing buy or rent request..."}
		json.NewEncoder(w).Encode(response)
	} else {
		response := Response{Message: "Invalid request method"}
		json.NewEncoder(w).Encode(response)
	}
}

func handleScanDocuments(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodGet {
		response := Response{Message: "Initializing document scanning..."}
		json.NewEncoder(w).Encode(response)
	} else if r.Method == http.MethodPost {
		// Логика обработки запроса на сканирование документов
		response := Response{Message: "Processing document scanning request..."}
		json.NewEncoder(w).Encode(response)
	} else {
		response := Response{Message: "Invalid request method"}
		json.NewEncoder(w).Encode(response)
	}
}

func handleMyDocuments(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodGet {
		response := Response{Message: "Fetching my documents..."}
		json.NewEncoder(w).Encode(response)
	} else {
		response := Response{Message: "Invalid request method"}
		json.NewEncoder(w).Encode(response)
	}
}

func handleWorkflow(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	if r.Method == http.MethodGet {
		response := Response{Message: "Fetching workflow information..."}
		json.NewEncoder(w).Encode(response)
	} else {
		response := Response{Message: "Invalid request method"}
		json.NewEncoder(w).Encode(response)
	}
}

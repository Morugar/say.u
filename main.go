package main

import (
	"app/lib"
	"net/http"
)

func main() {
	lib.Router()
	lib.Handler()
	err := http.ListenAndServe("localhost:8081", nil)
	lib.Check(err)
}

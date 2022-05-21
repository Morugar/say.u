package lib

import (
	"bytes"
	"encoding/json"
	"fmt"
	"github.com/google/uuid"
	"net/http"
	"net/http/cookiejar"
)

func authHandler(w http.ResponseWriter, r *http.Request) {
	login := r.FormValue("login")
	password := r.FormValue("password")

	dataa := map[string]interface{}{
		"login":    login,
		"password": password,
	}

	byteViews, err := json.Marshal(dataa)

	var result Auth

	resp, err := http.Post("http://127.0.0.1:8000/auth", "application/json", bytes.NewBuffer(byteViews))
	Check(err)
	decoder := json.NewDecoder(resp.Body)
	err = decoder.Decode(&result)
	fmt.Println(result)
	fmt.Println("lol")

	jar, err := cookiejar.New(nil)
	Check(err)
	client := http.Client{
		Jar: jar,
	}

	amogus := result.Token
	fmt.Println(amogus)
	cookie := &http.Cookie{
		Name:   "token",
		Value:  amogus,
		MaxAge: 0,
	}

	req, err := http.NewRequest("GET", "http://127.0.0.1:8081/profile", nil)
	Check(err)
	req.AddCookie(cookie)
	resp, err = client.Do(req)
	//err = resp.Body.Close()
	Check(err)

	http.Redirect(w, r, "/", 301)
}

func registrationHandler(w http.ResponseWriter, r *http.Request) {
	name := r.FormValue("name")
	login := r.FormValue("login")
	email := r.FormValue("email")
	password := r.FormValue("password")
	age := r.FormValue("age")

	data := map[string]interface{}{
		"name":     name,
		"login":    login,
		"email":    email,
		"password": password,
		"age":      age,
		"token":    uuid.New(),
	}

	byteViews, err := json.Marshal(data)
	Check(err)
	resp, err := http.Post("http://127.0.0.1:8000/register/", "application/json", bytes.NewBuffer(byteViews))
	Check(err)

	var result map[string]interface{}

	err = json.NewDecoder(resp.Body).Decode(&result)
	Check(err)
	fmt.Println(result)

	http.Redirect(w, r, "/", 301)
}

func changeProfile(w http.ResponseWriter, r *http.Request) {
	fmt.Println("lol")
	name := r.FormValue("name")
	login := r.FormValue("login")
	email := r.FormValue("email")
	social := r.FormValue("social")
	location := r.FormValue("location")
	age := r.FormValue("age")
	hobby := r.FormValue("hobby")
	career := r.FormValue("career")
	education := r.FormValue("education")
	cigaretes := r.FormValue("cigaretes")
	alcohol := r.FormValue("alcohol")
	music := r.FormValue("music")
	films := r.FormValue("films")
	videogames := r.FormValue("videogames")
	serials := r.FormValue("serials")
	books := r.FormValue("books")
	avatar := r.FormValue("avatar")
	fmt.Println(name)
	fmt.Println(age)
	fmt.Println(cigaretes)

	data := map[string]interface{}{
		"token":      "2efec13c-d544-4db2-a9c1-ad67aeea3906",
		"name":       name,
		"login":      login,
		"email":      email,
		"social":     social,
		"location":   location,
		"age":        age,
		"hobby":      hobby,
		"career":     career,
		"cigaretes":  cigaretes,
		"education":  education,
		"alcohol":    alcohol,
		"music":      music,
		"films":      films,
		"videogames": videogames,
		"serials":    serials,
		"books":      books,
		"avatar":     avatar,
	}

	byteViews, err := json.Marshal(data)
	Check(err)
	req, err := http.NewRequest(http.MethodPut, "http://127.0.0.1:8000/changeProfile/", bytes.NewBuffer(byteViews))
	Check(err)
	fmt.Println("kek")
	req.Header.Set("Content-Type", "application/json")
	resp, err := http.DefaultClient.Do(req)
	var result map[string]interface{}
	err = json.NewDecoder(resp.Body).Decode(&result)
	Check(err)
	fmt.Println(result)
	http.Redirect(w, r, "/changeProfile", 301)
}

func Handler() {
	http.HandleFunc("/registration", registrationHandler)
	http.HandleFunc("/auth", authHandler)
	http.HandleFunc("/changeProfile", changeProfile)
}

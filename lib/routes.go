package lib

import (
	"fmt"
	"net/http"
	"text/template"
)

func indexRouter(w http.ResponseWriter, r *http.Request) {

	html, err := template.ParseFiles("patterns/index/index.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "index", nil)
	Check(err)
}

func loginRouter(w http.ResponseWriter, r *http.Request) {
	html, err := template.ParseFiles("patterns/login.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "login", nil)
	Check(err)
}

func registerRouter(w http.ResponseWriter, r *http.Request) {
	html, err := template.ParseFiles("patterns/register.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "register", nil)
	Check(err)
}

func profileRouter(w http.ResponseWriter, r *http.Request) {
	html, err := template.ParseFiles("patterns/profile.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "profile", nil)
	Check(err)

	token, err := r.Cookie("token")
	Check(err)
	fmt.Println(token)
}

func settingRouter(w http.ResponseWriter, r *http.Request) {
	html, err := template.ParseFiles("patterns/settings.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "settings", nil)
	Check(err)
}

func appsRouter(w http.ResponseWriter, r *http.Request) {
	html, err := template.ParseFiles("patterns/apps.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "apps", nil)
	Check(err)
}

func faqRouter(w http.ResponseWriter, r *http.Request) {
	html, err := template.ParseFiles("patterns/faq.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "faq", nil)
	Check(err)
}

func chatRouter(w http.ResponseWriter, r *http.Request) {
	html, err := template.ParseFiles("patterns/chat/chat.html", "patterns/header.html")
	Check(err)
	err = html.ExecuteTemplate(w, "chat", nil)
	Check(err)
}

func Router() {
	http.Handle("/index/", http.StripPrefix("/index/", http.FileServer(http.Dir("./patterns/index"))))
	http.Handle("/assets/", http.StripPrefix("/assets/", http.FileServer(http.Dir("./patterns/index/assets"))))
	http.Handle("/chat/", http.StripPrefix("/chat/", http.FileServer(http.Dir("./patterns/chat"))))
	http.HandleFunc("/", indexRouter)
	http.HandleFunc("/login", loginRouter)
	http.HandleFunc("/register", registerRouter)
	http.HandleFunc("/profile", profileRouter)
	http.HandleFunc("/settings", settingRouter)
	http.HandleFunc("/apps", appsRouter)
	http.HandleFunc("/faq", faqRouter)
	http.HandleFunc("/chat", chatRouter)
}

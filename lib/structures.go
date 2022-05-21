package lib

type Full struct {
	User   User
	Chat   Chat
	Shared Shared
}

type Auth struct {
	Token string `json:"token"`
}

type User struct {
	Id         int    `json:"id"`
	Token      string `json:"token"`
	Seed       string `json:"seed"`
	Name       string `json:"name"`
	Login      string `json:"login"`
	Password   string `json:"password"`
	Email      string `json:"email"`
	Age        uint8  `json:"age"`
	Social     string `json:"social"`
	Location   string `json:"location"`
	Hobby      string `json:"hobby"`
	Career     string `json:"career"`
	Education  string `json:"education"`
	Cigaretes  string `json:"cigaretes"`
	Alcohol    string `json:"alcohol"`
	Musics     string `json:"musics"`
	Films      string `json:"films"`
	Videogames string `json:"videogames"`
	Serials    string `json:"serials"`
	Books      string `json:"books"`
}

type Chat struct {
	Id1      int
	Id2      int
	Location string
}

type Shared struct {
	Owner_id  int
	Shared_id int
	Field     string
}

type Session struct {
	id    int
	token string
}

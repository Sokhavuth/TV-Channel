<!--views/login.tpl-->

<link rel="stylesheet" href="/static/styles/frontend/login.css" />

<section class="Login">
    <div class="outer region">
        <div class="title">{{ data["pageTitle"] }}</div>
        <form action="/login" method="post">
            <a>Email:</a><input type="email" name="email" 
            value="guest@khmerweb.app" />
            <a>Password:</a><input type="password" name="password" 
            value="46d5eb4e5a4e4cf1a625bdcd6e7cdd56" />
            <a></a><input type="submit" value="Submit" />
            <a></a><div class="message">{{ data["message"] }}</div>
        </form>
    </div>
</section>
<!--views/login.tpl-->

<link rel="stylesheet" href="/static/styles/frontend/login.css" />

<section class="Login">
    <div class="outer region">
        <div class="title">{{ data["pageTitle"] }}</div>
        <form action="/login" method="post">
            <a>Email:</a><input type="email" name="email" />
            <a>Password:</a><input type="password" name="password" />
            <a></a><input type="submit" value="Submit" />
            <a></a><div class="message">{{ data["message"] }}</div>
        </form>
    </div>
</section>
<!--views/backend/index.tpl-->

<link rel="stylesheet" href="/static/styles/backend/index.css" />

<section class="Index">
    <header>
        <div class="inner region">
            <div class="page-title">{{ data["pageTitle"] }}</div>
            <form action="/admin/search" method="post">
                <select name="searchtype">
                    <option>Post</option>
                    <option>Category</option>
                    <option>User</option>
                </select>
                <input type="text" name="q" required />
                <input type="submit" value="Search" />
            </form>
            <div class="logout">
                {{ data["username"]}} | <a href="/">Home</a> | <a href="/login/logout">Logout</a>
            </div>
        </div>
    </header>

    <div class="main region">
        <div class="sidebar">
            <div class="inner">
                <a href="/admin/post"><img src="/static/images/movie.png" /></a>
                <a href="/admin/post">Post</a>

                <a href="/admin/category"><img src="/static/images/category.png" /></a>
                <a href="/admin/category">Category</a>

                <a href="/admin/upload"><img src="/static/images/upload.png" /></a>
                <a href="/admin/upload">Upload</a>

                <a href="/admin/user"><img src="/static/images/users.png" /></a>
                <a href="/admin/user">User</a>

                <a href="/admin/setting"><img src="/static/images/setting.png" /></a>
                <a href="/admin/setting">Settings</a>
            </div>
        </div>
        <div class="content">Content</div>
    </div>

    <div class="footer region">
        <div class="info">Total number of items:</div>
        <ul></ul>
        <div class="pagination">
            <img onclick="paginate(`{{ data['route'] }}`)" src="/static/images/load.png" />
        </div>

        <div class="credit">
            <a href="https://khmerweb.vercel.app/">&copy Khmer Web 2022</a>
        </div>
    </div>
</section>
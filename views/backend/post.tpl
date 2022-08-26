<!--views/backend/post.tpl-->

<link rel="stylesheet" href="/static/styles/backend/post.css" />
<script src="/static/scripts/ckeditor/ckeditor.js"></script>
<script src="/static/scripts/video.js"></script>
<script src="/static/scripts/addCategory.js"></script>

<section class="Post">
    <form action="/admin/post" method="post" name="form" onSubmit="submitForm(event)">
        <input type="text" name="tilte" required placeholder="Post title" />
        <textarea name="content" id="editor"></textarea>
        <input type="text" name="categories" required placeholder="Categories" />
        <div class="wrapper">
            <select id="category" onChange="getCategory()">
                <option>Slect a category</option>
                <option>News</option>
                <option>Entertainment</option>
                <option>Movie</option>
            </select>
            <input type="text" name="thumb" required placeholder="Thumbnail" />
            <input type="datetime-local" name="datetime" required />
            <input type="submit" value="Publish" />
        </div>
        <input name='videos' value='' type='hidden' />
    </form>
    <div class="video-wrapper" >
        <select name="type">
          <option>YouTube</option>
          <option>YouTubePL</option>
          <option>Facebook</option>
          <option>OK</option>
        </select>
        <input type="text" name="videoid" required placeholder="Video id" />
        <select name="status">
          <option>End</option>
          <option>Continue</option>
          <option>~ End</option>
        </select>
        <input onclick="genJson()" type="submit" value="Insert video" />
    </div>

    <div class='viddata'>
        <div></div>
    </div>

</section>
<script src="/static/scripts/ckeditor/config.js"></script>


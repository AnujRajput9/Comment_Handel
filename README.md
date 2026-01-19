# Comment-Handel-Django-Project-

## 🚀 Features

* 🔐 User Registration & Login
* ✍️ Create comments with image upload
* 📄 View all comments in a professional layout
* ✏️ Edit own comments
* 🗑️ Delete own comments
* 🎨 Modern dark UI (Bootstrap 5 + custom CSS)
* 📱 Fully responsive design

---

## 🛠️ Tech Stack

| Technology      | Usage               |
| --------------- | ------------------- |
| **Python**      | Backend language    |
| **Django**      | Web framework       |
| **SQLite**      | Database            |
| **Bootstrap 5** | Frontend UI         |
| **HTML & CSS**  | Templates & styling |

---

## 📂 Project Structure

```
django-comment-management/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── comments/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── comment_list.html
│   ├── comment_form.html
│   ├── login.html
│   └── register.html
│
├── media/
│   └── comments/
│
└── static/
```

---

## 🧠 CRUD Operations Explained (Core of Project)

### ➕ Create (Insert Data)

Users can create comments using a **Django ModelForm**.

```python
def create_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect("comment_list")
    else:
        form = CommentForm()
    return render(request, "comment_form.html", {"form": form})
```

✔ Validates input
✔ Saves data to database using Django ORM

---

### 📖 Read (Fetch Data)

All comments are fetched and displayed dynamically.

```python
def comment_list(request):
    comments = Comment.objects.all().order_by("-created_at")
    return render(request, "comment_list.html", {"comments": comments})
```

✔ Uses ORM instead of raw SQL
✔ Passes data securely to templates

---

### ✏️ Update (Edit Data)

Only the **comment owner** can update their comment.

```python
def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id, user=request.user)
    form = CommentForm(request.POST or None, request.FILES or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect("comment_list")
    return render(request, "comment_form.html", {"form": form})
```

✔ Uses `instance` to update existing record
✔ Prevents unauthorized access

---

### 🗑️ Delete (Remove Data)

Users can delete their own comments.

```python
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id, user=request.user)
    comment.delete()
    return redirect("comment_list")
```

✔ Secure deletion
✔ Ownership validation

---

## 🗄️ Database Model

```python
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to="comments/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

✔ Clean database schema
✔ Django ORM handles SQL internally

---

## 🎨 UI & Template System

* Uses **template inheritance** (`layout.html`)
* Consistent UI across all pages
* Modern glassmorphism design
* Responsive layout

```django
{% extends "layout.html" %}
{% block content %}
{% endblock %}
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/django-comment-management-system.git
cd django-comment-management-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

### 6️⃣ Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🔐 Security Features

* CSRF protection enabled
* Authentication required for CRUD actions
* Authorization checks for edit/delete
* Secure media uploads

---

## 📸 Screenshots (Optional)

*Add screenshots here to make the repository more attractive.*

---

## 🚧 Future Improvements

* AJAX-based CRUD (no page reload)
* Nested comments & replies
* Like / reaction system
* Pagination
* REST API using Django REST Framework

---

## 👨‍💻 Author

**Anuj Rajput**
Django Developer | Backend Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it really helps!

---

### 🏁 Final Note

This README follows **GitHub best practices**, is **interview-friendly**, and clearly explains **CRUD operations in Django**.



Just tell me 😎

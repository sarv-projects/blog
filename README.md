# Full-Stack Blogging Platform

A production-grade blogging platform built with **Django**, **PostgreSQL**, **Bootstrap**, and **Jinja2 Templates**.  
It features user authentication, post CRUD operations, threaded comments, and a responsive, user-friendly interface.

---

## 🚀 Features

- **User Authentication**: Register, Login, Logout with Django’s secure auth system.
- **CRUD for Posts**: Create, read, update, and delete blog posts.
- **Threaded Comments**: Engage with post-specific discussions.
- **Post Status Control**: Publish or save posts as drafts.
- **Slugified URLs**: SEO-friendly routes like `/post/my-blog-title/`.
- **User Dashboard**: Manage only your own posts.
- **Search & Filter**: Find posts by title or category.
- **Pagination**: Smooth navigation for large blogs.
- **Responsive Design**: Built with Bootstrap for mobile-first UI.

---

## 🛠️ Tech Stack

| Layer       | Technology                                    |
|-------------|-----------------------------------------------|
| Backend     | Django, Django ORM                            |
| Database    | PostgreSQL                                    |
| Frontend    | Django Templates (Jinja2), Bootstrap          |
| Auth        | Django's built-in authentication              |
| Extras      | crispy-forms, Django messages, pagination     |

---

## 📦 Installation

**Prerequisites**:  
- Python 3.x  
- PostgreSQL  
- (Optional) WSL for Linux environment on Windows

**Steps**:

```bash
Clone the repository
git clone https://github.com/sarv-projects/blog.git
cd blogcraft

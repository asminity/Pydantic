from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):
    title: str
    author: str
    price: int
    no_of_pages: int
    genre: Optional[List[str]] = None
    
class Comment(BaseModel):
    id: int
    content: str
    timestamp: datetime
    likes: int
    dislikes: int
    replies : Optional[List["Comment"]] = None
    

class User(BaseModel):
    Name: str
    Age: int
    Email: Optional[str] = None
    BooksRead: Optional[List[Book]] = None
    Comments: Comment
    
Book1 = Book(
        title="Alice in Wonderland",
        author="Lewis Carroll",
        price=100,
        no_of_pages=200,
        genre=["Fantasy", "Adventure"]
    )

Book2 = Book(
        title="The Alchemist",
        author="Paulo Coelho",
        price=200,
        no_of_pages=300,
        genre=["Fiction", "Adventure"]
    )

Book3 = Book(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        price=300,
        no_of_pages=400,
        genre=["Fiction", "Drama"]
    )

Comment1 = Comment(
    id=1,
    content="Hello",
    timestamp=datetime.now(),
    likes=10,
    dislikes=2
)


User1 = User(
    Name="Asmit Yadav",
    Age=20,
    BooksRead=[Book1, Book2, Book3],
    Comments=Comment1
)

print(User1)
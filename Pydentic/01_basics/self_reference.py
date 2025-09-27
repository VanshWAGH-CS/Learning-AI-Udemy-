from typing import List, Optional
from pydantic import BaseModel, Field

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = Field(default_factory=list)

# Use this in Pydantic v1
Comment.update_forward_refs()

comment = Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2"),
    ]
)

print(comment)

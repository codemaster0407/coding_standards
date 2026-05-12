from pydantic import BaseModel, Field
from typing import List, Literal

class Section(BaseModel):
    header_type: Literal["h1", "h2", "h3", "h4", "h5", "h6"] = Field(
        description="The type of header (e.g., 'h1', 'h2', 'h3')."
    )
    header_text: str = Field(
        description="The text of the header."
    )
    text: str = Field(
        description="The text content that falls under this header."
    )

class DocumentContent(BaseModel):
    sections: List[Section] = Field(
        description="A list of extracted sections from the document."
    )


class TechStackData(BaseModel):
    techstack : List[str] = Field(
        description="A list of tech stacks used in the problem statement."
    ) 
    tavily_search_prompts : List[str] = Field(
        description = 'Tavily prompts for web search for respective tech stack for coding standards'
    )
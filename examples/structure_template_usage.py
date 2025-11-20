"""Examples demonstrating TOON structure template generation for LLM prompts."""
from toon import generate_structure

try:
    from pydantic import BaseModel, Field
    from toon import generate_structure_from_pydantic
    PYDANTIC_AVAILABLE = True
except ImportError:
    PYDANTIC_AVAILABLE = False
    print("Note: Pydantic examples will be skipped (pydantic not installed)")


def example_simple_response_structure():
    """Example: Generate a simple response structure template."""
    print("=== Simple Response Structure ===")
    print("Use case: Telling an LLM what format to return data in\n")
    
    schema = {
        "name": "name of the person",
        "age": "age of the person",
        "occupation": "job description of the person"
    }
    
    structure = generate_structure(schema)
    
    print("Schema definition:")
    print(schema)
    print("\nGenerated TOON structure template:")
    print(structure)
    print("\nHow to use in LLM prompt:")
    print('  "Please extract person information and return it in this format:')
    print(f'   {structure}"')
    print()


def example_nested_response_structure():
    """Example: Generate a nested response structure."""
    print("=== Nested Response Structure ===")
    print("Use case: Complex data with nested objects\n")
    
    schema = {
        "company": {
            "name": "company name",
            "location": {
                "city": "city name",
                "country": "country name"
            }
        },
        "employee_count": "number of employees"
    }
    
    structure = generate_structure(schema)
    
    print("Generated structure template:")
    print(structure)
    print()


def example_array_response_structure():
    """Example: Generate structure for array responses."""
    print("=== Array Response Structure ===")
    print("Use case: Extracting multiple items in tabular format\n")
    
    schema = {
        "products": [{
            "id": "product identifier",
            "name": "product name",
            "price": "product price in USD",
            "in_stock": "availability status"
        }]
    }
    
    structure = generate_structure(schema)
    
    print("Generated structure template:")
    print(structure)
    print("\nHow to use in LLM prompt:")
    print('  "Extract all products from the page and return them in this format:')
    print(f'   {structure}"')
    print()


def example_list_response_structure():
    """Example: Generate structure for list of items."""
    print("=== Root-Level Array Structure ===")
    print("Use case: Returning an array of similar objects\n")
    
    schema = [{
        "title": "article title",
        "author": "article author",
        "date": "publication date",
        "summary": "brief summary"
    }]
    
    structure = generate_structure(schema)
    
    print("Generated structure template:")
    print(structure)
    print()


def example_mixed_response_structure():
    """Example: Complex structure with mixed types."""
    print("=== Mixed Response Structure ===")
    print("Use case: Complex extraction with various data types\n")
    
    schema = {
        "page_title": "title of the page",
        "metadata": {
            "published": "publication date",
            "author": "author name"
        },
        "tags": ["tag name"],
        "sections": [{
            "heading": "section heading",
            "word_count": "number of words"
        }]
    }
    
    structure = generate_structure(schema)
    
    print("Generated structure template:")
    print(structure)
    print()


def example_delimiter_options():
    """Example: Using different delimiters."""
    print("=== Custom Delimiters ===")
    print("Use case: When data might contain commas\n")
    
    schema = [{
        "address": "full address (may contain commas)",
        "city": "city name",
        "zipcode": "zip code"
    }]
    
    print("With pipe delimiter (recommended for addresses):")
    structure_pipe = generate_structure(schema, {"delimiter": "|"})
    print(structure_pipe)
    
    print("\nWith tab delimiter (good for spreadsheet-like data):")
    structure_tab = generate_structure(schema, {"delimiter": "\t"})
    print(structure_tab)
    print()


# Pydantic-specific examples
if PYDANTIC_AVAILABLE:
    
    class Person(BaseModel):
        """Person information model."""
        id: int = Field(description="unique identifier")
        name: str = Field(description="full name")
        email: str = Field(description="email address")
        age: int = Field(description="age in years")
        occupation: str = Field(description="job title or profession")
    
    
    class Article(BaseModel):
        """Article model."""
        title: str = Field(description="article title")
        author: str = Field(description="author name")
        published_date: str = Field(description="publication date in YYYY-MM-DD format")
        tags: list[str] = Field(description="article tags")
        word_count: int = Field(description="number of words")
    
    
    def example_pydantic_simple_model():
        """Example: Generate structure from Pydantic model."""
        print("=== Pydantic Model Structure ===")
        print("Use case: Generate structure from existing data models\n")
        
        structure = generate_structure_from_pydantic(Person)
        
        print(f"Model: {Person.__name__}")
        print("\nGenerated structure template:")
        print(structure)
        print()
    
    
    def example_pydantic_for_llm_prompt():
        """Example: Using Pydantic structure in LLM prompts."""
        print("=== Complete LLM Prompt Example ===")
        print("Use case: Full example of using structure in a prompt\n")
        
        structure = generate_structure_from_pydantic(Article)
        
        prompt = f"""Extract the article information from the following text and return it in TOON format.

Expected structure:
{structure}

Text to extract from:
[Article content would go here...]

Please return only the TOON formatted data."""
        
        print("Complete prompt:")
        print("-" * 60)
        print(prompt)
        print("-" * 60)
        print()
    
    
    def example_pydantic_array_structure():
        """Example: Array of Pydantic models."""
        print("=== Pydantic Array Structure ===")
        print("Use case: Extracting multiple items of the same type\n")
        
        # To generate array structure, we pass a list schema
        schema = [{
            "title": "article title",
            "author": "author name",
            "published_date": "publication date",
            "word_count": "word count"
        }]
        
        structure = generate_structure(schema)
        
        print("Generated structure for array of articles:")
        print(structure)
        print()


def example_real_world_use_case():
    """Example: Real-world use case for web scraping."""
    print("=== Real-World Use Case: Product Scraping ===")
    print("Use case: Instructing an LLM to extract product data\n")
    
    schema = {
        "products": [{
            "name": "product name",
            "sku": "product SKU or ID",
            "price": "price in USD",
            "rating": "average rating (1-5)",
            "reviews_count": "number of reviews",
            "availability": "in stock or out of stock"
        }]
    }
    
    structure = generate_structure(schema)
    
    prompt = f"""You are a web scraping assistant. Extract all product information from the HTML and return it in TOON format.

Return the data in this exact structure:
{structure}

Important notes:
- Extract ALL products from the page
- Price should be numeric (remove currency symbols)
- Rating should be a number between 1 and 5
- If a field is missing, use null

HTML content:
[HTML content would go here...]"""
    
    print("Complete prompt for web scraping:")
    print("=" * 60)
    print(prompt)
    print("=" * 60)
    print()


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("  TOON STRUCTURE TEMPLATE EXAMPLES")
    print("  Generate response structures for LLM prompts")
    print("="*60 + "\n")
    
    example_simple_response_structure()
    example_nested_response_structure()
    example_array_response_structure()
    example_list_response_structure()
    example_mixed_response_structure()
    example_delimiter_options()
    
    if PYDANTIC_AVAILABLE:
        example_pydantic_simple_model()
        example_pydantic_for_llm_prompt()
        example_pydantic_array_structure()
    
    example_real_world_use_case()
    
    print("="*60)
    print("  Summary")
    print("="*60)
    print("✨ Use generate_structure() to create response templates")
    print("✨ Perfect for LLM prompts - no need to provide examples")
    print("✨ Supports nested objects, arrays, and custom delimiters")
    print("✨ Works with Pydantic models for type-safe schemas")
    print("✨ Reduces token usage while maintaining clarity")
    print()


if __name__ == "__main__":
    main()

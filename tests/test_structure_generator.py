"""Tests for TOON structure generator."""
import pytest
from toon import generate_structure


def test_generate_simple_structure():
    """Test generating a simple object structure."""
    schema = {
        "name": "name of the person",
        "age": "age of the person",
        "occupation": "job description of the person"
    }
    
    result = generate_structure(schema)
    
    assert "name: <name of the person>" in result
    assert "age: <age of the person>" in result
    assert "occupation: <job description of the person>" in result


def test_generate_nested_structure():
    """Test generating a nested object structure."""
    schema = {
        "user": {
            "id": "user identifier",
            "profile": {
                "name": "user name",
                "email": "user email"
            }
        }
    }
    
    result = generate_structure(schema)
    
    assert "user:" in result
    assert "id: <user identifier>" in result
    assert "profile:" in result
    assert "name: <user name>" in result
    assert "email: <user email>" in result


def test_generate_array_structure():
    """Test generating a structure with arrays."""
    schema = {
        "users": [{
            "id": "user id",
            "name": "user name",
            "email": "user email"
        }]
    }
    
    result = generate_structure(schema)
    
    assert "users[N]{id,name,email}:" in result
    assert "<user id>" in result
    assert "<user name>" in result
    assert "<user email>" in result
    assert "..." in result


def test_generate_root_array_structure():
    """Test generating a structure for root-level array."""
    schema = [{
        "id": "product id",
        "name": "product name",
        "price": "product price"
    }]
    
    result = generate_structure(schema)
    
    assert "[N]{id,name,price}:" in result
    assert "<product id>" in result
    assert "<product name>" in result
    assert "<product price>" in result
    assert "..." in result


def test_generate_empty_structures():
    """Test generating empty structures."""
    # Empty object
    result = generate_structure({})
    assert result == "{}"
    
    # Object with empty nested object
    schema = {"data": {}}
    result = generate_structure(schema)
    assert "data: {}" in result
    
    # Object with empty array
    schema = {"items": []}
    result = generate_structure(schema)
    assert "items: []" in result


def test_generate_with_tab_delimiter():
    """Test generating structure with tab delimiter."""
    schema = [{
        "id": "user id",
        "name": "user name"
    }]
    
    result = generate_structure(schema, {"delimiter": "\t"})
    
    # Should show tab indicator in header
    assert "[N\t]{id,name}:" in result
    # Should use tab as delimiter in sample row
    assert "<user id>\t<user name>" in result


def test_generate_with_pipe_delimiter():
    """Test generating structure with pipe delimiter."""
    schema = [{
        "id": "user id",
        "name": "user name"
    }]
    
    result = generate_structure(schema, {"delimiter": "|"})
    
    # Should show pipe indicator in header
    assert "[N|]{id,name}:" in result
    # Should use pipe as delimiter in sample row
    assert "<user id>|<user name>" in result


def test_generate_with_custom_indent():
    """Test generating structure with custom indentation."""
    schema = {
        "user": {
            "name": "user name"
        }
    }
    
    result = generate_structure(schema, {"indent": 4})
    
    lines = result.split("\n")
    # First level should have no indent
    assert lines[0] == "user:"
    # Second level should have 4 spaces
    assert lines[1].startswith("    ")


def test_generate_mixed_structure():
    """Test generating a complex mixed structure."""
    schema = {
        "title": "document title",
        "metadata": {
            "author": "author name",
            "created": "creation date"
        },
        "tags": ["tag name"],
        "sections": [{
            "heading": "section heading",
            "content": "section content"
        }]
    }
    
    result = generate_structure(schema)
    
    assert "title: <document title>" in result
    assert "metadata:" in result
    assert "author: <author name>" in result
    assert "created: <creation date>" in result
    assert "tags: [<tag name>,...]" in result
    assert "sections[N]{heading,content}:" in result


def test_generate_primitive_array():
    """Test generating structure for primitive arrays."""
    schema = {
        "numbers": ["numeric value"],
        "names": ["name string"]
    }
    
    result = generate_structure(schema)
    
    assert "numbers: [<numeric value>,...]" in result
    assert "names: [<name string>,...]" in result


# Pydantic-specific tests
try:
    from pydantic import BaseModel, Field
    from toon import generate_structure_from_pydantic
    
    class SimpleUser(BaseModel):
        """Simple user model."""
        id: int = Field(description="user identifier")
        name: str = Field(description="user full name")
        email: str = Field(description="user email address")
    
    
    class NestedUser(BaseModel):
        """User model with nested profile."""
        id: int = Field(description="user identifier")
        name: str = Field(description="user name")
        
        class Profile(BaseModel):
            bio: str = Field(description="user biography")
            location: str = Field(description="user location")
        
        profile: Profile = Field(description="user profile")
    
    
    def test_generate_from_pydantic_simple():
        """Test generating structure from simple Pydantic model."""
        result = generate_structure_from_pydantic(SimpleUser)
        
        assert "id: <user identifier>" in result
        assert "name: <user full name>" in result
        assert "email: <user email address>" in result
    
    
    def test_generate_from_pydantic_without_descriptions():
        """Test generating structure from Pydantic model without descriptions."""
        class UserNoDesc(BaseModel):
            id: int
            name: str
            active: bool
        
        result = generate_structure_from_pydantic(UserNoDesc, include_descriptions=False)
        
        # Should use type names as descriptions
        assert "id: <integer>" in result or "id: <int>" in result
        assert "name: <string>" in result or "name: <str>" in result
        assert "active: <boolean>" in result or "active: <bool>" in result
    
    
    def test_generate_from_pydantic_invalid_input():
        """Test error handling for invalid Pydantic input."""
        class NotAModel:
            pass
        
        with pytest.raises(TypeError):
            generate_structure_from_pydantic(NotAModel)
    
    
    def test_generate_from_pydantic_with_options():
        """Test generating structure from Pydantic with custom options."""
        result = generate_structure_from_pydantic(
            SimpleUser,
            options={"indent": 4}
        )
        
        # Check that custom indentation is used (though this simple model has no nesting)
        assert "id: <user identifier>" in result

except ImportError:
    # Pydantic tests will be skipped if pydantic is not installed
    pass


def test_generate_structure_ordering():
    """Test that field ordering is preserved."""
    schema = {
        "field_a": "first field",
        "field_b": "second field",
        "field_c": "third field"
    }
    
    result = generate_structure(schema)
    lines = result.split("\n")
    
    # Find positions of each field
    pos_a = next(i for i, line in enumerate(lines) if "field_a" in line)
    pos_b = next(i for i, line in enumerate(lines) if "field_b" in line)
    pos_c = next(i for i, line in enumerate(lines) if "field_c" in line)
    
    # Check ordering
    assert pos_a < pos_b < pos_c


def test_generate_structure_realistic_example():
    """Test with a realistic example similar to the issue description."""
    schema = {
        "name": "name of the person",
        "age": "age of the person",
        "occupation": "job description of the person"
    }
    
    result = generate_structure(schema)
    
    # This should produce a clean template for LLM prompts
    expected_lines = [
        "name: <name of the person>",
        "age: <age of the person>",
        "occupation: <job description of the person>"
    ]
    
    for line in expected_lines:
        assert line in result
    
    # Should not contain actual data values
    assert "Alice" not in result
    assert "30" not in result
    assert "Engineer" not in result

"""Tests for nested arrays and objects within tabular arrays (Issue #6)."""
import pytest
from toon import encode, decode


def test_array_of_objects_with_nested_arrays():
    """Test encoding/decoding arrays of objects that contain nested arrays."""
    original = {
        "categorization": [
            {
                "id": "01.04.04.01.",
                "label": "Aspetti generali",
                "hierarchy": [
                    "Prodotti",
                    "Organizzazione altro e Sito Internet",
                    "Aspetti generali",
                    "Aspetti generali"
                ],
                "score": 900,
                "winner": True,
                "namespace": "$namespace",
                "frequency": 0,
                "offset": [
                    {"start": 511, "end": 520},
                    {"start": 524, "end": 527},
                    {"start": 528, "end": 543}
                ]
            }
        ]
    }
    
    # Encode
    toon = encode(original)
    print("Encoded TOON:")
    print(toon)
    
    # Decode
    result = decode(toon)
    print("\nDecoded result:")
    print(result)
    
    # Verify all fields are preserved
    assert result == original, "Decoded data should match original"
    assert "hierarchy" in result["categorization"][0], "hierarchy field should be preserved"
    assert "offset" in result["categorization"][0], "offset field should be preserved"
    assert len(result["categorization"][0]["hierarchy"]) == 4, "hierarchy array should have 4 items"
    assert len(result["categorization"][0]["offset"]) == 3, "offset array should have 3 items"


def test_array_of_objects_with_nested_objects():
    """Test encoding/decoding arrays where objects contain nested objects."""
    original = {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "address": {
                    "street": "123 Main St",
                    "city": "NYC"
                }
            },
            {
                "id": 2,
                "name": "Bob",
                "address": {
                    "street": "456 Oak Ave",
                    "city": "LA"
                }
            }
        ]
    }
    
    # Encode
    toon = encode(original)
    print("Encoded TOON:")
    print(toon)
    
    # Decode
    result = decode(toon)
    
    # Verify all fields are preserved
    assert result == original
    assert "address" in result["users"][0]
    assert result["users"][0]["address"]["city"] == "NYC"


def test_array_of_objects_mixed_primitive_and_nested():
    """Test arrays with both primitive and nested fields."""
    original = {
        "items": [
            {
                "id": 1,
                "name": "Item A",
                "tags": ["tag1", "tag2"],
                "price": 10.5
            },
            {
                "id": 2,
                "name": "Item B",
                "tags": ["tag3"],
                "price": 20.0
            }
        ]
    }
    
    # Encode
    toon = encode(original)
    
    # Decode
    result = decode(toon)
    
    # Verify all fields are preserved
    assert result == original
    assert "tags" in result["items"][0]
    assert len(result["items"][0]["tags"]) == 2
    assert len(result["items"][1]["tags"]) == 1


def test_roundtrip_complex_nested_structure():
    """Test full roundtrip of complex nested structure."""
    original = {
        "data": [
            {
                "id": "A1",
                "value": 100,
                "metadata": {
                    "created": "2024-01-01",
                    "tags": ["important", "urgent"]
                },
                "scores": [95, 87, 92]
            },
            {
                "id": "A2", 
                "value": 200,
                "metadata": {
                    "created": "2024-01-02",
                    "tags": ["normal"]
                },
                "scores": [88, 90]
            }
        ]
    }
    
    # First roundtrip
    toon1 = encode(original)
    result1 = decode(toon1)
    assert result1 == original
    
    # Second roundtrip
    toon2 = encode(result1)
    result2 = decode(toon2)
    assert result2 == original
    assert toon1 == toon2


def test_array_of_objects_some_with_nested_some_without():
    """Test arrays where only some objects have nested fields."""
    original = {
        "records": [
            {
                "id": 1,
                "name": "Record A",
                "extra": {"note": "Has nested"}
            },
            {
                "id": 2,
                "name": "Record B"
                # No 'extra' field
            }
        ]
    }
    
    # Encode
    toon = encode(original)
    
    # Decode
    result = decode(toon)
    
    # Verify structure is preserved
    assert "extra" in result["records"][0]
    assert "extra" not in result["records"][1]
    assert result["records"][0]["extra"]["note"] == "Has nested"


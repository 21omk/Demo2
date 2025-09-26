import pytest
import sys
import os

# Add the parent directory to the path so we can import our app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import calculate_average, process_data

class TestDemoFailures:
    """Test class with intentional failures for demo purposes"""
    
    def test_passing_test(self):
        """This test should pass"""
        assert True
        assert 1 + 1 == 2
        
    def test_assertion_failure(self):
        """This test will fail with assertion error"""
        assert False, "This test is designed to fail for demo purposes"
        
    def test_math_calculation_error(self):
        """Test that demonstrates a math error"""
        result = 2 + 2
        assert result == 5, f"Expected 5 but got {result}"
        
    def test_string_comparison_failure(self):
        """Test that fails on string comparison"""
        actual = "hello world"
        expected = "goodbye world"
        assert actual == expected, f"Expected '{expected}' but got '{actual}'"
        
    def test_list_length_error(self):
        """Test that fails on list length check"""
        my_list = [1, 2, 3, 4]
        expected_length = 10
        assert len(my_list) == expected_length, f"Expected list length {expected_length} but got {len(my_list)}"
        
    def test_type_error_failure(self):
        """Test that demonstrates a type error"""
        with pytest.raises(TypeError):
            result = "string" + 123  # This should raise TypeError
            # But we're not actually testing the right thing, so this will fail
            assert result == "string123"
            
    def test_division_by_zero(self):
        """Test that should catch division by zero but doesn't"""
        result = calculate_average([])  # This will cause division by zero
        assert result == 0  # This assertion will never be reached
        
    def test_function_return_type(self):
        """Test that expects wrong return type"""
        result = process_data("hello")
        assert isinstance(result, int), f"Expected int but got {type(result)}"
        
    def test_none_comparison(self):
        """Test that fails on None comparison"""
        value = None
        assert value is not None, "Value should not be None"
        assert len(value) > 0, "Value should have length greater than 0"
        
    def test_dictionary_key_error(self):
        """Test that causes KeyError"""
        test_dict = {"key1": "value1", "key2": "value2"}
        # This will raise KeyError but we're not handling it properly
        missing_value = test_dict["nonexistent_key"]
        assert missing_value == "expected_value"
        
    def test_index_error(self):
        """Test that causes IndexError"""
        test_list = [1, 2, 3]
        # This will raise IndexError
        value = test_list[10]
        assert value == 1
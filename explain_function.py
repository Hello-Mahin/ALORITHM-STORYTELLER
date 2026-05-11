import re
import ast

def explain_code(user_code, language):
    """
    Analyzes and explains code with step-by-step logic, complexity analysis, and special patterns.
    
    Args:
        user_code (str): The code to be explained
        language (str): Programming language (C, Java, Python)
    
    Returns:
        str: A detailed explanation including logic, complexity, and special patterns
    """
    
    explanation = f"## Code Explanation - {language}\n\n"
    
    # 1. STEP-BY-STEP LOGIC
    explanation += "### Step-by-Step Logic:\n"
    
    if language == "Python":
        explanation += _analyze_python(user_code)
    elif language == "Java":
        explanation += _analyze_java(user_code)
    elif language == "C":
        explanation += _analyze_c(user_code)
    else:
        explanation += "Language not supported yet.\n"
    
    # 2. COMPLEXITY ANALYSIS
    explanation += "\n### Complexity Analysis:\n"
    explanation += _analyze_complexity(user_code, language)
    
    # 3. SPECIAL PATTERNS & OPERATIONS
    explanation += "\n### Special Patterns & Operations:\n"
    explanation += _identify_patterns(user_code, language)
    
    return explanation


def _analyze_python(code):
    """Analyze Python code and explain logic."""
    explanation = ""
    lines = code.strip().split('\n')
    
    try:
        tree = ast.parse(code)
        
        # Extract function definitions
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                explanation += f"**Function: `{node.name}`**\n"
                explanation += f"- Parameters: {', '.join([arg.arg for arg in node.args.args])}\n"
                explanation += "- Logic Flow:\n"
        
        # Line-by-line explanation
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped and not stripped.startswith('#'):
                explanation += f"  - Line {i}: {stripped}\n"
        
        return explanation if explanation else "- Code analysis complete.\n"
    
    except SyntaxError:
        return "- Unable to parse Python code. Please check syntax.\n"


def _analyze_java(code):
    """Analyze Java code and explain logic."""
    explanation = ""
    lines = code.strip().split('\n')
    
    # Extract class/method definitions
    class_match = re.search(r'(public|private)?\s*class\s+(\w+)', code)
    if class_match:
        explanation += f"**Class: `{class_match.group(2)}`**\n"
    
    method_matches = re.finditer(r'(public|private|protected)?\s*\w+\s+(\w+)\s*\([^)]*\)', code)
    for match in method_matches:
        explanation += f"- Method: `{match.group(2)}`\n"
    
    # Line-by-line explanation
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped and not stripped.startswith('//'):
            explanation += f"  - Line {i}: {stripped}\n"
    
    return explanation


def _analyze_c(code):
    """Analyze C code and explain logic."""
    explanation = ""
    lines = code.strip().split('\n')
    
    # Extract function definitions
    func_matches = re.finditer(r'(\w+)\s+(\w+)\s*\([^)]*\)\s*\{', code)
    for match in func_matches:
        explanation += f"**Function: `{match.group(2)}`** (returns {match.group(1)})\n"
    
    # Line-by-line explanation
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped and not stripped.startswith('//') and not stripped.startswith('/*'):
            explanation += f"  - Line {i}: {stripped}\n"
    
    return explanation


def _analyze_complexity(code, language):
    """Identify and explain Time and Space Complexity."""
    explanation = ""
    
    # Check for common patterns
    if re.search(r'for\s*\(.*for\s*\(', code):
        explanation += "- **Time Complexity: O(n²)** - Nested loops detected\n"
    elif re.search(r'for\s*\(', code):
        explanation += "- **Time Complexity: O(n)** - Single loop detected\n"
    elif re.search(r'while\s*\(', code):
        explanation += "- **Time Complexity: O(n)** - While loop detected\n"
    else:
        explanation += "- **Time Complexity: O(1)** - Constant time (no loops)\n"
    
    # Space Complexity
    if re.search(r'(list|array|vector|ArrayList|LinkedList)\s*[=\[]', code):
        explanation += "- **Space Complexity: O(n)** - Dynamic data structure (list/array) used\n"
    elif re.search(r'(dict|HashMap|map|Set|HashSet)\s*[=\[]', code):
        explanation += "- **Space Complexity: O(n)** - Hash-based data structure used\n"
    else:
        explanation += "- **Space Complexity: O(1)** - Constant space (local variables)\n"
    
    return explanation


def _identify_patterns(code, language):
    """Identify bitwise operations, recursion, and complex data structures."""
    explanation = ""
    patterns_found = []
    
    # Bitwise operations
    if re.search(r'[&|^~](?!=)', code):
        patterns_found.append("🔧 **Bitwise Operations**: AND (&), OR (|), XOR (^), or NOT (~) used")
    
    # Recursion
    if re.search(r'def\s+\w+\s*\([^)]*\):|\\b\w+\s*\(', code):
        if re.search(r'(\w+)\s*\(\s*\1\s*\(', code) or language == "Python" and re.search(r'return.*\(', code):
            patterns_found.append("🔄 **Recursion**: Function calls itself")
    
    # Data structures
    if re.search(r'(Stack|Queue|Deque|Heap|PriorityQueue)', code):
        patterns_found.append("📦 **Complex Data Structure**: Stack, Queue, Heap, or Priority Queue detected")
    
    if re.search(r'(dict|HashMap|map|TreeMap|Set|HashSet|TreeSet)', code):
        patterns_found.append("🗂️ **Hash-based Structure**: HashMap, HashSet, or similar detected")
    
    if re.search(r'(Graph|Tree|LinkedList|Node)', code):
        patterns_found.append("🌳 **Graph/Tree Structure**: Node-based structure detected")
    
    # Sorting
    if re.search(r'(sort|sorted|Collections\.sort)', code):
        patterns_found.append("📊 **Sorting Algorithm**: Sorting operation detected")
    
    if patterns_found:
        for pattern in patterns_found:
            explanation += f"- {pattern}\n"
    else:
        explanation += "- No special bitwise operations or complex patterns detected.\n"
    
    return explanation

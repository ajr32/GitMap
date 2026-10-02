import ast
import os


def extract_functions_from_project(project_root, output_file_path):
    """
    Scans the given project directory for all Python files, extracts
    the names of all functions and classes, and writes them to a reference file.
    """
    total_files = 0
    total_functions = 0
    
    with open(output_file_path, "w", encoding="utf-8") as out_file:
        out_file.write("===================================================\n")
        out_file.write("          PROJECT FUNCTION REFERENCE GUIDE         \n")
        out_file.write("===================================================\n\n")
        
        # Walk through the entire project directory
        for root, _, files in os.walk(project_root):
            # Skip common virtual environments, cache, and hidden folders
            skip_dirs = {'.git', '.venv', 'venv', '__pycache__', '.idea', 'build', 'dist'}
            if any(skip in root.split(os.sep) for skip in skip_dirs):
                continue
                
            for file in files:
                if file.endswith(".py"):
                    total_files += 1
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, project_root)
                    
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            node = ast.parse(f.read(), filename=file)
                        
                        # Find all top-level functions and class methods
                        file_functions = []
                        current_class = None
                        
                        for item in ast.walk(node):
                            if isinstance(item, ast.ClassDef):
                                current_class = item.name
                            elif isinstance(item, ast.FunctionDef):
                                # Capture the function or method signature
                                args = [arg.arg for arg in item.args.args]
                                sig = f"{item.name}({', '.join(args)})"
                                
                                if current_class and any(isinstance(p, ast.ClassDef) and p.name == current_class for p in ast.walk(node)):
                                    # Very basic fallback helper to check if inside a class context during linear walk
                                    # For a clean layout, we check top-level or structural context
                                    pass
                                
                                file_functions.append((item.name, sig, item.lineno))
                        
                        # Re-parse to accurately separate top-level functions vs class methods structurally
                        file_functions = []
                        for top_level_item in node.body:
                            if isinstance(top_level_item, ast.FunctionDef):
                                args = [arg.arg for arg in top_level_item.args.args]
                                file_functions.append(f"  [Line {top_level_item.lineno}] def {top_level_item.name}({', '.join(args)})")
                                total_functions += 1
                            elif isinstance(top_level_item, ast.ClassDef):
                                class_methods = []
                                for sub_item in top_level_item.body:
                                    if isinstance(sub_item, ast.FunctionDef):
                                        args = [arg.arg for arg in sub_item.args.args]
                                        class_methods.append(f"    [Line {sub_item.lineno}] def {sub_item.name}({', '.join(args)})")
                                        total_functions += 1
                                if class_methods:
                                    file_functions.append(f"  class {top_level_item.name}:")
                                    file_functions.extend(class_methods)
                        
                        if file_functions:
                            out_file.write(f"📁 File: {relative_path}\n")
                            out_file.write("-" * (8 + len(relative_path)) + "\n")
                            for func in file_functions:
                                out_file.write(f"{func}\n")
                            out_file.write("\n" + "="*40 + "\n\n")
                            
                    except Exception as e:
                        out_file.write(f"❌ Could not parse {relative_path}: {e}\n\n")
        
        out_file.write("===================================================\n")
        out_file.write(f" SUMMARY: Scanned {total_files} files | Found {total_functions} functions.\n")
        out_file.write("===================================================\n")

if __name__ == "__main__":
    # You can change '.' to your actual project path if running outside the project root
    project_directory = "." 
    output_filename = "project_function_reference_marked.txt"
    
    print(f"Scanning directory: {os.path.abspath(project_directory)}")
    extract_functions_from_project(project_directory, output_filename)
    print(f"Reference file created successfully: {output_filename}")

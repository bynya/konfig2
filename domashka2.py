import yaml
import re
import os

def read_apkbuild(apkbuild_path):
    with open(apkbuild_path, 'r') as file:
        content = file.read()
        
    makedepends_match = re.search(r'makedepends="([^"]+)"', content)
    if makedepends_match:
        dependencies = makedepends_match.group(1).split()
        return dependencies
    else:
        return []

def generate_plantuml(dependencies):
    plantuml_code = "@startuml\n"
    for dep in dependencies:
        plantuml_code += f"package --> {dep}\n"
    plantuml_code += "@enduml\n"
    return plantuml_code

def write_plantuml(output_file, plantuml_code):
    with open(output_file, 'w') as file:
        file.write(plantuml_code)

def main(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    
    if not config:
        raise ValueError("Файл конфигурации пуст или неправильно отформатирован.")
    
    dependencies = read_apkbuild(config['package_path'])
    
    plantuml_code = generate_plantuml(dependencies)
    
    plantuml_output_file = config['output_file']
    write_plantuml(plantuml_output_file, plantuml_code)
    
    print(plantuml_code)
    
    output_image_path = os.path.dirname(config['output_file'])
    print(f"Сохранение PlantUML кода в файл {plantuml_output_file}")

if __name__ == "__main__":
    main(r"C:\Users\dorzh\OneDrive\Desktop\config.yaml")

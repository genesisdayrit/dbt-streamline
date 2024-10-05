import os

def create_model_layers():
    # Get the model path from the user
    model_path = input("Enter the path to your dbt project's model directory: ").strip()
    
    # Define the model layers to be added
    model_layers = ['staging', 'intermediate', 'mart']

    # Create each model layer in the specified model path
    for layer in model_layers:
        layer_path = os.path.join(model_path, layer)
        try:
            os.makedirs(layer_path, exist_ok=True)
            print(f"Created model layer: {layer_path}")
        except Exception as e:
            print(f"Error creating model layer {layer_path}: {e}")

if __name__ == "__main__":
    create_model_layers()


from PIL import Image
import numpy as np

def swap_pixels(img_array):
    # Reverse pixel array (simple swap-like effect)
    return img_array[::-1]

def math_operation(img_array, operation='add', value=50):
    if operation == 'add':
        return np.clip(img_array + value, 0, 255)
    elif operation == 'subtract':
        return np.clip(img_array - value, 0, 255)
    elif operation == 'xor':
        return np.bitwise_xor(img_array, value)
    else:
        raise ValueError("Unsupported operation. Choose from 'add', 'subtract', or 'xor'.")

def encrypt_image(image_path, method='swap', operation='add', value=50, output_path='encrypted_image.png'):
    img = Image.open(image_path)
    img_array = np.array(img)

    if method == 'swap':
        encrypted_array = swap_pixels(img_array)
    elif method == 'math':
        encrypted_array = math_operation(img_array, operation, value)
    else:
        raise ValueError("Invalid method. Choose 'swap' or 'math'.")

    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(encrypted_path, method='swap', operation='add', value=50, output_path='decrypted_image.png'):
    # Decryption just reverses the operation
    img = Image.open(encrypted_path)
    img_array = np.array(img)

    if method == 'swap':
        decrypted_array = swap_pixels(img_array)
    elif method == 'math':
        inverse_op = 'subtract' if operation == 'add' else 'add' if operation == 'subtract' else 'xor'
        decrypted_array = math_operation(img_array, inverse_op, value)
    else:
        raise ValueError("Invalid method. Choose 'swap' or 'math'.")

    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

# Example usage
if __name__ == "__main__":
    import os

    input_image = input("Enter the path to your image: ").strip()
    if not os.path.exists(input_image):
        print("Image not found.")
        exit()

    mode = input("Choose mode: (E)ncrypt or (D)ecrypt: ").lower()
    method = input("Choose method: 'swap' or 'math': ").lower()

    if method == 'math':
        op = input("Choose operation ('add', 'subtract', 'xor'): ").lower()
        value = int(input("Enter value (e.g., 50): "))
    else:
        op, value = None, None

    if mode == 'e':
        encrypt_image(input_image, method, op, value)
    elif mode == 'd':
        decrypt_image(input_image, method, op, value)
    else:
        print("Invalid mode. Choose E or D.")

# punnycode_gen.py
import idna

# Visually similar Unicode variants for each letter
punny_variants = {
    'a': ['à', 'á', 'â', 'ã', 'ä', 'å', 'ɑ', 'а'],  # Cyrillic а
    'b': ['ƅ', 'ɓ', 'ʙ', 'Ь', 'в'],
    'c': ['ç', 'ć', 'č', 'с'],
    'd': ['ď', 'đ', 'ԁ'],
    'e': ['è', 'é', 'ê', 'ë', 'е'],
    'f': ['ƒ', 'ғ'],
    'g': ['ɡ', 'ġ', 'ğ', 'ǧ'],
    'h': ['ħ', 'н'],
    'i': ['ì', 'í', 'î', 'ï', 'ı', 'ӏ'],
    'j': ['ј', 'ʝ'],
    'k': ['κ', 'к'],
    'l': ['ĺ', 'ļ', 'ľ', 'ӏ', 'ⅼ'],
    'm': ['м', 'ṃ'],
    'n': ['ń', 'ņ', 'ň', 'ñ', 'п'],
    'o': ['ò', 'ó', 'ô', 'õ', 'ö', 'ø', 'о'],
    'p': ['р', 'ρ'],
    'q': ['զ'],
    'r': ['ř', 'ŗ', 'г'],
    's': ['ś', 'š', 'ș', 'ѕ'],
    't': ['ţ', 'ť', 'т'],
    'u': ['ù', 'ú', 'û', 'ü', 'ŭ', 'ū'],
    'v': ['ѵ'],
    'w': ['ŵ', 'ш'],
    'x': ['х', 'ҳ'],
    'y': ['ý', 'ÿ', 'у'],
    'z': ['ź', 'ž', 'ż', 'з'],
}

def generate_punnycodes(char):
    char = char.lower()
    if char not in punny_variants:
        print(f"No variants defined for '{char}'.")
        return

    print(f"\nPunnycode variants for '{char}':\n")
    for i, variant in enumerate(punny_variants[char], 1):
        try:
            punycode = idna.encode(variant).decode()
            print(f"{i}. {variant} -> {punycode}")
        except idna.IDNAError as e:
            print(f"{i}. {variant} -> Error: {e}")

if __name__ == "__main__":
    letter = input("Enter a letter (a-z): ").strip().lower()
    if len(letter) == 1 and letter.isalpha():
        generate_punnycodes(letter)
    else:
        print("Please enter a single alphabet letter (a-z).")

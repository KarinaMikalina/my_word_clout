print("🚀 Мой проект запустился!")
print("Это генератор облака слов")

def main():
    text = input("Введите текст для анализа: ")
    words = text.split()
    
    print(f"В вашем тексте {len(words)} слов")
    
    # Простой подсчет слов
    from collections import Counter
    word_count = Counter(words)
    
    print("\nСамые частые слова:")
    for word, count in word_count.most_common(5):
        print(f"{word}: {count} раз")

if __name__ == "__main__":
    main()
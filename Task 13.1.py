def reverse_words_count(sentence: str) -> tuple:
    words_list = sentence.split()
    rev_w_list = [word[::-1] for word in words_list]
    return (rev_w_list, len(rev_w_list))

print(reverse_words_count("hello world"))
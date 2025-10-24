from document_utils import clean_text, word_count, get_top_n_words

sample_text = "Hello, world! Hello students. Welcome to the world of information retrieval."

print("Cleaned Text:", clean_text(sample_text))
print("Word Count:", word_count(sample_text))
print("Top 5 Words:", get_top_n_words(sample_text, 5))

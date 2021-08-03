def is_palindrome_iterative(word):
    """ Identifica se uma palavra é uma palindromo """
    if not isinstance(word, str) or word == "":
        return False
    if word == word[::-1]:
        return True
    else:
        return False

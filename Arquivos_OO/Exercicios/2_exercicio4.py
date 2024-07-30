class StringUtil:
    
    @staticmethod
    def palindrome(palindrome):
        palindrome = palindrome.upper()
        return (palindrome == palindrome[::-1])
    
    @staticmethod
    def contarVogais(palavra):
        vogais = 'AEIOUaeiou'
        quantidade = 0
        for vogal in vogais:
            quantidade += palavra.count(vogal)
        return int(quantidade)



print(StringUtil.palindrome("Ana"))
print(StringUtil.contarVogais("Ana"))

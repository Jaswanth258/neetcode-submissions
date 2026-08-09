class Solution:

    def encode(self, strs: List[str]) -> str:
        parts=[]
        for word in strs:
            encoded_word = str(len(word)) + "#" + word
            parts.append(encoded_word)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i=j+1
            word=s[i:i+length]
            decoded.append(word)
            i=i+length

        return decoded


             
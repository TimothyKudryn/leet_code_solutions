class Solution(object):
    def sortSentence(self, s):
        count = 1
        for a in s:
            if a == ' ':
                count += 1
        list = [0] * count
        string = ''
        for i in s:
            if i == ' ':
                continue
            elif i.isalpha():
                string += i
            elif i.isnumeric():
                list[int(i) - 1] = string
                string = ''
        for j in range(len(list)):
            string += list[j]
            if j < len(list)-1:
                string += ' '
        return string
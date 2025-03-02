from collections import defaultdict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)
        
        return file_contents

def get_book_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)
        
        fc_split = file_contents.split()

        count = 0

        for x in fc_split:
            count += 1
        
        return count

def get_book_character_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)

        fc_lower = file_contents.lower()
        fc_split = fc_lower.split()

        char_dict = {}

        for x in fc_split:
            for c in x:
                if c in char_dict:
                    #print(c)
                    #print("need to increment value")
                    char_dict[c] += 1
                else:
                    char_dict[c] = 1
                    #print("added value")

        print(char_dict)

def get_book_character_count_sorted(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)

        fc_lower = file_contents.lower()
        fc_split = fc_lower.split()

        char_dict = {}

        for x in fc_split:
            for c in x:
                alpha_test = c.isalpha()
                if alpha_test == True:
                    if c in char_dict:
                        char_dict[c] += 1
                    else:
                        char_dict[c] = 1
                else:
                    #print("not an alpha character")
                    pass

        sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
        print(sorted_dict)

        d = defaultdict(list)

        for a, b in sorted_dict:
            print(a + ":", b)
            
        '''
        for k, v in sorted_dict.items():
            print(k, v)      
        '''

import sys


def wordSubsets(words1, words2):
    universal_map = {}
    for word in words2:
        temp_map = {}
        for char in word:
            temp_map[char] = temp_map.get(char, 0) + 1
        for char, count in temp_map.items():
            universal_map[char] = max(universal_map.get(char, 0), count)

        result = []
        for word in words1:
            word_map = {}
            for char in word:
                word_map[char] = word_map.get(char, 0) + 1

            is_subset = True
            for char, count in universal_map.items():
                if word_map.get(char, 0) < count:
                    is_subset = False
                    break

            if is_subset:
                result.append(word)

        return result


def main():
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["lo", "eo"]
    print(wordSubsets(words1, words2))


if __name__ == "__main__":
    sys.exit(main())

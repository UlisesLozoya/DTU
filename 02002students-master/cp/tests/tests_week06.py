from unitgrade import Report
import cp
from unitgrade import UTestCase


class Week06TextToNato(UTestCase):
    def test_TextToNato(self):
        from cp.ex06.nato import text_to_nato
        self.assertEqual(text_to_nato('Jason'), 'Juliet-Alpha-Sierra-Oscar-November')
        self.assertEqual(text_to_nato('Spongebob'), 'Sierra-Papa-Oscar-November-Golf-Echo-Bravo-Oscar-Bravo')
        self.assertEqual(text_to_nato('Oo'), 'Oscar-Oscar')
        self.assertEqual(text_to_nato('Bubble'), 'Bravo-Uniform-Bravo-Bravo-Lima-Echo')
        
class Week06LetterHistogram(UTestCase):
    def test_LetterHistogram(self):
        from cp.ex06.letter import letter_histogram
        self.assertEqual(letter_histogram('The roof is on fire.'),{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 2, 'f': 2, 'g': 0, 'h': 1, 'i': 2, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 3, 'p': 0, 'q': 0, 'r': 2, 's': 1, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} )
        self.assertEqual(letter_histogram('abcdefghijklmnoprstuvwxyz'),{'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 0, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1})
        self.assertEqual(letter_histogram('The name is Bond. James Bond'),{'a': 2, 'b': 2, 'c': 0, 'd': 2, 'e': 3, 'f': 0, 'g': 0, 'h': 1, 'i': 1, 'j': 1, 'k': 0, 'l': 0, 'm': 2, 'n': 3, 'o': 2, 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0})

class Week06WordHistogram(UTestCase):
    def test_WordHistogram(self):
        from cp.ex06.word_histogram import word_histogram
        self.assertEqual(word_histogram(["Write the function word histogram."," which takes as argument a list containing lines of a text."]),{'write': 1, 'the': 1, 'function': 1, 'word': 1, 'histogram': 1, 'which': 1, 'takes': 1, 'as': 1, 'argument': 1, 'a': 2, 'list': 1, 'containing': 1, 'lines': 1, 'of': 1, 'text': 1})
        self.assertEqual(word_histogram(["The function should make a histogram of words that occur in the text.","Punctuation, spaces, and capitalization should be ignored.",]),{'the': 2, 'function': 1, 'should': 2, 'make': 1, 'a': 1, 'histogram': 1, 'of': 1, 'words': 1, 'that': 1, 'occur': 1, 'in': 1, 'text': 1, 'punctuation': 1, 'spaces': 1, 'and': 1, 'capitalization': 1, 'be': 1, 'ignored': 1})
        self.assertEqual(word_histogram(["The function should return a dictionary. The function.",]),{'the': 2, 'function': 2, 'should': 1, 'return': 1, 'a': 1, 'dictionary': 1})
 
class Week06ExtractKeywords(UTestCase):
    def test_ExtractKeywords(self):
        from cp.ex06.word_histogram import extract_keyword
        ignore_list = ['a', 'an', 'the', 'above', 'across', 'against', 'along', 'among', 'around',    'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'by',    'down', 'from', 'in', 'into', 'near', 'of', 'off', 'on', 'to', 'toward',    'under', 'upon', 'with', 'within','function', 'for', 'and', 'nor', 'but', 'or', 'yet', 'so']
        self.assertEqual(extract_keyword(["one two two three three three four four four four five five five five five six six six six six six",], ignore_list), {'six': 6, 'five': 5, 'four': 4, 'three': 3, 'two': 2})
        lines2 = ["Words are flowing out like endless rain into a paper cup. They slither wildly as they slip away across the universe. Pools of sorrow, waves of joy are drifting through my opened mind. Possessing and caressing me. Images of broken light which dance before me like a million eyes. They call me on and on across the universe. Thoughts meander like a restless wind inside a letterbox they. They tumble blindly as they make their way across the universe. Jai guru deva, om. Sounds of laughter shades of life are ringing. Through my open ears inciting and inviting meLimitless undying love which shines around me like a million suns. It calls me on and on across the universe"]
        self.assertEqual(extract_keyword(lines2,ignore_list),{'they': 6, 'me': 5, 'like': 4, 'universe': 4, 'are': 3})

class Week06SpellCheck(UTestCase):
    def test_spell_check(self):
        from cp.ex06.spell_check import spell_check
        corrections = {'occurence': 'occurrence', 'apsolute': 'absolute', 'teh': 'the', 'acess': 'access', 'occured': 'occurred', 'exampel': 'example'}
        text = "The apsolute acess to teh data occured in this exampel"
        self.assertEqual(spell_check(text, corrections),"The absolute access to the data occurred in this example")
        text2= "The first occurence of teh mean apsolute error formula look at teh exampel below"
        self.assertEqual(spell_check(text2, corrections),"The first occurrence of the mean absolute error formula look at the example below")
        self.assertEqual(spell_check("We can handle teh damag", {'damag': 'damage'}),"We can handle teh damage")
        self.assertEqual(spell_check("We can handle teh damag.",{'damag': 'damage'}),"We can handle teh damage.")
        text3 = "The apsolute acess to teh, data occured in this exampel."
        self.assertEqual(spell_check(text3, corrections),"The absolute access to the, data occurred in this example.")
        
class Week06GetPeopleByLanguage(UTestCase):
    def test_GetPeopleByLanguage(self):
        from cp.ex06.language import get_people_by_language
        name_languages = {
                'Peter': ['Danish', 'English', 'German'],
                'Alice': ['English', 'French', 'Spanish'],
                'John': ['Spanish', 'English', 'French'],
                'Maria': ['Danish', 'Spanish', 'German'],
                'Anna': ['German', 'English', 'French'],
                'David': ['English', 'French'],
                'Sophia': ['Danish', 'Spanish'],
                'Michael': ['German', 'English'],
                'Emma': ['English', 'French'],
                'Daniel': ['Spanish', 'English', 'German'],
                'Laura': ['English', 'Spanish', 'Italian'],
                'Mark': ['English', 'German'],
                'Isabella': ['French', 'Spanish'],
                'William': ['English'],
                'Sophie': ['German', 'French'],
                'Robert': ['English', 'German'],
                'Olivia': ['French', 'Spanish'],
                'James': ['English'],
                'Ella': ['Spanish', 'Italian'],
                'Alexander': ['English', 'German'],
                'Lily': ['English', 'French']
                }
        self.assertEqual(get_people_by_language('English', name_languages),['Peter', 'Alice', 'John', 'Anna', 'David', 'Michael', 'Emma', 'Daniel', 'Laura', 'Mark', 'William', 'Robert', 'James', 'Alexander', 'Lily'])
        self.assertEqual(get_people_by_language('Spanish', name_languages),['Alice', 'John', 'Maria', 'Sophia', 'Daniel', 'Laura', 'Isabella', 'Olivia', 'Ella'])
        self.assertEqual(get_people_by_language('German', name_languages),['Peter', 'Maria', 'Anna', 'Michael', 'Daniel', 'Mark', 'Sophie', 'Robert', 'Alexander'])
        self.assertEqual(get_people_by_language('French', name_languages),['Alice', 'John', 'Anna', 'David', 'Emma', 'Isabella', 'Sophie', 'Olivia', 'Lily'])

class Week06TruncateAndNormalize(UTestCase):
    def test_truncate(self):
        from cp.ex06.truncate import truncate_values
        settings = {'vmin': 0, 'vmax': 2, 'normalize': False}
        settings2 = {'vmin': 0, 'vmax': 2, 'normalize': True}
        float_list = [0.5,0.4,-0.3, 1.5, 2.5, 3.5]
        float_list2 = [0,1.,2.,3.,4.,5.]        
        self.assertEqual((truncate_values(float_list,settings)),[0.5, 0.4, 0, 1.5, 2, 2])
        self.assertEqual((truncate_values(float_list2,settings2)),[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])


class Week06SentimentAnalysis(UTestCase):
    def test_sentiment_analysis(self):
        from cp.ex06.sentiment_analysis import sentiment_analysis
        self.assertEqual(sentiment_analysis('I think the food was excellent and great, but the waiter service was horrible '),-5)
        self.assertEqual(sentiment_analysis('When I woke up I was feeling very bad but then I had a coffee and my day turned out to be excellent '),4)
        self.assertEqual(sentiment_analysis('I know it is good not to complain, but the selection criteria were genuinely inadequate and unfair '),-1)


class Week06MultiTap(UTestCase):
    def test_multi_tap(self):
        from cp.ex06.multi_tap import multi_tap 
        self.assertEqual(multi_tap([7, 7, 7, 7, 6, 6, 6], [0, 0.7, 0.8, 0.9, 1, 1.1, 1.2]), 'PRO')
        self.assertEqual(multi_tap([4, 4, 4, 0, 2, 6, 0, 4, 4, 2, 7, 7, 9, 9, 9], [0.1, 0.3, 0.6, 1.0, 1.2, 1.4, 1.7, 2.0, 2.2, 2.5, 2.9, 3.9, 4.3, 4.4, 4.8]), "I AM HAPPY")
        self.assertEqual(multi_tap([7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 8, 8, 3], [0.1, 0.5, 0.8, 1.2, 2.6, 3.7, 4.1, 4.2, 4.5, 4.9, 5.1, 5.4, 5.6, 5.9]), "SPROUD")
        self.assertEqual(multi_tap([4, 4, 4, 2, 2, 2, 3, 3, 0, 4, 4, 4, 2, 2, 2, 3, 3, 0, 2, 2, 2, 2, 2, 9, 9, 9], [0.3, 0.7, 0.8, 1.1, 1.3, 1.5, 1.7, 1.8, 2.1, 2.4, 2.7, 3.0, 3.4, 3.7, 3.9, 4.0, 4.3, 4.5, 4.7, 5.0, 6.4, 7.9, 8.3, 8.5, 8.7, 9.0]), "ICE ICE BABY")
        self.assertEqual(multi_tap([5, 5, 5, 4, 4, 4, 8, 8, 8, 3, 3, 0, 5, 5, 5, 2, 8, 8, 4, 4, 4, 0, 5, 5, 5, 4, 4, 4, 7, 7, 7, 7, 8], [0.7, 0.9, 1.2, 1.6, 1.7, 2.0, 2.4, 2.5, 2.8, 3.2, 3.5, 3.7, 3.9, 4.3, 4.6, 4.8, 5.0, 5.3, 5.6, 6.3, 6.7, 6.8, 7.1, 7.3, 7.5, 7.8, 8.0, 8.1, 8.3, 8.5, 8.7, 8.9, 9.3]), "LIVE LAUGH LIST")
        

class Week06Tests(Report): #240 total.
    title = "Tests for week 06"
    #version = 0.1
    #url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (Week06TextToNato, 10),
                (Week06LetterHistogram, 10),
                (Week06WordHistogram, 10),
                (Week06ExtractKeywords, 10),
                (Week06SpellCheck, 10),
                (Week06GetPeopleByLanguage, 10),
                (Week06TruncateAndNormalize, 10),
                (Week06SentimentAnalysis,10),
                (Week06MultiTap, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week06Tests())

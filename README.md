# HackHolyoke-TutorTots-Python

Tutor Tots -- an efficient web tool designed to help college administrators expedite the process of assigning peer tutors to tutees without the hassle of manually handling raw data.

How Tutor Tots work: The web tool takes in tutor’s and tutee information using Wix’s forms and collections (database) features. Using an array of different engines, the web tool computes and assigns tutees to tutors using an algorithm that would produce the best possible match. After computation, it then outputs the results in a human readable way.

My contribution: I built the needed Wix input forms to produce two sets of database - one for tutor and one for tutee. Then, I collaborated with a teammate to construct the backbone of readtutor.py. As the middle person between the data and the person in charge of optimizing and making the assignments, I cleaned up readtutor.py's code accordingly and made readtutee.py. We created two different Python files for tutors and tutee since input fields are different for each form.

Included in this repository is readtutor.py, readtutee.py and two sample csv files.

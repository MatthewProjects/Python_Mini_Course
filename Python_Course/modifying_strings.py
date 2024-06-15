def main():
    print("Running modifying_strings.main()")
    course_description = "The Python course is a comprehensive and hands-on learning experience designed to introduce students to the fundamentals of Python programming. Through a combination of interactive lectures, practical exercises, and real-world projects, participants will gain a solid understanding of Python syntax, data structures, control flow, functions, and object-oriented programming. They will also explore various libraries and modules for tasks such as data analysis, web scraping, and GUI development. By the end of the course, students will be equipped with the skills to develop their own Python applications and confidently pursue further programming endeavors"

    print(len(course_description))

    words = course_description.split()
    print(len(words))

    sentences = course_description.split(". ")
    num_sentences = len(sentences)
    print("Number of sentences:", num_sentences)

    new_course_description = "The Python course is a comprehensive and hands-on learning experience designed to introduce students to the fundamentals of Python programming. Through a combination of interactive lectures, practical exercises, and real-world projects, participants will gain a solid understanding of Python syntax, data structures, control flow, functions, and object-oriented programming. They will also explore various libraries and modules for tasks such as data analysis, web scraping, and GUI development. By the end of the course, students will be equipped with the skills to develop their own Python applications and confidently pursue further programming endeavors"

    # Replace "Python" with "JavaScript" and store the result
    javascript_description = new_course_description.replace("Python", "JavaScript")

    # Replace "programming" with "coding" in the modified string
    modified_description = javascript_description.replace("programming", "coding")

    print(modified_description)

    print(modified_description.upper())

    print(modified_description.lower())
    print("Finished modifying_strings.main()")

if __name__ == "__main__":
    main()

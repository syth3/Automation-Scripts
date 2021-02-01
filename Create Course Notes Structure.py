# 1) gather user input for directory to put files and names of sections
# 2) Create markdown files for all sections and place the section name as the heading for the file
    # Number the sections in order they were given
# 3) Create screenshots directory
# 4) Create directory inside screenshots directory for each section (number the sections)
from pathlib import Path


def create_markdown_files(section_names, dest_dir):
    for name in section_names:
        full_path = dest_dir / name
        with full_path.open("w") as markdown_file:
            markdown_file.write("# " + str(name))


def create_screenshot_dirs(section_names, dest_dir):
    screenshots_dir = dest_dir / "Screenshots"
    screenshots_dir.mkdir()
    for name in section_names:
        full_path = screenshots_dir / name
        full_path.mkdir()


def gather_course_name():
    return str(input("Enter Course Name: "))


def gather_dest_dir(course_name):
    dest_dir = Path(input("Enter Absolute Path for Destination Directory: "))
    while not dest_dir.is_dir():
        print("Path entered is not a valid directory. Try again")
        dest_dir = Path(input("Enter Absolute Path for Destination Directory: "))
    dest_dir = dest_dir / course_name
    if dest_dir.is_dir():
        proceed_input = input("The following directory already exists: " + str(dest_dir) + "\nProceed? (y/n): ")
        if proceed_input == 'n':
            exit(1)
    return dest_dir


def gather_section_names():
    section_names = []
    section_name = input("Enter Section name (type qwe to stop): ")
    counter = 1
    while section_name != 'qwe':
        section_names.append(str(counter).zfill(2) + " - " + section_name)
        counter += 1
        section_name = input("Enter Section name (type qwe to stop): ")
    return section_names


def gather_input():
    course_name = gather_course_name()
    dest_dir = gather_dest_dir(course_name)
    section_names = gather_section_names()
    return course_name, dest_dir, section_names


def make_dest_dir(dest_dir):
    dest_dir.mkdir()


def main():
    course_name, dest_dir, section_names = gather_input()
    make_dest_dir(dest_dir)
    create_markdown_files(section_names, dest_dir)
    create_screenshot_dirs(section_names, dest_dir)


if __name__ == '__main__':
    main()

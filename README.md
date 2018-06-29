
| [Website](http://links.otrenav.com/website) | [Twitter](http://links.otrenav.com/twitter) | [LinkedIn](http://links.otrenav.com/linkedin)  | [GitHub](http://links.otrenav.com/github) | [GitLab](http://links.otrenav.com/gitlab) | [CodeMentor](http://links.otrenav.com/codementor) |

---

# Behavior Driven Development (BDD) with Django

- Omar Trejo
- February, 2016

The objective is to show how `behave` can be used to do BDD with Django.

## Requirements

- `django` (pip), web framework
- `factory-boy` (pip), create objects for tests easily
- `behave-django` (pip), BDD framework for Python
- `selenium` (pip), testing web browsers
- `phantomjs` (system), _headless_ browser for tests

Install requirements with `pip` and install (in Ubuntu):

```
$ sudo apt-get install phantomjs
```

## Usage

To run the tests:

```
$ ./manage.py behave
```

## Notes

1. We're using PhantomJS to test, but if the appropiate line is changed in
   `features/environment.py` you can actually see the tests with Firefox.

2. Both `behave` and `selenium` offer a ton of funcionality that is not shown in
   this repository. See their documentation for further details.

3. To understand `factory_boy` you should be familiar with `Factories`.

4. Another BDD framework that is worth looking at is `robot-framework`.

---

> "The best ideas are common property."
>
> —Seneca

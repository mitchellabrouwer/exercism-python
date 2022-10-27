from typing import List


def round_scores(student_scores: List[str]) -> List[str]:

    return [round(score) for score in student_scores]


def count_failed_students(student_scores: List[int]) -> int:

    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> List[int]:

    return list(range(41, highest, int((highest - 40) / 4)))


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:

    return [f"{i + 1}. {student_names[i]}: {score}" for i, score in enumerate(student_scores)]


def perfect_score(student_info: List[tuple]) -> List[str]:

    return next(filter(lambda student: student[1] == 100, student_info), [])

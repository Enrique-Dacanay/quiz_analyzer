scores = []

for i in range(1, 6):
    score = int(input(f"Enter quiz {i}:"))
    scores.append(score)

print("===== QUIZ SCORE REPORT =====")
print("Quiz score:", scores)
n_quiz = len(scores)
total_score = sum(scores)
average = total_score / n_quiz


print(f"Number of quizzes:{n_quiz}")
print(f"Total score:{total_score}")
print(f"Average score:{average:.2f}")
print(f"Highest score:{max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Ascending:", sorted(scores))
print(f"Descending:", sorted(scores, reverse=True))
print(f"Original score:",scores)

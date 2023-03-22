times = [0, 0]

for _ in range(30):
  job_manage    = list(map(int, input().split()))
  current_times = [0, 0]

  if job_manage.count(0) == 4: continue

  # 時の部分を計算
  current_times[0] += job_manage[2] - job_manage[0]

  #分の部分を計算
  current_times[1] += abs(job_manage[1] - job_manage[3])

  #休憩時間の差し引き
  if (job_manage[2] - job_manage[0]) > 8:
    current_times[0] -= 1
  elif 6 < (job_manage[2] - job_manage[0]) <= 8:
    if (current_times[1] - 45) < 0:
      current_times[0] -= 1
      current_times[1]  = 60 + (current_times[1] - 45)
    else:
      current_times[1] -= 45

  #加算
  times[0] += current_times[0]
  times[1] += current_times[1]

  if times[1] >= 60:
    times[0] += 1
    times[1]  = times[1] - 60

print(*times)
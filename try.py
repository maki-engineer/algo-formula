times         = [0, 0]
job_time_sums = 0

for _ in range(30):
  job_manage = list(map(int, input().split()))
  job_time   = 0

  if job_manage.count(0) == 4: continue

  # 時を加算
  job_time += (job_manage[2] - job_manage[0]) * 60

  # 分を加算
  job_time += abs(job_manage[1] - job_manage[3])

  # 休憩時間差し引き
  if job_time > 480:
    job_time -= 60
  elif 360 < job_time <= 480:
    job_time -= 45

  # 加算
  job_time_sums += job_time

# 変換
times[0] = job_time_sums // 60
times[1] = job_time_sums  % 60

print(*times)
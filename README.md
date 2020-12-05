# 유전자 알고리즘 Snake Game AI

유전자 알고리즘을 이용한 Snake Game 머신러닝 프로그램입니다.
하단에 기술된 Evolutionary Snake 프로그램을 개량하여 제작하였습니다.

## 이전 연구 문제점 도출
1. 긴 학습시간
2. 2030세대를 지난 진화 후에도 평균 1~2점의 낮은 스코어
3. 학습 이후에도 여전한 빠른 사망

## 원인 분석
1. 테스트 종료 조건의 불분명함
2. 무한루프 검사 미구현
3. 생존시간에 따른 가산점 미부여
4. 너무 짧은 센서범위

## 개선사항
1. 점수가 너무 낮거나 득점을 오랜기간 못할 때 종료
2. 무한루프 감지 시 감점 후 종료
3. 순탄한 진행과정 내에서는 진행 시간별 가산점 부여
4. 센서 크기 2배로 확장
5. 기타 세세한 수치 수정

## Run
```
python evolution.py
```

## Dependencies
- Python 3+
- numpy
- pygame

Snake game code by HonzaKral: https://gist.github.com/HonzaKral/833ee2b30231c53ec78e
Base evolutionary snake program by kairess: https://github.com/kairess/genetic_snake
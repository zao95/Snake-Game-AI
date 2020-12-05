import pygame, random
import numpy as np
from copy import deepcopy
from snake import Snake, SCREEN_SIZE, PIXEL_SIZE
from genome import Genome

# 기본 변수 선언
N_POPULATION = 50
N_BEST = 5
N_CHILDREN = 5
PROB_MUTATION = 0.2

# 초기 설정
pygame.init()
pygame.font.init()
display_setting = pygame.display.set_mode((SCREEN_SIZE * PIXEL_SIZE, SCREEN_SIZE * PIXEL_SIZE))
pygame.display.set_caption('Snake')

# 첫번째 인구 발생(generate 1st population)
genomes = [Genome() for _ in range(N_POPULATION)]
best_genomes = None

# 진화 1번 = 1루프
n_gen = 0
while True:
    n_gen += 1

    # 유전자 열거 후, index와 유전자 값을 변수로 루프
    for i, genome in enumerate(genomes):
        # 유전자 기반으로 스네이크 게임 진행 후 fitness를 유전자에 입력
        snake = Snake(display_setting, genome=genome)
        fitness, score = snake.run()

        genome.fitness = fitness

        # print('Generation #%s, Genome #%s, Fitness: %s, Score: %s' % (n_gen, i, fitness, score))

    # 부모 유전자들을 이전 게임 시행의 fitness가 포함된 상태로 추가
    if best_genomes is not None:
        genomes.extend(best_genomes)

    # 유전자의 fitness값을 기반으로 내림차순 정렬
    genomes.sort(key=lambda x: x.fitness, reverse=True)

    avg_fitness = 0
    for i in genomes:
        avg_fitness += i.fitness
    avg_fitness /= len(genomes)
    print('===== #%s 세대 유전자\t최고 Fitness %s\t평균 Fitness %s =====' % (n_gen, genomes[0].fitness, avg_fitness))

    # N_BEST값 만큼 추출하여 깊은 복사
    best_genomes = deepcopy(genomes[:N_BEST])

    # 유전(crossover)
    for i in range(N_CHILDREN):
        new_genome = deepcopy(best_genomes[0])
        a_genome = random.choice(best_genomes)
        b_genome = random.choice(best_genomes)

        cut = random.randint(0, new_genome.w1.shape[1])
        new_genome.w1[i, :cut] = a_genome.w1[i, :cut]
        new_genome.w1[i, cut:] = b_genome.w1[i, cut:]

        cut = random.randint(0, new_genome.w2.shape[1])
        new_genome.w2[i, :cut] = a_genome.w2[i, :cut]
        new_genome.w2[i, cut:] = b_genome.w2[i, cut:]

        cut = random.randint(0, new_genome.w3.shape[1])
        new_genome.w3[i, :cut] = a_genome.w3[i, :cut]
        new_genome.w3[i, cut:] = b_genome.w3[i, cut:]

        cut = random.randint(0, new_genome.w4.shape[1])
        new_genome.w4[i, :cut] = a_genome.w4[i, :cut]
        new_genome.w4[i, cut:] = b_genome.w4[i, cut:]

        best_genomes.append(new_genome)

    # 돌연변이(mutation)
    genomes = []
    for i in range(int(N_POPULATION / (N_BEST + N_CHILDREN))):
        for bg in best_genomes:
            new_genome = deepcopy(bg)

            mean = 20
            stddev = 10

            if random.uniform(0, 1) < PROB_MUTATION:
                new_genome.w1 += new_genome.w1 * np.random.normal(mean, stddev, size=(6, 10)) / 100 * np.random.randint(-1, 2, (6, 10))
            if random.uniform(0, 1) < PROB_MUTATION:
                new_genome.w2 += new_genome.w2 * np.random.normal(mean, stddev, size=(10, 20)) / 100 * np.random.randint(-1, 2, (10, 20))
            if random.uniform(0, 1) < PROB_MUTATION:
                new_genome.w3 += new_genome.w3 * np.random.normal(mean, stddev, size=(20, 10)) / 100 * np.random.randint(-1, 2, (20, 10))
            if random.uniform(0, 1) < PROB_MUTATION:
                new_genome.w4 += new_genome.w4 * np.random.normal(mean, stddev, size=(10, 3)) / 100 * np.random.randint(-1, 2, (10, 3))

            genomes.append(new_genome)

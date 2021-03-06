from algorithms import on_policy_first_visit_monte_carlo_control
from grid_world import S, A, is_terminal, step, reset

if __name__ == "__main__":
    Q, Pi = on_policy_first_visit_monte_carlo_control(len(S), len(A),
                                                      reset,
                                                      is_terminal, step,
                                                      episodes_count=50000,
                                                      max_steps_per_episode=100)
    print(Q)
    print(Pi)

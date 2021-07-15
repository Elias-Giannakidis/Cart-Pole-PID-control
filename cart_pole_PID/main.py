import gym
import keyboard

env_name = "CartPole-v1"
env = gym.make(env_name)
env.reset()

#Define PID parameters
P1 = 3
D1 = 1.9
P2 = 10
D2 = 2.4

stp = 0
speed = 0.08

#Define PID function
def PIDfunction(state):

    S = P1*state[0] + D1*state[1] + P2*state[2] + D2*state[3] + stp
    if S > 0:
        return 1
    else:
        return 0

new_state, reward, done, _ = env.step(env.action_space.sample())
done = False

while not done:
    if keyboard.is_pressed('a'):
        stp += speed
    if keyboard.is_pressed('d'):
        stp -= speed
    print(stp)
    new_state, reward, done, _ = env.step(PIDfunction(new_state))
    done = False
    env.render()
    if keyboard.is_pressed('p'):
        done = True

env.close()



from unity3d.app import SofiUnity3d
import time


if __name__ == '__main__':
    app = SofiUnity3d(background=True)
    app.start()

    # Wait a sec just to make sure we're fully connected
    time.sleep(1)

    app.spawn("barbarian", "barb", scale=(2, 2, 2), look_at="Main Camera", animation="Walk", rigidbody=True, freeze_rotation=True)
    app.spawn("tree", "tree1", scale=(1.5, 1.5, 1.5), position=(-5, 0, 13))
    app.spawn("tree", "tree2", scale=(1.5, 1.5, 1.5), position=(6, 0, 10))
    app.spawn("well", "well", scale=(0.5, 0.5, 0.5), position=(-0.4, 1.91, 14), rotation=(-90, -945, 0))

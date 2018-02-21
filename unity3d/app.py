from sofi.app import Sofi


class SofiUnity3d(Sofi):
    """A regular Sofi application with command wrappers to talk to the Unity3D WebSocket client"""

    def start(self):
        """Overriding start() because we don't support desktop / browser modes from base Sofi"""

        super().start(desktop=False)

    def update(self, name, position=None, rotation=None, scale=None, rigidbody=None, freeze_rotation=None, look_at=None, animation=None, collider=None, color=None, text=None):
        """Update the game object given by `name`"""

        cmd = {'command': 'unity.update'}

        cmd['name'] = name

        self._send_command(cmd, position, rotation, scale, rigidbody, freeze_rotation, look_at, animation, collider, color, text)


    def spawn(self, prefab, name, position="SpawnPoint", rotation=(0, 0, 0), scale=(1, 1, 1), rigidbody=None, freeze_rotation=None, look_at=None, animation=None, collider=None, color=None, text=None):
        """Spawn a new game object from the prefab given by `prefab`"""

        cmd = {'command': 'unity.spawn'}

        cmd['obj'] = prefab
        cmd['name'] = name

        self._send_command(cmd, position, rotation, scale, rigidbody, freeze_rotation, look_at, animation, collider, color, text)


    def _send_command(self, cmd, position=None, rotation=None, scale=None, rigidbody=None, freeze_rotation=None, look_at=None, animation=None, collider=None, color=None, text=None):
        """Send a command to the Unity3D WebSocket client"""

        if position is not None:
            if isinstance(position, str):
                cmd['position_on'] = position
            else:
                cmd['position'] = position

        if rotation is not None:
            cmd['rotation'] = rotation

        if scale is not None:
            cmd['scale'] = scale

        if rigidbody is not None:
            cmd['rigidbody'] = rigidbody

        if freeze_rotation is not None:
            cmd['rigidbody_freeze_rotation'] = freeze_rotation

        if look_at is not None:
            cmd['look_at'] = look_at

        if animation is not None:
            cmd['animation'] = animation

        if collider is not None:
            cmd['collider'] = collider

        if color is not None:
            cmd['color'] = color

        if text is not None:
            cmd['text'] = text

        # TODO: This is assuming 1 client!
        self.clients[0].dispatch(cmd)

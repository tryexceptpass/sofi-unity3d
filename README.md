`sofi-unity3d` explores how to control a Unity3D game environment through [sofi](https://www.github.com/tryexceptpass/sofi) by using [WebSocketSharp](https://github.com/sta/websocket-sharp) as a client inside the game world.

For more details on how it works, have a look at [Making 3D Interfaces for Python with Unity3D](https://medium.com/@tryexceptpass/user-interfaces-with-unity3d-and-python-eb2e7744518a)

## Requirements
* You'll need to install the Sofi package, available at the tryexceptpass/sofi repository.
* To run the game world:
  * If you have Unity3D already and want to run from there, use the project in the `engine` directory.
  * If you don't, you can download the built world from the links below:
    * [MacOS](https://s3.amazonaws.com/tryexceptpass/sofi3d.app.zip)
    * [Windows](https://s3.amazonaws.com/tryexceptpass/sofi3d.exe)
    * [Linux](https://s3.amazonaws.com/tryexceptpass/sofi3d.x86.zip)
* Update `server.py` with your twitter account credentials.

## Execution
1. Start the game world by running the executable you downloaded above or start it directly from Unity3D. This will wait for a websocket server at port 9000.
2. Run the python code: `python server.py`. This will start the slide deck I used at PyCaribbean and start a twitter listener for #python which will spawn objects as tweets come in.

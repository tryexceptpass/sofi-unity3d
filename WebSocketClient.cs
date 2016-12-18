using UnityEngine;
using WebSocketSharp;

public class WebSocketClient : MonoBehaviour {
    WebSocket ws;

	// Use this for initialization
	void Start () {

        ws = new WebSocket("ws://127.0.0.1:9000");
        ws.OnMessage += (sender, e) =>
        {
            Debug.Log("Server says: " + e.Data);
            ws.Close();
        };

        ws.Connect();
        ws.Send("{\"event\":\"init\"}");
    }
	
	// Update is called once per frame
	void Update ()
    {
        ws.Send("{\"event\":\"init\"}");
    }
}

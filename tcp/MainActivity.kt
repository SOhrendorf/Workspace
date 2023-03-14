package com.example.tcp_server_by_Revan

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import io.ktor.network.selector.ActorSelectorManager
import io.ktor.network.sockets.Socket
import io.ktor.network.sockets.aSocket
import io.ktor.util.KtorExperimentalAPI
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.runBlocking
import java.net.InetSocketAddress


@Suppress("UNREACHABLE_CODE")
class MainActivity : AppCompatActivity() {
    @KtorExperimentalAPI
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        val port = findViewById<EditText>(R.id.get_port)
        val sumbitbutton = findViewById<Button>(R.id.button3)
        //val dispMessage = findViewById<TextView>(R.id.textView4)



        fun server(){
            runBlocking {
                val server = aSocket(ActorSelectorManager(dispatcher = Dispatchers.IO)).tcp().bind(InetSocketAddress( 6666))
                Toast.makeText(this@MainActivity, " starte Server auf ${server.localAddress} ", Toast.LENGTH_SHORT).show()
                val socket : Socket = server.accept()

                while (true) {
                    server.accept()
                }
            }
        }

        class SimpleThread: Thread() {
            public override fun run() {
                server()
            }
        }


        sumbitbutton.setOnClickListener(){
            //dispMessage.setText("der port ist" + port)
        }

        button.setOnClickListener {
            //wenn button dann:
            Toast.makeText(this@MainActivity, " starte Server... ", Toast.LENGTH_SHORT).show()
            //getRuntime().exec("su")
            server()
        }

        button2.setOnClickListener {
            //wenn button2 dann :
            Toast.makeText(this@MainActivity, " stoppe Server... ", Toast.LENGTH_SHORT).show()
        }



    }
}

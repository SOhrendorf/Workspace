object HelloWorld{
    def main(args: Array[String])
    {
        println("Ich lebe, juhu!!")
        var meineVariable : String = "Jonas"
        meineVariable = "Simon der Allerechte"
        println(meineVariable)

        //rechnen(5, 10)
        schleife()
    }

    def rechnen(a: Int,b : Int)
    {
        var c = a+b
        println(c)
    }

    def schleife()
    {
        var x = 0
        var y = 0

        for(x <- 1 to 10) //variable vorher definieren und Range angeben
        {
            println("Die Schleife ist hier")
        }
    }
}
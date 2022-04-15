object main {
  def incrementMethod(x: Int): Int = x+1
  this.incrementMethod(3)

  val incrementFunction = (x: Int) => x+1
  val incrementFunctionExplicit = new Function[Int, Int] {
    override def apply(x: Int) = x+1
  }

  val three = incrementFunction(2)

  val incrementF = incrementMethod
  val incrementF2: Int => Int = incrementMethod
  List(1,2,3).map(incrementMethod)

  def multiArgAdder(x: Int)(y: Int) = x+y
  val add2 = multiArdAdder(2)

  val threeAlt = add2(1)
  List(1,2,3).map(multiArgAdder(3))
  def main(array: Array)
}

public class Kata {
  public static boolean betterThanAverage(int[] classPoints, int yourPoints) {
  
    int sum = yourPoints;
    
    for (int n: classPoints)
      sum += n;
    
    return (yourPoints > sum/(classPoints.length+1));
  }
}
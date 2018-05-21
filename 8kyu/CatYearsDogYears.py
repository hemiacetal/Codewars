public class Dinglemouse {

  public static int[] humanYearsCatYearsDogYears(final int humanYears) {
    
    int[] years = new int[]{humanYears,15,15};

    if (humanYears > 1){
      years[1]+=9;
      years[2] = years[1];
      
      if (humanYears > 2){
        years[1] += (humanYears-2)*4;
        years[2] = years[1]+(humanYears-2);
      }
          
      
    }
  
    return years;
  }

}
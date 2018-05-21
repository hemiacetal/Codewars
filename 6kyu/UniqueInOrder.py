def unique_in_order(iterable):

  n = [];
  length = len(iterable);
  
  if (length > 0):
      n.append(iterable[0]);
  if (length > 1):
      for i in range(1,len(iterable)):
          if (iterable[i] != iterable[i-1]):
              n.append(iterable[i]);
    
  return n;
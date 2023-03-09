function(csv_name){
  pval=wilcox.test(csv_name[,2], csv_name[,3])    # using the wilcox function select the second and third col of the csv 
  return(pval[3])  #return the third index of the outputted list 
}


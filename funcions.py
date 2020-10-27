def ConsultarLlocClasse():
  aules_mestre = ["Lab.Naturals" , "Lavabos" , "Direccio" , "Aula Plastica" , "Aula Musica" , "Aula Idiomes" , "Lab.Tecno" , "Lab.FiQ"]
  print("Per referir-se a aules específiques escriure:")
  print("Lab.Naturals")
  print("Lavabos")
  print("Direccio")
  print("Aula Plastica")
  print("Aula Musica")
  print("Aula Idiomes")
  print("Lab.Tecno")
  print("Lab.FiQ")
  print("Indica de quina classe surts ")
  classe_requerida = input.lower()
  print("Digues la classe a la que vols anar. Indica només si es aula o una de les opcions anteriors ")
  classe_de_sortida = input.lower()

  if classe_requerida == "aula ":
    if classe_de_sortida == "aula ":
      print ("2")
ConsultarLlocClasse()
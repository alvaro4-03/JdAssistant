def ConsultarLlocClasse():
  print("Per referir-se a aules específiques escriure:")
  print("Lab.Naturals")
  print("Lavabos")
  print("Direccio")
  print("Aula Plastica")
  print("Aula Musica")
  print("Aula Idiomes")
  print("Lab.Tecno")
  print("Lab.FiQ")
  
  classe_requerida = input("Digues la classe a la que vols anar. Indica només si es aula o una de les opcions anteriors").upper()
  classe_de_sortida = input("Indica de quina classe surts").upper()

  if classe_requerida == 
lojaA = {"iPhone 14", "Samsung Galaxy S23", "Xiaomi 13", "Motorola Edge 40"}
lojaB = {"Samsung Galaxy S23", "Xiaomi 13", "OnePlus 11", "iPhone 14 Pro"}

modelosTotais = lojaA | lojaB
print("Modelos que você pode comprar visitando ambas:", modelosTotais)

# Modelos em ambas (interseção)
modelosAmbas = lojaA & lojaB
print("Modelos disponíveis nas duas lojas:", modelosAmbas)
#Calcuradora
#Programado por ANTONIO REQUENA QUESADA - 2/01/2023
print("CALCULADORA \n")
user_name = input("Bienvenido a la calculadora, ingrese su nombre: ")
print(user_name,"puede usar la calculadora")
print("Estas son las operaciones que puede realizar: Suma - Resta - Multiplicación - División")
operacion = input("escriba que operación quiere hacer:")
print("Perfecto, vamos a realizar una", operacion)

if operacion == "suma" or "Suma":
    sumando_1 = int(input("Introduzca el primer sumando: "))
    sumando_2 = int(input("Introduzca el segundo sumando: "))
    resultado = sumando_1 + sumando_2
    print("El resultado de la suma es: ", resultado)
elif operacion == "resta" or "Resta":
    minuendo = int(input("Introduzca el minuendo: "))
    sustraendo = int(input("Introduzca el sustraendo: "))
    diferencia = minuendo - sustraendo
    print("El resultado de la resta es: ", diferencia)
elif operacion == "multiplicación" or "multiplicacion":
    factor_1 = int(input("Introduzca el primer factor: "))
    factor_2 = int(input("Introduzca el segundo factor: "))
    producto = round(factor_1 * factor_2)
    print("El producto de la multiplicación es: ", producto)
elif operacion == "division" or "división":
    dividendo = int(input("Introduzca el dividendo: "))
    divisor = int(input("Introduzca el divisor "))
    cociente = round(dividendo / divisor)
    resto = dividendo % divisor
    print("El cociente de la división es: ", cociente)
    print("El resto de la división es: ",resto)
else:
    print("Operación no Válida")

<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyB3tLo4gKC3k1n83tBZdAEkVJhkVtq4vls",
    authDomain: "python-prueba-9ea01.firebaseapp.com",
    projectId: "python-prueba-9ea01",
    storageBucket: "python-prueba-9ea01.appspot.com",
    messagingSenderId: "44936947801",
    appId: "1:44936947801:web:8cef008e941a4c2add6948",
    measurementId: "G-MX6J1B8W1K"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>

Para cada una de las 8 aplicaciones listadas abajo, redacta una descripción PEAS completa y coherente. Debes pensar como diseñador del agente: qué optimiza, dónde actúa, con qué puede mover o modificar el mundo, y qué puede observar.


### 1. Asistente virtual de voz
- **Performance: ** rapidez, precisión, satisfacción de usuario, privacidad, calidad de audio, %error, % éxito.
- **Environment: ** Usuario, Entorno, Internet, IOT, servicios digitales. Parcialmente observable, estocástico, secuencial, dinámico, continuo. 
- **Actuators: ** Acceso a internet/API, Bocina o altavoz para comunicarse, capacidad para iniciar un conteo o contador, Luz led o identificador de escucha activa, procesador de información, Regulador de volumen, envió de señales por protocolos conocidos (bluetooth, wifi). 
- **Sensors: **Micrófono, protocolos de conectividad (bluetooth, wifi, API), Sensor de temperatura, botones.

EL entorno es parcialmente observable porque a pesar de conocer todos sus métodos de acción no conoce las peticiones del usuario, no es omnisciente en el entorno. Es estocástico porque existen demasiadas variables que pueden cambiar los resultados de las acciones una misma solicitud puede tener miles de solucione. Es secuencial porque a veces las solicitudes pueden estar encadenadas, pero también puede ser episódica pues hay solicitudes e interacciones que no se relacionan entre sí. Es dinámico porque el entorno puede cambiar mientras se está respondiendo a una solicitud. 


### 2. Robot aspirador doméstico
- **Performance: ** rapidez, eficiencia, ruido, consumo, independencia, adaptabilidad, cobertura. 
- **Environment: ** entorno (habitación, sala, comedor), obstáculos, estación de limpieza y carga, personas o mascotas. Parcialmente observable (si puede mapear y mantener memoria eventualmente conocido, pero no observable), estocástico, secuencial, dinámico, continuo. 
- **Actuators: ** motores de las ruedas, motores de los rodillos limpiadores, motor aspirador, luz led de carga de la batería, display pequeño, bocina o buzzer. 
- **Sensors: ** sensores de proximidad, sensores de tipo de superficie (para identificar si la aspiradora necesita cambiar la succión por el tipo de piso o tipo de suciedad), botones, Lidar. 

Es parcialmente observable porque la rumba solo percibe el entorno a través de los sensores, a pesar de poder mapear el entorno no siempre está viendo todo el entorno al mismo tiempo. Es estocástica porque no siempre habrá tierra o suciedad en la misma ubicación, las acciones de la rumba no siempre dan el mismo resultado. Es secuencial porque al desplazarse cambia completamente el resultado de sus acciones siguientes. Es dinámico porque el usuario puede en cualquier momento poner objetos que obstaculicen su paso o nueva suciedad puede ser introducida al sistema. Es continuo porque las variables que utiliza para desplazarse son infinitas. 


### 3. Sistema de recomendación de streaming
- **Performance: ** %acierto a la predicción, satisfacción, reporte de usuarios (basado en reseñas), calidad de la recomendación, retención, diversidad. 
- **Environment: ** el usuario o la cuenta, base de datos de películas, internet, el objeto donde se está utilizando (celular, consola, Smart tv). Parcialmente observable, estocástico, secuencial, dinámico, continuo. 
- **Actuators: ** la presentación de las películas, el filtrado y los comandos de control de la base de datos, notificaciones al usuario (correo o las notificaciones de celular) 
- **Sensors: ** el historial de visualización del usuario, tiempo de retención al ver la película/serie, lectura de las reseñas, acceso a internet/API’s, interacción con el usuario (clicks, botones, controles) las cookies. 

Es parcialmente observable porque conoce su catálogo sus reglas de trabajo, pero no conoce los gustos del usuario o las elecciones que este hará. Es estocástico porque la recomendación de película a pesar de tener posibilidades determinadas no todos los usuarios actuaran de la misma manera cuando se haga la propuesta. Es secuencial porque la manera en la que se actualizan los gustos del usuario se define por las propuestas y estas a su vez cambian si el usuario las consume. Es dinámico porque el catálogo puede cambiar. Es continuo porque opera en un entorno infinito. 


### 4. Vehículo autónomo en ciudad
- **Performance: ** seguridad, velocidad, consumo de combustible, disponibilidad, comodidad, calidad de experiencia, precisión de la ubicación final. 
- **Environment: *calles, avenidas, personas, tráfico, señales viales, reglas de tránsito, clima. * Parcialmente observable, estocástico, secuencial, dinámico, continuo. 
- **Actuators: ** motor, volante, frenos, los instrumentos del auto (wipers, aire acondicionado, ventanas… etc.), máquina de cobro o métodos de cobro virtuales, pantalla para mostrar la ruta, app. 
- **Sensors: ** Lidar, cámaras, GPS, conectividad con la app, micrófono, métodos de ingreso de ruta (botones, pantalla, reconocimiento por voz), sensores de clima (lluvia, niebla), sensores en los instrumentos básicos, sensor de velocidad, tacómetro, acelerómetro, y sensores de golpes o de colisiones. 

Es parcialmente observable porque el vehículo solo conoce su entorno a través de los sensores que tiene, no puede conocer intenciones o en su totalidad la ruta. Desde que tenga que lidiar con el clima y este cuente con probabilidades de lluvia es estocástico. Es secuencial porque cada movimiento afecta al siguiente. Es dinámico porque constantemente cambian los estados del entorno, nuevos vehículos, accidentes, obras. Es continuo por desplazarse en un entorno con posibilidades infinitas. 


### 5. Agente de trading algorítmico en bolsa
- **Performance: ** precisión de predicciones, tiempo de ejecución, tiempo de reacción, perdidas, dependiendo el contexto minimizar riesgo, ganancias. 
- **Environment: ** bolsa de valores, el usuario o la cuenta asociada, los fondos, el entorno o app donde estará hosteada, los otros usuarios o competidores. Parcialmente observable, estocástico, secuencial, dinámico, continuo. 
- **Actuators: ** Comprar, vender, solicitar cotizaciones, enviar notificaciones al usuario, display de datos o alertas. 
- **Sensors: ** Conexión a internet/API’s, herramientas para interpretar el historial de operaciones, sensores para los trigers definidos por el usuario, lectura de datos del mercado (bases de datos). 

Es parcialmente observable porque contar con la información de las bases de datos no necesariamente le describe las intenciones de trading de su usuario no tiene una idea total del entorno. Estocástico por la volatilidad misma de bolsa de valores ninguna acción es 100% cierta. Es secuencial porque las acciones que realice modifican el estado siguiente en el que se encontrara. Es dinámico porque el mercado cambia mientras toma decisiones. Diría que tiene características mixtas de continuo o discreto, pero es más continuo que discreto por el simple hecho que los precios pueden estar entre los reales y eso es infinito. 


### 6. Sistema de diagnóstico médico asistido por IA
- **Performance: ** diagnósticos correctos, correcta interpretación, costos, percepción del cliente, reseñas, tiempo de diagnóstico, privacidad. 
- **Environment: ** Paciente, base de datos enfermedades, archivos de exámenes médicos (estudios de sangre, y resultados de pruebas), base de datos de medicamentos, hospitales, servidor donde esta hosteado, internet. Parcialmente observable, estocástico, secuencial, dinámico, continuo/discreto. 
- **Actuators: ** pantalla para comunicar el diagnostico, notificaciones, agendar citas, tratamientos o en los casos extremos contactar al 911. 
- **Sensors: ** Métodos de análisis y visión por computadora, conexión a internet/API’s, botones para configuración, lectura de entrada de texto por teclado o touchscreen, micrófono si cuenta con función de dictar. 

Es parcialmente observable porque la condición del paciente a pesar de poder verlo no es final hasta no conocer los síntomas internos. Es estocástico porque a veces síntomas similares pueden ser enfermedades distintas. Secuencial porque mientras se van introduciendo resultados de estudios o preguntas al paciente estos modifican el historial clínico que se está evaluando y cada una actualiza o mejora el análisis. Dinámico porque el paciente puede decaer o mejorar con el tiempo mientras se hace el análisis. Discreto porque la temperatura y las mediciones que se hacen son finitas, pero también es continuo porque existe un numero infinito de posibles diagnósticos. 


### 7. Dron de inspección de infraestructura
- **Performance: ** eficiencia de batería, tiempo de vuelo, cobertura, precisión de la inspección, seguridad, calidad de las imágenes, minimizar daños y riesgos al tomar muestras o imágenes. 
- **Environment: ** la estructura, el espacio aéreo, obstáculos u obstrucciones, personas, clima, centro de carga y ambiente de intercambio de información, el protocolo de comunicación. Parcialmente observable, estocástico, secuencial, dinámico, continuo. 
- **Actuators: ** Motores, cámara, estabilizador, luces indicadoras, luces para asistir a la visión, motores para mover la cámara de posición, buzzer o bocina. 
- **Sensors: ** Cámaras, Lidar, GPS, sensores de altura, sensores de proximidad, sensores de batería, giroscopios.  

Es parcialmente observable porque el agente solo percibe el entorno a través de los sensores que tiene. Estocástico porque existen variables que pueden introducir incertidumbre como el polvo, el viento y el clima. Secuencial porque el cambio de posiciones afecta la siguiente posible acción y los movimientos. Dinámico porque existen condiciones que pueden alterar al entorno de manera impredecible, obstáculos nuevos, personas caminando, todo mientras el agente toma las decisiones de movimiento. Continuo porque los valores de velocidad y orientación pueden ser infinitos. 


### 8. Agente jugador de ajedrez (digital)
- **Performance: ** número de movimientos, adaptabilidad, %victorias, % derrotas, tiempo de procesamiento, efectividad táctica, tiempo de partida, si el partido quedo tablas la puntuación final. 
- **Environment: **tablero, el oponente, las piezas, el tiempo, si está conectado a la red internet, la interface y el servidor. observable, determinista, secuencial, estático, discreto. 
- **Actuators: ** asumiendo que es digital: comunicación con servidor, protocolo para mover sus piezas, pantalla. 
- **Sensors: ** botones para configuración inicial, conectividad digital, acceso a internet/API’s, el reloj o tiempo, el estado de turnos. 

Es observable porque conoce en la totalidad el tablero en todo momento. Es determinista porque las acciones a pesar de ser muchísimas tienen siempre resultados conocidos. Es secuencial porque los movimientos tienen consecuencias a largo plazo. Es estático porque el tablero no cambia mientras se toma la decisión del movimiento siguiente, Discreto porque el entorno tiene una distribución finita.
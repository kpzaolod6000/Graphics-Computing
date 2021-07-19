#include "ProjectionMatriz.h"
#include<math.h>
int main() {
	
	glm::mat4 vertices = glm::mat4(-1.0, 1.0, -1.0, 1.0,
									2.0, 2.0, 0.0, 0.0,
									-6.0, -6.0, -6.0, -6.0,
									1.0, 1.0, 1.0, 1.0);
	cout << "Vertice: "<<endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{
			
			cout << vertices[i][j] << " ";
		}
		cout << endl;
	}
	float viewX = 100.00;
	float viewY = 80.00;
	float l = -2.0;
	float b = 0.0;
	float n = -4.0;
	float r = 2.0;
	float t = 3.0;
	float f = -8.0;

	/*TRANSFORMACION DE VIEWPORT*/
	glm::mat4 Mvp = buildViewPort(viewX, viewY);
	cout << "Matriz Mvp: " << endl << glm::to_string(Mvp) << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Mvp[i][j] << " ";
		}
		cout << endl;
	}

	/*TRANSFORMACION DE PROJECTION ORTHOGRAFICA*/
	glm::mat4 Morth = buildTrasformationOrtographics(l, b, n, r, t, f);
	cout << "Matriz Morth: " << endl <<glm::to_string(Morth) << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Morth[i][j] << " ";
		}
		cout << endl;
	}


	/*MATRIZ RESULTANTE M*/
	glm::mat4 Maux = Morth * Mvp;
	cout << endl << "Matriz Maux: " << endl <<glm::to_string(Maux) << endl;

	/*RESULTADO*/
	glm::mat4 aux = vertices * Maux;
	cout << "Posicion de los pixeles en la pantalla aux : " << glm::to_string(aux)<< endl;
	cout << endl;

	/*TRANSFORMACION DE LA CAMARA*/
	/*Posiciones de la camara 1 */
	/*ojo*/
	glm::vec3 e1 = glm::vec3(0.0, 5.0, 2.0);
	/*vector de mirada*/
	glm::vec3 g1 = glm::vec3(0.0, -2.0, -5.0);
	/*vector de vista superior*/
	glm::vec3 t1 = glm::vec3(0.0, 1.0, 0.0);

	/*Posiciones de la camara 1 */
	/*ojo*/
	glm::vec3 e2 = glm::vec3(0.0, 2.0, 2.0);
	/*vector de mirada*/
	glm::vec3 g2 = glm::vec3(0.0, -2.0, -5.0);
	/*vector de vista superior*/
	glm::vec3 t2 = glm::vec3(0.0, 1.0, 0.0);

	/*proyeccion de la camara 1*/
	glm::vec3 w1 = -(glm::normalize(g1));
	glm::vec3 u1 = glm::normalize(glm::cross(t1, w1));
	glm::vec3 v1 = glm::cross(w1, u1);

	/*proyeccion de la camara 2*/
	glm::vec3 w2 = -(glm::normalize(g2));
	glm::vec3 u2 = glm::normalize(glm::cross(t2, w2));
	glm::vec3 v2 = glm::cross(w2, u2);


	//cout << e1.x << e1.y << e1.z << endl;
	cout << "poyeccion camara 1: " << endl;
	cout << glm::to_string(w1) << endl;
	cout << glm::to_string(u1) << endl;
	cout << glm::to_string(v1) << endl;
	cout << "poyeccion camara 2: " << endl;
	cout << glm::to_string(w2) << endl;
	cout << glm::to_string(u2) << endl;
	cout << glm::to_string(v2) << endl;


	/*MATRIZ DE Mcam para la CAMARA 1*/

	glm::mat4 Mcam1 = buildTrasformationCamera(u1, v1, w1, e1);
	cout << endl << "Matriz Mcam de la camara 1:" << endl << glm::to_string(Mcam1) << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Mcam1[i][j] << " ";
		}
		cout << endl;
	}
	/*TRASFORMACION DEL VERTICE*/
	glm::mat4 M1 = Mcam1 * Morth * Mvp;
	cout << endl << "Matriz M1:" << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << M1[i][j] << " ";
		}
		cout << endl;
	}
	/*RESULTADO*/
	glm::mat4 result1 = vertices * M1;
	cout << "Posicion de los pixeles en la pantalla con camara 1: " << endl << glm::to_string(result1) << endl;
	cout << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << result1[i][j] << " ";
		}
		cout << endl;
	}
	///////////////////////////////////////////////////////////////////////////////////////////////////////////
	/*MATRIZ DE Mcam para la CAMARA 2*/

	glm::mat4 Mcam2 = buildTrasformationCamera(u2, v2, w2, e2);
	cout << endl << "Matriz Mcam de la camara 2:" << endl << glm::to_string(Mcam2) << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Mcam2[i][j] << " ";
		}
		cout << endl;
	}
	/*TRASFORMACION DEL VERTICE*/
	glm::mat4 M2 = Mcam2 * Morth * Mvp;
	cout << endl << "Matriz M2:" << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << M2[i][j] << " ";
		}
		cout << endl;
	}
	/*RESULTADO*/
	glm::mat4 result2 = vertices * M2;
	cout << "Posicion de los pixeles en la pantalla con camara 2: " << endl << glm::to_string(result2) << endl;
	cout << endl;

	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << result2[i][j] << " ";
		}
		cout << endl;
	}
	/////



	/*TRANSFORMACION DE PROJECTION DE PERSPECTIVA*/
	glm::mat4 P = buildTrasformationPerspective(n, f);
	cout << "Matriz P: " << endl << glm::to_string(P) << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << P[i][j] << " ";
		}
		cout << endl;
	}
	glm::mat4 Mper = P * Morth;
	cout << "Matriz Mper: " << endl << glm::to_string(Mper) << endl;

	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Mper[i][j] << " ";
		}
		cout << endl;
	}


	/*TRASFORMACION DEL VERTICE CON LA CAMARA 1*/
	glm::mat4 M1_per = Mcam1 * Mper * Mvp;

	cout << endl << "Matriz M1_per:" << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << M1_per[i][j] << " ";
		}
		cout << endl;
	}
	/*RESULTADO*/
	glm::mat4 result1_per = vertices * M1_per;
	cout << "Posicion de los pixeles en la pantalla con camara 1 y perspectiva: " << endl << glm::to_string(result1_per) << endl;
	cout << endl;

	cout << endl << "Matriz result1_per:" << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << result1_per[i][j] << " ";
		}
		cout << endl;
	}

	/*CONVITIENDO A COORDENADAS CARTESIANAS*/
	cout << "Resultado de coordenas Cartesianas: " << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{
			float w_p = result1_per[3][j];
			cout << result1_per[i][j] / w_p << " ";
		}
		cout << endl;
	}

	/*TRASFORMACION DEL VERTICE CON LA CAMARA 2*/
	glm::mat4 M2_per = Mcam2 * Mper * Mvp;

	cout << endl << "Matriz M2_per:" << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << M2_per[i][j] << " ";
		}
		cout << endl;
	}
	/*RESULTADO*/
	glm::mat4 result2_per = vertices * M2_per;
	cout << "Posicion de los pixeles en la pantalla con camara 2 y perspectiva: " << endl << glm::to_string(result2_per) << endl;
	cout << endl;

	cout << endl << "Matriz result2_per:" << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << result2_per[i][j] << " ";
		}
		cout << endl;
	}
	/*CONVITIENDO A COORDENADAS CARTESIANAS*/
	cout << "Resultado de coordenas Cartesianas: " << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{
			float w_p = result2_per[3][j];
			cout << result2_per[i][j] / w_p << " ";
		}
		cout << endl;
	}

	/*TRANSFORMACION CON FIELDVIEW*/
	/*int angulo = 60;
	t = tan(((angulo / 2) * 3.14159265) / 180) * abs(-3);
	b = -t;
	r = (viewX / 50) * t;
	l = -r;
	cout << t << endl;
	cout << b << endl;
	cout << r << endl;
	cout << l << endl;*/
	int angulo = 60;
	t = tan(((angulo / 2) * 3.14159265) / 180) * abs(n);
	b = -t;
	r = (viewX / viewY) * t;
	l = -r;
	cout << t << endl;
	cout << b << endl;
	cout << r << endl;
	cout << l << endl; 

	/*TRANSFORMACION DE LA CAMARA*/
	/*Posiciones de la camara 3 */
	/*ojo*/
	glm::vec3 e3 = glm::vec3(0.0, 4.0, 2.0);
	/*vector de mirada*/
	glm::vec3 g3 = glm::vec3(0.0, -2.0, -5.0);
	/*vector de vista superior*/
	glm::vec3 t3 = glm::vec3(0.0, 1.0, 0.0);

	/*proyeccion de la camara 3*/
	glm::vec3 w3 = -(glm::normalize(g3));
	glm::vec3 u3 = glm::normalize(glm::cross(t3, w3));
	glm::vec3 v3 = glm::cross(w3, u3);

	cout << "poyeccion camara 3: " << endl;
	cout << glm::to_string(w3) << endl;
	cout << glm::to_string(u3) << endl;
	cout << glm::to_string(v3) << endl;

	/*se modificop las coordenadas segun la formula viewField*/
	/*asi que consultamos como es la matriz nuevamente*/
	glm::mat4  Morth3 = buildTrasformationOrtographics(l, b, n, r, t, f);
	cout << "Matriz Morth3: " << endl << glm::to_string(Morth3) << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Morth3[i][j] << " ";
		}
		cout << endl;
	}

	glm::mat4 Mper3 = P * Morth3;
	cout << "Matriz Mper: " << endl << glm::to_string(Mper) << endl;

	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Mper3[i][j] << " ";
		}
		cout << endl;
	}
	/*CAMARA Mcam3*/
	glm::mat4 Mcam3 = buildTrasformationCamera(u3, v3, w3, e3);
	cout << endl << "Matriz Mcam de la camara 3:" << endl << glm::to_string(Mcam3) << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << Mcam3[i][j] << " ";
		}
		cout << endl;
	}

	glm::mat4 M3 = Mcam3 * Mper3 * Mvp;
	cout << endl << "Matriz M3:" << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << M3[i][j] << " ";
		}
		cout << endl;
	}
	/*RESULTADO*/
	glm::mat4 result3_per = vertices * M3;
	cout << "Posicion de los pixeles en la pantalla con camara 2: " << endl << glm::to_string(result3_per) << endl;
	cout << endl;

	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{

			cout << result3_per[i][j] << " ";
		}
		cout << endl;
	}

	/*CONVITIENDO A COORDENADAS CARTESIANAS*/
	cout << "Resultado de coordenas Cartesianas: " << endl;
	for (size_t i = 0; i < 4; i++)
	{

		for (size_t j = 0; j < 4; j++)
		{
			float w_p = result3_per[3][j];
			cout << result3_per[i][j] / w_p << " ";
		}
		cout << endl;
	}

	return 0;
}


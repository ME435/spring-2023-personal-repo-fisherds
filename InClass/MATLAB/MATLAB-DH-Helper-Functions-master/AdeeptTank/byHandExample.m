clc
ptAonLink1 = [0; 0; 2; 1]
ptBonLink2 = [1; 0; 1; 1]

A1 = create_A_matrix(2,3,0,0);
A2 = create_A_matrix(3, 0, 0, 0);

T0_1 = A1;
T0_2 = A1 * A2;

ptAonLink0 = T0_1 * ptAonLink1
ptBonLink0 = T0_2 * ptBonLink2
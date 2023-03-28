clc
pointAOnLink1 = [0;0;2;1];
pointBOnLink2 = [1;0;1;1];

A1 = create_A_matrix(2, 3, 0, 0);
A2 = create_A_matrix(3, 0, 0, 0);

T0_1 = A1;
T0_2 = A1 * A2;

fprintf("A")
expectedPointAOnLink0 = [2;0;5;1]
actualPointAOnLink0 = T0_1 * pointAOnLink1
fprintf("B")
expectedPointBOnLink0 = [6;0;4;1]
actualPointBOnLink0 = T0_2 * pointBOnLink2







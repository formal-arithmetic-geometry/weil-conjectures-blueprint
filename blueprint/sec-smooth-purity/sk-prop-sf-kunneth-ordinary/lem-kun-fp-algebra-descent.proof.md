+++
kind  = "proof"
of    = "lem-kun-fp-algebra-descent"
+++
A finitely presented $A$-algebra admits a finite presentation
$B\cong A[x_1,\dots,x_n]/(f_1,\dots,f_m)$ with $m,n$ finite; this is the
form of finite presentation used in
[def-weil-pbc-scheme-conventions]. Each $f_j$ has finitely many
coefficients, and each coefficient of $A$ is the image of an element of some
$A_i$; as the index set is filtered and only finitely many coefficients
occur, all of them are images of elements of a single $A_i$. Choose lifts
$\tilde f_1,\dots,\tilde f_m\in A_i[x_1,\dots,x_n]$ of the $f_j$ and put

$$
B_i=A_i[x_1,\dots,x_n]/(\tilde f_1,\dots,\tilde f_m),
$$

a finitely presented $A_i$-algebra. Base change along $A_i\to A$ commutes
with polynomial rings and with forming quotients, so

$$
B_i\otimes_{A_i}A\cong A[x_1,\dots,x_n]/(f_1,\dots,f_m)\cong B,
$$

which is the assertion.

+++
kind = "proof"
of = "lemma-point-count-bound--1"
order = 1177003
+++
Put $R=\Gamma(U_0,\mathcal O_{U_0})$. If $R$ is the zero ring,
there are no rational points, and we take $D=0$. Otherwise Noether
normalization gives a finite injective $k_0$-algebra map
$$
A_0=k_0[t_1,\ldots,t_s]\longrightarrow R.
$$
An integral extension preserves Krull dimension, so
$s=\dim R\le1$. Choose $D$ generators of $R$ as an $A_0$-module.

For $K=k_n$, restriction gives a map from the $k_0$-algebra maps
$R\to K$ to the $k_0$-algebra maps $A_0\to K$. There are at most
$(\#K)^s$ maps of the latter kind, since they are determined by the
images of the variables. Each fibre has at most $D$ elements: the
value vectors of its maps on the chosen module generators are
linearly independent in $K^D$. Indeed, the values on the generators
recover the whole map by a fixed $K$-linear map, and distinct
multiplicative characters are linearly independent. This is the
bound `finite_ringHom_comp_eq_and_natCard_le`; summing over the
fibres gives `natCard_algHom_le_mul_natCard_algHom`.

The rational points of $U_0$ inject into the $k_0$-algebra maps
$R\to K$, by `AlgebraicGeometry.Scheme.Hom.exists_injective_fieldPoints_algHom`.
Consequently
$$
\#U_0(k_n)\le D(\#k_n)^s\le Dq^n.
$$

For the second assertion take $A=D$. There are no closed points of
degree zero. If $e\ge1$, the point-counting formula
`AlgebraicGeometry.Scheme.Hom.pointCount_eq_sum` expresses
$\#U_0(k_e)$ as the sum of the degrees of all closed points whose
degrees divide $e$. Every point of $T$ of degree $e$ contributes
$e\ge1$ to this sum, so their number is at most
$\#U_0(k_e)\le Dq^e$.

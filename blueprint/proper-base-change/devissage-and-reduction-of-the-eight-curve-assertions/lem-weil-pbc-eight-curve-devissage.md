+++
id = "lem-weil-pbc-eight-curve-devissage"
kind = "lemma"
title = "Short-exact devissage for the eight assertions"
order = 1154
lean = ["AlgebraicGeometry.Etale.CurveCoefficientPair.EightAssertions.of_shortExact"]
uses = ["def-weil-pbc-eight-curve-assertions-detailed"]
+++
Let

$$
 0\longrightarrow F_1\longrightarrow F\longrightarrow F_2
 \longrightarrow0
$$

be exact in $\Ab(C_{\Et})$. If $\mathcal C(C,F_1)$ and $\mathcal C(C,F_2)$
hold in the sense of [def-weil-pbc-eight-curve-assertions-detailed], then
$\mathcal C(C,F)$ holds. In particular, the class of torsion sheaves
satisfying all eight implications is closed under extensions.

## Proof

For $1\leq j\leq7$, the assertion $\mathcal C_j$ is preserved by short exact
sequences: the long exact cohomology sequences of $0\to F_1\to F\to F_2\to0$
and the five lemma pass the vanishing statements (C1)--(C3) to $F$, give
finiteness of the middle group in (C4) and (C5) (cokernels and kernels of maps
of finite groups are finite), and give the isomorphism statements (C6) and
(C7) once the pullback maps $\rho^q_{k'/k}$ form a natural map of the two long
exact sequences.

For (C8), fix any open immersion $a:U\hookrightarrow C$ and a class $b\in
H^2(U,a^{-1}F)$. Denote its image in $H^2(U,a^{-1}F_2)$ by $b_2$. Assertion
(C8) for $F_2$ gives $c_2\in H^2(C,F_2)$ with $a^*c_2=b_2$. The obstruction to
lifting $c_2$ to $H^2(C,F)$ lies in $H^3(C,F_1)$, which is zero by (C1) for
$F_1$. Choose a lift $c\in H^2(C,F)$. Naturality of the long exact sequences
under restriction shows that $b-a^*c$ maps to zero in $H^2(U,a^{-1}F_2)$.
Exactness therefore gives $b_1\in H^2(U,a^{-1}F_1)$ whose image is $b-a^*c$.
Apply (C8) for $F_1$ to choose $c_1\in H^2(C,F_1)$ restricting to $b_1$. If
$\iota_*:H^2(C,F_1)\to H^2(C,F)$ is induced by $F_1\hookrightarrow F$, then

$$
 a^*(c+\iota_*c_1)=a^*c+(b-a^*c)=b.
$$

This proves (C8) for $F$, without a hypothesis on the components of $U$. Thus
$\mathcal C(C,F)$ holds.

Unresolved dependencies: def:weil-pbc-etale-sheaves

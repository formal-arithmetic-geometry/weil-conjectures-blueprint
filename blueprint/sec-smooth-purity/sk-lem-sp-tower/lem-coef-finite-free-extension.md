+++
id = "lem-coef-finite-free-extension"
kind = "lemma"
title = "Finite free coefficient extensions and cofinal levels"
order = 2487
uses = ["cor-coef-finite-verdier", "def-coefficient-twists-detailed", "def-weil-derived-pullback-tensor-hom", "lem-coef-finite-closed-shriek", "lem-coef-finite-direct-image", "lem-coef-finite-dualizing", "thm-coef-finite-hom"]
+++
Let $E\subset L$ be a finite extension of coefficient fields,
with ramification index $e$. For every $n\geq1$, put

$$
A=\mathcal O_E/\pi_E^n,\qquad
B=\mathcal O_L/\pi_E^n\mathcal O_L
=\mathcal O_L/\pi_L^{en}=A_{L,en}.
$$

Equality here is equality of ideals; a unit relating the chosen
uniformizers does not change the quotient. The coefficient ring
$B$ is finite free over $A$. For finite-Tor constructible
complexes the canonical maps give isomorphisms

$$
\begin{aligned}
(Rf_{*,A}K)\otimes_A B&\cong Rf_{*,B}(K\otimes_A B),\\
(Ri_A^!M)\otimes_A B&\cong Ri_B^!(M\otimes_A B),\\
\omega_{X,A}\otimes_A B&\cong\omega_{X,B},\\
R\mathcal Hom_A(K,M)\otimes_A B
&\cong R\mathcal Hom_B(K\otimes_A B,M\otimes_A B),\\
(D_{X,A}K)\otimes_A B&\cong D_{X,B}(K\otimes_A B).
\end{aligned}
$$

They respect evaluation, double-dual maps and the adjunction
counits, are compatible with further finite coefficient-field
extension, and commute with coefficient reduction. Their formation
is natural under scheme isomorphisms, in particular Frobenius.
Thus the levels $en$ give the coefficient comparisons on a
cofinal subsystem of the $\mathcal O_L$-adic tower.

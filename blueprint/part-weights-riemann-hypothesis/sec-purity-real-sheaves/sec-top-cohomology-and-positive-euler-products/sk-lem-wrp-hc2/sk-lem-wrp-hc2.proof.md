+++
kind = "proof"
of = "sk-lem-wrp-hc2"
+++
Both formulas come from the description of a lisse sheaf by its
representation, and Poincaré duality reduces $H^2_c$ to $H^0$. The
weights are then read off from the stalks. The sections of a local
system are the invariant vectors of its fibre, which gives the first
formula. By degreewise Poincaré
duality (Corollary [sk-thm-derived-duality]) we have

$$
H_c^2(U,\mathcal F)^\vee
=H^0(U,\mathcal F^\vee(1))=(V^\vee)^{\pi_1(U)}(1).
$$

Since the dual of $(V^\vee)^{\pi_1(U)}$ is $V_{\pi_1(U)}$, this gives the second
formula, with its twist. The identification is induced by the
canonical duality pairing and is therefore Frobenius equivariant.

The same duality gives the vanishing outside degrees $0,1,2$, which
for torsion coefficients is the bound on cohomological dimension in
Appendix [sec-curve-estimates]. For
$i<0$ there is nothing to prove, and for $i>2$ the space
$H_c^i(U,\mathcal F)$ is dual to $H^{2-i}(U,\mathcal F^\vee(1))$,
which is zero because $2-i<0$.

Suppose that $U_0$ is affine, and choose a smooth proper completion of
$U$. Its boundary is nonempty, because a connected proper curve has
only constant global functions and hence is not affine. A compactly
supported section extends by zero to the completion, so it vanishes
on a neighbourhood of the boundary. Since a section of a lisse sheaf
on a connected curve is determined by its generic value, the section
is zero. Thus $H_c^0(U,\mathcal F)=0$.

The action of $W(U_0)$ on $V^{\pi_1(U)}$ and $V_{\pi_1(U)}$ factors through the degree
quotient. If $\beta$ is an eigenvalue of the operator of degree one,
then $\beta^{\deg(x)}$ is an eigenvalue of $\operatorname{Frob}_x$ on
$\mathcal F_{\bar x}$ for every closed point $x$. Indeed, $V^{\pi_1(U)}$
is a subspace and $V_{\pi_1(U)}$ a quotient of $V\simeq\mathcal F_{\bar x}$,
both stable under $\operatorname{Frob}_x\in\pi_1(U)s^{\deg(x)}$, which
acts on them as $s^{\deg(x)}$. If $\mathcal F$ is punctually of
weights $\le a$, this implies $|\iota(\beta)|\le q^{a/2}$, and purity implies
equality.
Finally, the twist $(-1)$ multiplies each global eigenvalue by $q$,
which gives the stated weights for $H_c^2$.

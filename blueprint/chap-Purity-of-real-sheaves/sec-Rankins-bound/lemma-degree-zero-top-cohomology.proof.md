+++
kind = "proof"
of = "lemma-degree-zero-top-cohomology"
order = 1151
uses = ["proposition-lattices-representations-normal-scheme", "corollary-degreewise-duality-over-fields", "definition-weights", "lemma-filtrations-spectra", "lemma-proper-smooth-model", "lemma-degree-zero-top-cohomology--1", "lemma-degree-zero-top-cohomology--2", "lemma-degree-zero-top-cohomology--3", "lemma-degree-zero-top-cohomology--4", "lemma-degree-zero-top-cohomology--5", "lemma-degree-zero-top-cohomology--6", "lemma-degree-zero-top-cohomology--7"]
+++
We deduce both formulas from the description of a lisse sheaf by its
representation, using Poincaré duality to reduce $H^2_c$ to $H^0$, and
then we read off the weights from the stalks.

A global section of a local system is determined by its value at
$\bar\eta$, and a vector of the fibre extends to a global section
exactly when it is fixed by the monodromy. This is the first
formula.  For the second, by degreewise Poincaré
duality (Corollary [corollary-degreewise-duality-over-fields]) we have

$$
H_c^2(U,\mathcal F)^\vee
=H^0(U,\mathcal F^\vee(1))=(V^\vee)^{\pi_1(U)}(1).
$$

Since the dual of $(V^\vee)^{\pi_1(U)}$ is $V_{\pi_1(U)}$, this gives the second
formula, with its twist. Moreover, the identification is induced by the
canonical duality pairing and is therefore Frobenius equivariant.

Duality also gives the vanishing outside degrees $0,1,2$. Indeed, for
$i<0$ there is nothing to prove, and for $i>2$ the space
$H_c^i(U,\mathcal F)$ is dual to $H^{2-i}(U,\mathcal F^\vee(1))$,
which is zero because $2-i<0$. For torsion coefficients the vanishing comes instead from the bound on cohomological dimension of
Appendix [chap-Cohomology-of-torsion-sheaves-on-curves].

Suppose that $U_0$ is affine, and choose a smooth proper completion of
$U$. Its boundary is nonempty, because a connected proper curve has
only constant global functions and hence is not affine. A compactly
supported section extends by zero to the completion, so it vanishes
on a neighbourhood of the boundary. Since a section of a lisse sheaf
on a connected curve is determined by its generic value, the section
is zero, and $H_c^0(U,\mathcal F)=0$.

For the weights we compare the global Frobenius on these two spaces
with the local Frobenius at a closed point. Since $\pi_1(U)$ acts
trivially on $V^{\pi_1(U)}$ and on $V_{\pi_1(U)}$, the action of $W(U_0)$
on them factors through the degree quotient.  If $\beta$ is an eigenvalue of the operator of degree one,
then $\beta^{\deg(x)}$ is an eigenvalue of $\operatorname{Frob}_x$ on
$\mathcal F_{\bar x}$ for every closed point $x$. Indeed, $V^{\pi_1(U)}$
is a subspace and $V_{\pi_1(U)}$ a quotient of $V\simeq\mathcal F_{\bar x}$,
both stable under $\operatorname{Frob}_x\in\pi_1(U)s^{\deg(x)}$, which
acts on them as $s^{\deg(x)}$.  If $\mathcal F$ is punctually of
weights $\le a$, it follows that $|\iota(\beta)|\le q^{a/2}$, and if $\mathcal F$
is pure of weight $a$, equality holds.
Finally, the twist $(-1)$ multiplies each global eigenvalue by $q$,
which gives the stated weights for $H_c^2$.

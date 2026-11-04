+++
id = "prose-10-19"
kind = "hidden"
title = "Weil complexes (1)"
order = 868
+++
The Weil conjectures concern varieties over $\mathbf F_q$, while the six
operations of Part I live on schemes over the algebraic
closure. On $X=X_0\times_{\mathbf F_q}k$, what remains of a variety $X_0$
over $\mathbf F_q$ is an action of Frobenius on $X$ and on every
complex pulled back from $X_0$.

Here $k_0=\mathbf F_q$ and $k$ is an algebraic closure of
$k_0$. The geometric Frobenius
$\sigma\in\operatorname{Gal}(k/k_0)$ is the inverse of the arithmetic
Frobenius $a\mapsto a^q$. For a scheme $T$ of the form
$T_0\times_{k_0}k$, with $T_0$ over $k_0$, let

$$
\operatorname{Fr}_T:T\longrightarrow T
$$

be the semilinear automorphism induced by $\sigma$. It is a morphism of
schemes covering the automorphism $\operatorname{Spec}(\sigma)$ of
$\operatorname{Spec}k$.

We use $\operatorname{Fr}_T$ to define Weil structures. We prove the trace
formula instead for the $k$-linear Frobenius
$\Phi_T=F_{T_0/k_0}\times_{k_0}k$, obtained by base change from the
relative $q$-power Frobenius of $T_0$, since its graph is a correspondence over $k$.
We compare the two in Section [sec-Frobenius-correspondences]
(Lemma [lemma-scheme-frobenius-geometric-frobenius]).

Since $\operatorname{Fr}_T$ is an automorphism of schemes, pullback of
sheaves of modules along it is exact and preserves derived completeness.
Hence for every admissible coefficient ring $\Lambda$ it induces an
autoequivalence

$$
\operatorname{Fr}_T^*:
D^b_{\mathrm{ctf}}(T,\Lambda)\longrightarrow
D^b_{\mathrm{ctf}}(T,\Lambda),
$$

which agrees with the derived inverse image along $\operatorname{Fr}_T$.

Instead of complexes on $T_0$ pulled back to
$T$, we keep only the part of that datum that the trace formula sees:
the complex on $T$, where all cohomology is computed, together with an
identification of it with its Frobenius pullback. Every construction on $T$
(direct images, $f^!$, truncations, duals) is compatible with such
identifications by base change, as we check below, so we never have to descend
anything to $T_0$.

There are also more of these pairs than complexes on $T_0$, and we use the extra
ones in Part III. For a $\mathbf Q_\ell$-sheaf on $T_0$, the stalk at a geometric point over
a closed point is a continuous representation of a Galois group. Frobenius
therefore preserves a lattice in it, and its eigenvalues are $\ell$-adic
units. On $\operatorname{Spec}k$, the sheaf $\mathbf Q_\ell$ with
Frobenius acting by $\ell$ is a pair of this kind that does not come
from $\operatorname{Spec}\mathbf F_q$. Pulled back to a scheme, such
pairs are the sheaves $\mathcal B_b$ that normalize weights in
Proposition [proposition-weights-under-usual-operations].

We require an isomorphism so that the Frobenius operator on cohomology is
invertible over a field (Theorem [theorem-poincare-duality-frobenius]).
The trace formula itself only needs a morphism
(Definition [definition-frobenius-correspondences-their-operators]), and
it is stated for these pairs
(Theorem [theorem-grothendieck-lefschetz-trace-formula]).

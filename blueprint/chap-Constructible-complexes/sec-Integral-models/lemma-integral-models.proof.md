+++
kind = "proof"
of = "lemma-integral-models"
order = 296
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "proposition-milnor-sequence", "definition-classical-pro-etale-sheaves", "proposition-comparison-morphism-inverse-image", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-constructible-sheaves", "corollary-finite-tor-amplitude-under-comparison", "lemma-inverse-image-coefficient-sheaves", "lemma-acyclic-resolutions", "proposition-sp-unique-adjoint"]
+++
In (1) and (2) we compare two coefficient sheaves related by a flat map
that is an isomorphism modulo every $\pi_E^n$, so they have the same
derived complete objects. For (3)
we use the two characterizations of integral constructibility, while for (4) we
combine the dévissage of
Corollary [corollary-coefficient-heart-b] with the lattices of
Lemma [lemma-lattices-after-finite-stratification].

(1) and (2). The map from the constant sheaf $\mathcal O_E$ to
$\mathcal O_{E,X}$ is flat and induces isomorphisms modulo every
$\pi_E^n$ [Stacks, [099L](https://stacks.math.columbia.edu/tag/099L)]. Hence by [Stacks, [099I](https://stacks.math.columbia.edu/tag/099I)] restriction of scalars
is an equivalence on derived complete objects, which is (1).
By [Stacks, [09C1](https://stacks.math.columbia.edu/tag/09C1)], an object of $\Dc(X,\mathcal O_E)$ is a derived complete
complex whose reduction modulo $\pi_E$ is constructible of finite Tor
dimension over $\mathbf F_E$. Since over the field $\mathbf F_E$ every
bounded complex has finite Tor dimension, this
description agrees with the description of $\Dbc(X,\mathcal O_E)$ in
Proposition [proposition-integral-constructibility-criterion], and
together with (1) this gives (2).

(3) By Proposition [proposition-integral-constructibility-criterion], an object of
$D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ lies in $\Dbc(X,\mathcal O_E)$ if and only if
it satisfies condition (2) there: it is derived complete with constructible
reduction modulo $\pi_E$. Equivalently, it satisfies condition (3): there is a
finite stratification such that on each stratum $S$, pro-étale locally,
$K|_S\simeq\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ for a bounded
complex $P^\bullet$ of finite free $\mathcal O_E$-modules; here the implication
from (2) to (3) is
Proposition [proposition-local-structure-integral-constructible-complexes].
For each of the three operations we therefore check whichever of these two conditions is convenient.

*Inverse image.* By Lemma [lemma-inverse-image-coefficient-sheaves], $f^*$
sends finite free $\mathcal O_{E,Y}$-modules to finite free
$\mathcal O_{E,X}$-modules, so it preserves the local description of
condition (3).

*Extension by zero.* The functor $a_!=i_*j_!$ preserves derived
completeness. Indeed, $j_!$ for a quasi-compact open immersion $j$ preserves
limits by [Stacks, [09BP](https://stacks.math.columbia.edu/tag/09BP)], and $i_*$ is exact and preserves limits by
[Stacks, [09AA](https://stacks.math.columbia.edu/tag/09AA), [09BM](https://stacks.math.columbia.edu/tag/09BM)]. Moreover, both functors commute with reduction
modulo $\pi_E$ and preserve constructibility of the reductions, so $a_!$
preserves condition (2).

*Tensor product.* Let $K,M\in\Dbc(X,\mathcal O_E)$, and choose a
stratification for $K$ as above. Derived completeness and
constructibility of the reduction modulo $\pi_E$ are both preserved by
cones, so $\Dbc(X,\mathcal O_E)$ is closed under cones. Moreover, the localization
triangles along the strata exhibit $K$ as a finite iterated extension of
the objects $a_!a^*K$, for the strata $a:S\hookrightarrow X$, and the functor
$-\otimes^{\mathbf L}M$ preserves these triangles. It therefore suffices to
show that $(a_!a^*K)\otimes^{\mathbf L}M$ lies in $\Dbc(X,\mathcal O_E)$.

For this we use the projection formula for a locally closed immersion:
for $L\in D(S_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ and $M\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$
the canonical map

$$
(a_!L)\otimes^{\mathbf L}M\longrightarrow a_!(L\otimes^{\mathbf L}a^*M)
$$

is an isomorphism. Indeed, write
$a=i\circ j$ with $j$ open and $i$ closed, so that $a_!=i_*j_!$. On $S$
the map restricts to the identity of $L\otimes^{\mathbf L}a^*M$, while on
every complementary stratum both sides restrict to zero. Since restriction to
the strata is exact and jointly conservative
by [Stacks, [09AD](https://stacks.math.columbia.edu/tag/09AD)], the map is an isomorphism.

Given the parts on inverse image and extension by zero,
we are reduced to showing that $a^*K\otimes^{\mathbf L}a^*M$ lies in
$\Dbc(S,\mathcal O_E)$. Tensoring with $a^*K$ preserves derived
completeness, because $a^*K$ is pro-étale locally a bounded
complex of finite free modules. Moreover, the reduction modulo $\pi_E$ of the
tensor product is the tensor product of the reductions, and this is constructible.

(4) For $\overline{\mathbf Q}_\ell$, we first descend to a finite $E$ by
Lemma [lemma-descent-finite-coefficient-field]. By
Corollary [corollary-coefficient-heart-b], every object of $\Dbc(X,E)$ is
obtained by finitely many cones and shifts from sheaves $a_!L$ with $L$
lisse. We refine the stratum $S$ by a finite stratification as in
Lemma [lemma-lattices-after-finite-stratification]. This replaces $a_!L$
by finitely many extensions of such sheaves, and on each new stratum $L$
contains a lattice $L_0$ with $L_0[1/\ell]=L$, so that $a_!L=(a_!L_0)[1/\ell]$.
It remains to see that $L_0$ is integrally constructible. The reduction of $L_0$ modulo $\pi_E^n$ is a locally constant sheaf of
finitely presented $\mathcal O_E/\pi_E^n$-modules, so it comes from the
étale site by [Stacks, [099Y](https://stacks.math.columbia.edu/tag/099Y)]. Thus $L_0\in\Dbc(S,\mathcal O_E)$, and
$a_!L_0\in\Dbc(X,\mathcal O_E)$ by (3).

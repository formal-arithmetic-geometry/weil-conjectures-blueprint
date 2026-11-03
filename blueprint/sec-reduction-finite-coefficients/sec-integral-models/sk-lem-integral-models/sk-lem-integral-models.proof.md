+++
kind = "proof"
of = "sk-lem-integral-models"
uses = ["sk-prop-integral-criterion", "sk-prop-integral-local-structure", "sk-prop-sfb-cartesian-coefficients", "sk-thm-sfb-qlbar-two-colimit", "sk-cor-coefficient-heart-ii", "sk-lem-stratified-lattice"]
+++
(1) and (2). The map from the constant sheaf $\mathcal O_E$ to
$\mathcal O_{E,X}$ is flat and induces isomorphisms modulo every
$\pi_E^n$ [Stacks, Tag 099L](https://stacks.math.columbia.edu/tag/099L). Hence, by [Stacks, Tag 099I](https://stacks.math.columbia.edu/tag/099I), restriction of scalars
is an equivalence on derived complete objects, which is (1).
By [Stacks, Tag 09C1](https://stacks.math.columbia.edu/tag/09C1), an object of $\Dc(X,\mathcal O_E)$ is a derived complete
complex whose reduction modulo $\pi_E$ is constructible of finite Tor
dimension over $\mathbf F_E$. Since $\mathbf F_E$ is a field, every
bounded complex has finite Tor dimension over it. Therefore this
description agrees with the description of $\Dbc(X,\mathcal O_E)$ in
Proposition [sk-prop-integral-criterion], and together with (1) we obtain
(2).

(3) By Proposition [sk-prop-integral-criterion], an object of
$D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ lies in $\Dbc(X,\mathcal O_E)$ if and only if
it is derived complete with constructible reduction modulo $\pi_E$
(condition (2)), and if and only if it admits a finite stratification such
that on each stratum $S$, pro-étale locally,
$K|_S\simeq\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ for a bounded
complex $P^\bullet$ of finite free $\mathcal O_E$-modules (condition (3)).
The implication from (2) to (3) is
Proposition [sk-prop-integral-local-structure]. For each of the three
operations we check one of these two conditions.

*Inverse image.* By Lemma [sk-prop-sfb-cartesian-coefficients], $f^*$
sends finite free $\mathcal O_{E,Y}$-modules to finite free
$\mathcal O_{E,X}$-modules, so that it preserves the local description.

*Extension by zero.* The functor $a_!=i_*j_!$ preserves derived
completeness. Indeed, $j_!$ for a quasi-compact open immersion $j$ preserves
limits by [Stacks, Tag 09BP](https://stacks.math.columbia.edu/tag/09BP), and $i_*$ is exact and preserves limits by
[Stacks, Tag 09AA](https://stacks.math.columbia.edu/tag/09AA), [Stacks, Tag 09BM](https://stacks.math.columbia.edu/tag/09BM). Both functors commute with reduction
modulo $\pi_E$ and preserve constructibility of the reductions.

*Tensor product.* Let $K,M\in\Dbc(X,\mathcal O_E)$, and choose a
stratification for $K$ as above. Derived completeness and
constructibility of the reduction modulo $\pi_E$ are both preserved by
cones, so $\Dbc(X,\mathcal O_E)$ is closed under cones. The localization
triangles along the strata exhibit $K$ as a finite iterated extension of
the objects $a_!a^*K$, for the strata $a:S\hookrightarrow X$, and
$-\otimes^{\mathbf L}M$ preserves these triangles. Hence it suffices to
show that $(a_!a^*K)\otimes^{\mathbf L}M$ lies in $\Dbc(X,\mathcal O_E)$.
For this we use the projection formula for a locally closed immersion:
for $L\in D(S_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ and $M\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$
the canonical map

$$
(a_!L)\otimes^{\mathbf L}M\longrightarrow a_!(L\otimes^{\mathbf L}a^*M)
$$

is an isomorphism. To see this, write
$a=i\circ j$ with $j$ open and $i$ closed, so that $a_!=i_*j_!$. On $S$
the map restricts to the identity of $L\otimes^{\mathbf L}a^*M$, and on
every complementary stratum both sides restrict to zero. Restriction to
the strata is exact, and these restrictions are jointly conservative
by [Stacks, Tag 09AD](https://stacks.math.columbia.edu/tag/09AD). By the parts on inverse image and extension by zero, it
therefore remains to see that $a^*K\otimes^{\mathbf L}a^*M$ lies in
$\Dbc(S,\mathcal O_E)$. Since $a^*K$ is pro-étale locally a bounded
complex of finite free modules, tensoring with it preserves derived
completeness. The reduction modulo $\pi_E$ of the tensor product is the
tensor product of the reductions, which is constructible.

(4) For $\overline{\mathbf Q}_\ell$, we first descend to a finite $E$ by
Lemma [sk-thm-sfb-qlbar-two-colimit]. By
Corollary [sk-cor-coefficient-heart-ii], every object of $\Dbc(X,E)$ is
obtained by finitely many cones and shifts from sheaves $a_!L$ with $L$
lisse. By Lemma [sk-lem-stratified-lattice], after refining the
stratum $S$ by a finite stratification (which replaces $a_!L$ by finitely
many extensions of such sheaves), $L$ contains a lattice $L_0$ with
$L_0[1/\ell]=L$, and then $a_!L=(a_!L_0)[1/\ell]$. The reduction of $L_0$
modulo $\pi_E^n$ is a locally constant sheaf of finitely presented
$\mathcal O_E/\pi_E^n$-modules, so it comes from the étale site by
[Stacks, Tag 099Y](https://stacks.math.columbia.edu/tag/099Y). Thus $L_0\in\Dbc(S,\mathcal O_E)$, hence
$a_!L_0\in\Dbc(X,\mathcal O_E)$ by (3), and the reductions of $a_!L_0$ are
bounded constructible complexes pulled back from $X_{\acute{e}t}$.

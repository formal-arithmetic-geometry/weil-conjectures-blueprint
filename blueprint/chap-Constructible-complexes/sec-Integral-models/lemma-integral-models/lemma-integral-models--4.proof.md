+++
kind = "proof"
of = "lemma-integral-models--4"
order = 294009
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-integral-models--3", "lemma-integral-models--5", "lemma-inverse-image-tensor-product--6", "proposition-sp-unique-adjoint--1"]
+++
(3) By Proposition [proposition-integral-constructibility-criterion], an object of
$D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ lies in $\Dbc(X,\mathcal O_E)$ if and only if
it satisfies condition (2) there: it is derived complete with constructible
reduction modulo $\pi_E$. Equivalently, it satisfies condition (3): there is a
finite stratification such that on each stratum $S$, pro-étale locally,
$K|_S\simeq\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ for a bounded
complex $P^\bullet$ of finite free $\mathcal O_E$-modules. The implication
from (2) to (3) is
Proposition [proposition-local-structure-integral-constructible-complexes].
For each of the three operations we check one of these two conditions.

*Inverse image.* By Lemma [lemma-inverse-image-coefficient-sheaves], $f^*$
sends finite free $\mathcal O_{E,Y}$-modules to finite free
$\mathcal O_{E,X}$-modules, so it preserves the local description of
condition (3).

*Extension by zero.* The functor $a_!=i_*j_!$ preserves derived
completeness. Indeed, $j_!$ for a quasi-compact open immersion $j$ preserves
limits by [Stacks, [09BP](https://stacks.math.columbia.edu/tag/09BP)], and $i_*$ is exact and preserves limits by
[Stacks, [09AA](https://stacks.math.columbia.edu/tag/09AA), [09BM](https://stacks.math.columbia.edu/tag/09BM)]. Both functors commute with reduction
modulo $\pi_E$ and preserve constructibility of the reductions. Hence $a_!$
preserves condition (2).

*Tensor product.* Let $K,M\in\Dbc(X,\mathcal O_E)$, and choose a
stratification for $K$ as above. Derived completeness and
constructibility of the reduction modulo $\pi_E$ are both preserved by
cones, so $\Dbc(X,\mathcal O_E)$ is closed under cones. The localization
triangles along the strata exhibit $K$ as a finite iterated extension of
the objects $a_!a^*K$, for the strata $a:S\hookrightarrow X$. The functor
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
the map restricts to the identity of $L\otimes^{\mathbf L}a^*M$. On
every complementary stratum both sides restrict to zero. Since restriction to
the strata is exact and jointly conservative
by [Stacks, [09AD](https://stacks.math.columbia.edu/tag/09AD)], the map is an isomorphism.

Given the parts on inverse image and extension by zero,
we are reduced to showing that $a^*K\otimes^{\mathbf L}a^*M$ lies in
$\Dbc(S,\mathcal O_E)$. Tensoring with $a^*K$ preserves derived
completeness, because $a^*K$ is pro-étale locally a bounded
complex of finite free modules. The reduction modulo $\pi_E$ of the
tensor product is the tensor product of the reductions, and this is constructible.

*Source:* the proof of Lemma [lemma-integral-models].

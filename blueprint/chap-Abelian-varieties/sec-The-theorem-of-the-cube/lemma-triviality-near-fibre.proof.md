+++
kind = "proof"
of = "lemma-triviality-near-fibre"
order = 1487
uses = ["lemma-acyclic-resolutions", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-triviality-fibres", "lemma-coherent-base-change-invertible-sheaves"]
+++
We want a section of $\mathcal L$ over $X\times U$, where $X=P\times Q$,
that does not vanish on the fibre over $t$. Its zero locus then misses a
neighbourhood of that fibre. Such a section exists as soon as
$f_*\mathcal L$ is free of rank one near $t$, with formation compatible
with passage to the fibre.

To get this, we represent $Rf_*\mathcal L$, and the pushforwards of the
restrictions of $\mathcal L$ to the two slices, by complexes of free
modules whose differentials vanish at $t$. By the Künneth formula,
restriction from $H^1$ of the fibre to $H^1$ of the two slices is an
isomorphism. This forces the first differential of $Rf_*\mathcal L$ to
vanish after shrinking $T$. Then $H^0$ of $Rf_*\mathcal L$ is free of
rank one, as we need.

*Setup.* Since $X_{\bar k}=P_{\bar k}\times Q_{\bar k}$ is a
product of integral varieties, $X$ is geometrically integral
[Stacks, [05P3](https://stacks.math.columbia.edu/tag/05P3)]. We may assume that $T=\operatorname{Spec}R$ is affine,
and we let $\mathfrak p$ be the prime of $t$. Below, “shrinking $T$”
means replacing $R$ by $R_g$ for some $g\notin\mathfrak p$; everything
already constructed survives this. Consider the projections

$$
f:X\times T\to T,\qquad f_1:P\times T\to T,\qquad f_2:Q\times T\to T,
$$

and the restrictions $\mathcal L_1$ and $\mathcal L_2$ of $\mathcal L$ to
$P\times q_0\times T$ and $p_0\times Q\times T$, which are trivial. The complexes $E=Rf_*\mathcal L$ and
$E_i=Rf_{i*}\mathcal L_i$ are perfect, and their formation commutes
with base change [Stacks, [0B91](https://stacks.math.columbia.edu/tag/0B91)]. Restriction of sections gives a map
$E\to E_1\oplus E_2$, also compatible with base change.
Since $T$ is affine, $H^0(X\times T,\mathcal L)=H^0(E)$ and likewise for
$E_i$.

*Minimal complexes.* A perfect complex over a local ring can be
represented by a complex of free modules whose differentials vanish
modulo the maximal ideal; the ranks are then the dimensions of the
cohomology of the fibre. We use this to read off the ranks from the
fibre over $t$, where everything is trivial. To do so, put $h^j=\dim H^j(X_t,\mathcal O)$ and
$h_i^j=\dim H^j$ of $\mathcal O$ on the fibres $P_t$ and $Q_t$. Since
$\mathcal L$ is trivial on $X_t$ and the $\mathcal L_i$ are trivial,
$E\otimes^{\mathbf L}_R\kappa(t)$ and $E_i\otimes^{\mathbf L}_R\kappa(t)$
have cohomology of dimensions $h^j$ and $h_i^j$, with $h^0=h_i^0=1$.
After shrinking $T$ we may therefore represent $E$ and $E_i$ by
complexes of finite free modules

$$
R\xrightarrow{d}R^{h^1}\to R^{h^2}\to\cdots,\qquad
R\xrightarrow{d_i}R^{h_i^1}\to R^{h_i^2}\to\cdots
$$

whose differentials vanish modulo $\mathfrak p$ [Stacks, [0BCD](https://stacks.math.columbia.edu/tag/0BCD)]. We
represent the map $E\to E_i$ by a map of complexes [Stacks, [064B](https://stacks.math.columbia.edu/tag/064B)], with
components $a_i:R\to R$ in degree $0$ and $b_i:R^{h^1}\to R^{h_i^1}$ in
degree $1$. Since the differentials vanish modulo $\mathfrak p$, the map
$b_i\otimes\kappa(t)$ is the restriction map on $H^1$ of the fibre
over $t$.

We want to show that $d=0$ after shrinking $T$, since then
$H^0(E)=\ker d=R$ is free of rank one. The maps $b_i$ will let us
transfer this question to the $d_i$, which are easier because
$\mathcal L_i$ is trivial.

*The differentials $d_i$ vanish.* Fix a trivialization
$\mathcal L_1\simeq\mathcal O$, and let $u\in H^0(E_1)=\ker d_1\subset R$
be the section corresponding to $1$. Its image in
$H^0(E_1\otimes^{\mathbf L}\kappa(t))=H^0(P_t,\mathcal O)$ is $1\ne0$,
so $u\notin\mathfrak p$. Since $d_1(u)=u\,d_1(1)=0$, after inverting
$u$ we get $d_1=0$. The same argument gives $d_2=0$.

*The differential $d$ vanishes.* This step uses the two slices
together. If the map $(b_1,b_2)$ is an isomorphism, then $d$ is
determined by $d_1$ and $d_2$, and this condition can be checked on
the fibre. The map $(b_1,b_2)\otimes\kappa(t)$ is restriction from
$H^1(P_t\times Q_t,\mathcal O)$ to the slices $P_t\times q_0$ and
$p_0\times Q_t$. It is an isomorphism by
Lemma [lemma-h-1-structure-sheaf-product], and in particular
$h^1=h_1^1+h_2^1$. Hence the square matrix $(b_1,b_2)$ has determinant
outside $\mathfrak p$. After inverting this determinant, $(b_1,b_2)$ is
an isomorphism. Since the maps form a map of complexes, we have
$b_i\circ d=d_i\circ a_i=0$, and therefore $d=0$.

*Conclusion.* A generator of $H^0$ gives the trivialization. We
have $H^0(X\times T,\mathcal L)=H^0(E)=\ker d=R$, and
its generator $\sigma$ maps to a generator of
$H^0(E\otimes^{\mathbf L}\kappa(t))=H^0(X_t,\mathcal L_t)$. Since
$\mathcal L_t\simeq\mathcal O_{X_t}$ and $H^0(X_t,\mathcal O)=\kappa(t)$,
the section $\sigma$ vanishes nowhere on $X_t$. Its zero locus is
closed in $X\times T$ and disjoint from $X_t$. Since $f$ is proper,
its image in $T$ is a closed set not containing $t$. On the complement
$U$ of this image, $\sigma$ trivializes $\mathcal L$.

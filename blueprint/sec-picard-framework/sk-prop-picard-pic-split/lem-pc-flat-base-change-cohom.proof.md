+++
kind  = "proof"
of    = "lem-pc-flat-base-change-cohom"
+++
*The comparison map and the reduction to cohomology.* The unit
$\mathcal F\to g'_*g'^*\mathcal F=g'_*\mathcal F'$ induces
$R\Gamma(X,\mathcal F)\to R\Gamma(X,g'_*\mathcal F')=R\Gamma(X',\mathcal F')$
(the morphism $g'$ is affine, so $g'_*$ is exact on quasi-coherent modules), an
$A$-linear map into a complex of $B$-modules; by adjunction it gives a
$B$-linear map $R\Gamma(X,\mathcal F)\otimes_AB\to R\Gamma(X',\mathcal F')$ in
$D(B)$. Since $B$ is flat over $A$, $H^i(K\otimes_AB)=H^i(K)\otimes_AB$ for
every complex $K$ of $A$-modules (see below). So the map is an isomorphism in
$D(B)$ as soon as the induced maps
$H^i(X,\mathcal F)\otimes_AB\to H^i(X',\mathcal F')$ are bijective for all $i$,
which is what the following two steps show; conversely, taking $H^i$ of the
derived isomorphism gives the degreewise statement.

*The case $X$ separated.* Let $A\to B$ be flat and let
$X$ be quasi-compact and separated over $A$; choose a finite affine
open covering $\mathcal U:X=U_1\cup\dots\cup U_t$. The base changes
$(U_i)_B$ are affine and form a cover $\mathcal U_B$ of
$X_B=X\times_{\operatorname{Spec} A}\operatorname{Spec} B$ (open affine subschemes of the base
change; separability of $X_B$ follows from that of $X$), and the
intersections are affine. By [lem-pc-cech-computes],

$$
H^p(X,\mathcal{F})=\check H^p(\mathcal U,\mathcal{F}),\qquad
H^p(X_B,\mathcal{F}_B)=\check H^p(\mathcal U_B,\mathcal{F}_B).
$$

For a multi-index $J$ with $U_J=\operatorname{Spec}(C)$ and $\mathcal{F}|_{U_J}=\widetilde M$,
the base change $(U_J)_B=\operatorname{Spec}(C\otimes_AB)$ carries
$\mathcal{F}_B|=\widetilde{M\otimes_AB}$ and the localization
identifications give
$\mathcal{F}(U_J)\otimes_AB=\mathcal{F}_B((U_J)_B)$; consequently

$$
\check C^\bullet(\mathcal U_B,\mathcal{F}_B)
=\check C^\bullet(\mathcal U,\mathcal{F})\otimes_AB .
$$

For a flat ring map $A\to B$ and any complex $C^\bullet$ of
$A$-modules,

$$
H^i(C^\bullet\otimes_AB)=H^i(C^\bullet)\otimes_AB:
$$

the proof is by induction on the number of terms (via the
truncations $0\to C^{\ge n+1}\to C^{\ge n}\to C^n[-n]\to0$ and the
five-lemma applied to the long exact sequences of the short exact
sequences, both for $C^\bullet$ and for $C^\bullet\otimes_AB$ – the
base changed sequences are exact because $A\to B$ is flat, so no
$\mathrm{Tor}_1$-terms occur). Combining gives the claim for separated $X$.

*The case $X$ quasi-separated.* Take a finite affine
open covering $\mathcal U$ of $X$ (quasi-compactness) and use the
Cech-to-cohomology spectral sequence
([lem-sc-cech-spectral]): with
$\underline H^q=\underline H^q(\mathcal{F})$,

$$
E_2^{p,q}=\check H^p(\mathcal U,\underline H^q(\mathcal{F}))
\Longrightarrow H^{p+q}(X,\mathcal{F}).
$$

The intersections $U_{i_0\dots i_p}$ are quasi-compact and separated,
so by the separated case

$$
\check H^p(\mathcal U_B,\underline H^q(\mathcal{F}_B))
=\check H^p(\mathcal U,\underline H^q(\mathcal{F}))\otimes_AB .
$$

The abutment follows from $A\to B$ flat (the spectral sequences and
their base changes are compatible in the sense that the filtration
pieces of $H^n$ base-change and are the base changes of the filtration
pieces of $H^n(X,\mathcal{F})$; the two filtrations have the same lengths and
the identification of the graded pieces gives the identification of
the filtered objects at each degree). This proves the claim in general.

*The dimension formula.* Apply the above to $A=k$, $B=K$ (a field
extension is flat): $H^i(X_K,\mathcal F_K)\cong H^i(X,\mathcal F)\otimes_kK$,
and $\dim_K(V\otimes_kK)=\dim_kV$ for every $k$-vector space $V$.

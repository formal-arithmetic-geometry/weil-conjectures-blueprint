+++
kind = "proof"
of = "proposition-proper-base-change-projective-line--1"
order = 380003
uses = ["definition-derived-base-change-map", "definition-torsion-sheaves", "prose-04-28", "proposition-cohomology-p-1-over-henselian", "lemma-extension-separably-closed-ground-field", "lemma-cohomology-modules-underlying-abelian"]
+++
First let $F$ be a torsion sheaf of $\Lambda$-modules and let $q\geq0$.
For $t\in T$, put $s=g(t)$ and choose algebraic closures $k_s$ and
$k_t$ of the residue fields, together with an embedding
$k_s\hookrightarrow k_t$ extending the residue field map. These give
compatible geometric points $\bar s$ and $\bar t$. The strict
localization stalk formula in [prose-04-28], followed by
[proposition-cohomology-p-1-over-henselian], identifies the stalk at
$\bar t$ of

$$
g^*R^q\pi_*F\longrightarrow R^q\pi'_*g'^*F
$$

with the pullback map

$$
H^q(\mathbf P^1_{k_s},F|)\longrightarrow
H^q(\mathbf P^1_{k_t},F|).
$$

The identifications commute with these maps: first compare the exchange
map with the exchange for the induced local map of strict localizations,
then restrict to the closed fibres. For the algebraic closures used here,
the comparison with the residue fields of the strict localizations also
uses topological invariance under purely inseparable extensions.
Cohomology is taken on the underlying abelian sheaves, as in
[lemma-cohomology-modules-underlying-abelian]. The field-extension map is
an isomorphism by [lemma-extension-separably-closed-ground-field], since
$\mathbf P^1_{k_s}$ is a proper curve. Geometric stalks detect
isomorphisms, so the degree-$q$ exchange map is an isomorphism.

Place $F$ in degree zero. In nonnegative degrees, the cohomology maps of
the derived base change map are the exchange maps just considered. In
negative degrees both sides vanish, since inverse image is exact and
derived direct image is left $t$-exact. Thus the derived base change map
is an isomorphism for $F[0]$, and hence also for every shift of $F$.

For a bounded below complex $K$ with torsion cohomology, fix a degree
$m$. Both functors $g^*R\pi_*$ and $R\pi'_*g'^*$ send $D^{\geq m+1}$
into $D^{\geq m+1}$. The truncation triangle therefore identifies the
comparison in degree $m$ for $K$ with that for the bounded complex
$\tau_{\leq m}K$. Induction on its cohomological length, using the
truncation triangles and the five lemma, reduces to its shifted
cohomology sheaves. These are torsion, so the preceding case applies.
The comparison is an isomorphism in every degree, as required.

+++
id = "prose-06-02"
kind = "hidden"
title = "Compactness of constructible complexes"
order = 266
+++
We begin with the first hypothesis of Brown representability, compactness,
for $\Lambda=E$ or $\overline{\mathbf Q}_\ell$. This $\Lambda$ is fixed until the end of
Section [sec-compactness]. Since $D^b_{\mathrm{ctf}}(X,\Lambda)=\Dbc(X,\Lambda)$, the
bounded constructible complexes are the proposed compact generators, and
we may use truncations and the constructible heart, which is abelian by
Lemma [sk-lem-coefficient-heart].
Without decoration, $\Hom$ and $\Ext$ are taken in $D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, also when both
arguments are constructible sheaves. A subscript indicates the coefficient
ring where it changes, as in the lattice arguments over $\mathcal O_E$.

For a constructible sheaf $C$ and a family $(K_\lambda)$ of objects of
$\Loc(\Dbc(X,\Lambda))$, we have to show that
$\bigoplus_\lambda\Hom(C,K_\lambda)\to\Hom(C,\bigoplus_\lambda K_\lambda)$
is bijective. The case of bounded constructible complexes then follows by
dévissage. We use two facts. First, $\Ext^q(C,-)$ commutes with filtered colimits of
complexes that vanish below a fixed degree, in particular of sheaves
(Lemma [sk-lem-constructible-ext-continuity], proved in
Section [sec-ext-continuity]). Second, $\Ext^q(C,N)=0$ for
$q>d_C$, with $d_C$ independent of the constructible sheaf $N$
(Lemma [sk-lem-uniform-constructible-ext] below). The second fact is needed
for unbounded targets, whose summands $K_\lambda$ may have cohomology in
unboundedly many degrees.

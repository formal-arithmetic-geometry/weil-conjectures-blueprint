+++
kind  = "proof"
of    = "prop-weil-pbc-p1-acyclicity"
+++
For $q>1$, $X=\mathbf P^1_A$ has affine diagonal and is covered by two affine
opens, so [lemma-weil-pbc-injective-restriction-acyclicity] gives the vanishing.
Let $\xi\in H^1(X_0,I_0)$. By [lemma-weil-pbc-h1-constructible-representation],
$\xi$ is the image of a tuple of classes in
$\bigoplus_iH^1(X_0,(h_i)_*\underline{M_i}|_{X_0})$, where each $h_i:V_i\to X$
is finite and finitely presented. [lemma-weil-pbc-finite-direct-image-exact] and
[lemma-weil-pbc-finite-exchange] identify this group with
$\bigoplus_iH^1((V_i)_0,\underline{M_i})$. Each $V_i$ is proper over $A$, so
[lemma-weil-pbc-h1-torsor-comparison] lifts every component to
$H^1(V_i,\underline{M_i})$, and finite Leray assembles their sum into a class
of $H^1(X,\bigoplus_i(h_i)_*\underline{M_i})$. Its image in $H^1(X,I)$
vanishes because $I$ is injective, and the restriction square is commutative,
so $\xi=0$.

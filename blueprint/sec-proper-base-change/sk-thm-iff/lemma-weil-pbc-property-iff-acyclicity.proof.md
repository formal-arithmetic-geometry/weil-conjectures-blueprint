+++
kind  = "proof"
of    = "lemma-weil-pbc-property-iff-acyclicity"
uses = ["def-weil-pbc-injective-acyclicity-property", "def-weil-pbc-derived-exchange", "lemma-weil-pbc-leray-acyclicity", "lemma-weil-pbc-proper-underived-exchange", "lemma-weil-pbc-prime-torsion-devissage"]
+++
Suppose $\mathrm{PBC}(f)$ holds. Restriction of scalars along
$\mathbf Z\to\mathbf F_r$ is exact and conservative, commutes with inverse and
direct images and with derived direct images (an injective sheaf of
$\mathbf F_r$-modules has no higher cohomology as an abelian sheaf), and a
complex of sheaves of $\mathbf F_r$-modules has torsion cohomology; so it
carries the exchange morphism over $\mathbf F_r$ to the one over $\mathbf Z$, and
$\mathrm{PBC}(f)$ gives the base change property with $\mathbf F_r$-coefficients.
If $I$ is injective among $\mathbf F_r$-module sheaves, then $Rf_*I=f_*I$; after
arbitrary base change, this base change property identifies $Rf'_*g'^{-1}I$ with
the degree-zero complex $g^{-1}f_*I$, so $R^qf'_*g'^{-1}I=0$ for $q>0$, which is
$\mathrm{IA}_r(f)$ by [def-weil-pbc-injective-acyclicity-property].

Conversely assume $\mathrm{IA}_r(f)$ for every prime $r$. Fix $r$ and
$K\in\Dplus(X_{\Et},\mathbf F_r)$, and represent $K$ by a bounded below complex
$I^\bullet$ of injective sheaves of $\mathbf F_r$-modules. Then
$g^{-1}f_*I^\bullet$ computes $g^{-1}Rf_*K$. The terms of $g'^{-1}I^\bullet$
are $f'_*$-acyclic by $\mathrm{IA}_r(f)$, so by
[lemma-weil-pbc-leray-acyclicity] $f'_*g'^{-1}I^\bullet$ computes
$Rf'_*g'^{-1}K$. Under these identifications the derived exchange morphism of
[def-weil-pbc-derived-exchange] is the underived proper exchange
$g^{-1}f_*I^\bullet\to f'_*g'^{-1}I^\bullet$ of
[lemma-weil-pbc-proper-underived-exchange], an isomorphism in every degree.
So the base change property holds with $\mathbf F_r$-coefficients.

Now let $E$ be an abelian sheaf on $X_{\Et}$ killed by a prime $r$. Then $E$ is
the restriction of scalars of an $\mathbf F_r$-module sheaf, and restriction of
scalars carries the exchange morphism over $\mathbf F_r$ to the one over
$\mathbf Z$ (see the first paragraph); hence $\Ex^q_{\square,E}$ is an
isomorphism for every $q$. Since proper maps are quasi-compact and
quasi-separated, the prime-torsion devissage
[lemma-weil-pbc-prime-torsion-devissage] shows that $\Ex^q_{\square,F}$ is an
isomorphism for every $q$ and every torsion sheaf $F$. For
$K\in\Dplus(X_{\Et})$ with torsion cohomology, induction on the
length of the canonical truncations of $K$ (both $g^{-1}Rf_*$ and $Rf'_*g'^{-1}$
are triangulated and send $D^{\geq N}$ into $D^{\geq N}$) shows that
$\Ex_{\square,K}$ is an isomorphism in every degree. This proves (1).

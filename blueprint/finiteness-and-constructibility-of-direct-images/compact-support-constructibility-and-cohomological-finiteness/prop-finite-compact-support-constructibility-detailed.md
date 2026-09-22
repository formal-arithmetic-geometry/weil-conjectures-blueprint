+++
id = "prop-finite-compact-support-constructibility-detailed"
kind = "theorem"
title = "Finite-level bounded constructibility for proper support"
order = 5821
tags = ["latex:proposition"]
lean = ["AlgebraicGeometry.Etale.derivedPushforwardCompactSupport_mapsTo_Dbc"]
uses = ["def-compact-support-direct-image", "sbc-thm-finiteness-finite-type"]
+++
Let $K_0$ be a field, let $X,Y$ be finite-type $K_0$-schemes, and let
$f:X\to Y$ be a separated finite-type $K_0$-morphism. Fix a prime $\ell$,
write $\Ql=\mathbf Q_\ell$, and require that its image in $K_0$ is
invertible. Choose a finite extension $E/\Ql$, an integer
$n\in\mathbf Z_{\geq1}$, and put $A=A_{E,n}$. Let $Rf_{!,n}$ be the coherent
finite-level compact-support direct image functor associated to the
compactification candidates. The comparison maps for refinements are
identities and satisfy the cocycle condition, and $\Dbc(X,A)$ uses
finite-torsion constructibility. For $a,b\in\mathbf Z$ with $a\leq b$, write
$$
D_c^{[a,b]}(X,A)=\{K\in\Dbc(X,A):\mathcal H^r(K)=0\text{ for }r\notin[a,b]\}.
$$

The ambient derived direct-image functor $Rf_{!,n}$ restricts to an exact
triangulated functor
$$
Rf_{!,n}:\Dbc(X,A_{E,n})\longrightarrow\Dbc(Y,A_{E,n}).
$$
For each cohomological interval $[a,b]$ with $a,b\in\mathbf Z$ and
$a\leq b$, and each integer $e\geq0$ such that every geometric fibre of $f$
has dimension at most $e$, there are integers $a'\leq b'$, independent of
the compactification, such that for every
$K\in D_c^{[a,b]}(X,A_{E,n})$ one has
$Rf_{!,n}K\in D_c^{[a',b']}(Y,A_{E,n})$. The restriction and its amplitude
bound commute with finite coefficient reduction.

(*Source: the finiteness of compact-support direct images of constructible
torsion sheaves: Stacks Project, More Étale Cohomology, Section 63.14,
Theorem 63.14.5, [Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0); the
fibre-dimension amplitude bounds are the finiteness bounds of the same
formalism, cf. Étale Cohomology, Lemma 59.92.2, [Tag
095U](https://stacks.math.columbia.edu/tag/095U).*)

## Proof

*Step 1 (the compactification form).* A compactification of $f$ is a
factorisation $f=\bar f\circ j$ with $j:X\hookrightarrow\bar X$ an open
immersion and $\bar f:\bar X\to Y$ proper, and the candidate attached to it
is $R\bar f_*\circ j_!$. The functor $Rf_{!,n}$ [def-compact-support-direct-image] is the coherent choice of
a candidate in the compactification category, and by the hypothesis recalled
in the statement its comparison maps are identities satisfying the cocycle
condition. It therefore suffices to bound the candidate of a single
compactification, and the bound produced below involves only the amplitude
interval of $K$ and the fibre bound $e$, so that it is independent of the
choice.

*Step 2 (transport to the étale site).* The functor is defined on the
pro-étale categories. Under the comparison morphism of sites $\nu$ the
direct images correspond,
$\nu^*Ru_{\Et,*}\cong Ru_{\Proet,*}\nu^*$, and constructibility on the
pro-étale site is by definition the inverse image of constructibility on the
étale site. It is accordingly enough to prove the assertion for the étale
direct image, which is what the two classical finiteness theorems below
provide.

*Step 3 (extension by zero and the proper case).* For $K\in\Dbc(X,A)$ the
object $j_!K$ lies in $\Dbc(\bar X,A)$ with constructible cohomology sheaves
in the same degrees: extension by zero is exact and preserves
constructibility. The geometric fibres of $\bar f$ have dimension at most
$e$, so the comparison-and-finitude theorem applies to $\bar f$: for every
constructible $A$-sheaf $F$ on $\bar X_{\Et}$ the sheaves $R^q\bar f_*F$ are
constructible and vanish for $q>2e$. For a complex whose cohomology sheaves
lie in degrees $[a,b]$ the conclusion holds degreewise, the constructible
sheaves forming a weak Serre subcategory, so that
$Rf_{!,n}K\in D_c^{[a,b+2e]}(Y,A)$.

*Step 4 (the finite-type form).* The same bound is available without
compactifying. By [sbc-thm-finiteness-finite-type], applied to the
finite-type morphism $f$ over the field $K_0$ whose geometric fibres have
dimension at most $e$, the sheaves $R^qf_!F$ are constructible for every $q$
and vanish for $q>2e$, for every constructible $A$-sheaf $F$; the case of a
complex follows as in Step 3.

*Step 5 (exactness and reduction).* The restriction is a triangulated
functor, $j_!$ and $R\bar f_*$ being exact and triangulated on the bounded
constructible categories, and it commutes with finite coefficient reduction
because the finite-level direct image does, the reduction being compatible
with the comparison morphisms that enter the definition.

Unresolved dependencies: def:weil-compact-support-candidate, def:weil-derived-direct-image, def:weil-derived-cohomology-sheaves, def:weil-constructible-intervals, def:weil-finite-torsion-constructibility, def:weil-scheme-morphism-properties, def:weil-compactifications-refinements, def:weil-extension-by-zero, def:weil-pbc-site-comparison-morphism, def:weil-pbc-constructible-direct-image-finiteness, lem:fin-extension-by-zero, lem:weil-pbc-constructible-serre, obl:fin-comparison, prop:weil-pbc-comparison-direct-image

+++
kind = "proof"
of = "theorem-smooth-base-change-classical-torsion-2"
order = 694
uses = ["theorem-comparison-direct-images", "definition-underived-base-change-map", "lemma-naturality-pasting-comparison", "theorem-smooth-base-change-classical-torsion"]
+++
We first treat a single sheaf, where the only point is $\Lambda$-linearity,
and then pass to complexes by comparing hypercohomology spectral sequences.

For a classical sheaf the assertion is
Theorem [theorem-smooth-base-change-classical-torsion], applied to the underlying
abelian sheaf, which is killed by $n$. Since the base change map is
constructed from units and counits, it is $\Lambda$-linear, and so it is an
isomorphism of $\Lambda$-module sheaves.

For a complex, we first note that by
Theorem [theorem-comparison-direct-images] and
Corollary [corollary-bounded-below-classical-complexes] the direct and
inverse images involved are classical, and that
Lemma [lemma-naturality-pasting-comparison] identifies the comparison
with (4.5). So we may argue on the étale sites.
Choose an integer $m$ with $K\in D^{\geq m}$. Since both
$g^*$ and $g'^*$ are exact, they commute with taking cohomology sheaves,
and the two sides of (4.5) are computed by the
hypercohomology spectral sequences for $Rf_*$ and $Rf'_*$, applied to $K$
and to $g'^*K$. These spectral sequences have $E_2$ terms

$$
g^*R^pf_*H^q(K),\qquad R^pf'_*g'^*H^q(K),
\qquad p\geq0,\quad q\geq m,
$$

and the base change map induces on them the comparison for sheaves, which is an
isomorphism by the preceding paragraph. Since in each total degree only
finitely many pairs $(p,q)$ occur, these shifted first quadrant
spectral sequences converge; this is where we use that $K$ is bounded
below. A map of convergent spectral sequences that is an isomorphism
on $E_2$ is an isomorphism on abutments, so the base change map induces
isomorphisms $g^*R^if_*K\to R^if'_*g'^*K$ for all $i$, and so it is an
isomorphism in the derived category.

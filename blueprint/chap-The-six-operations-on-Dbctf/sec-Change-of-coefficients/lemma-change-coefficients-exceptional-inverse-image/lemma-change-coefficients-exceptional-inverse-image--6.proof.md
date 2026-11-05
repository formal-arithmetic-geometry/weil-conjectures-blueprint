+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--6"
order = 640013
uses = ["lemma-change-coefficients-exceptional-inverse-image--4", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients-direct-image", "lemma-change-coefficients-compact-support", "definition-change-of-coefficients-maps", "theorem-nagata-s-compactification-theorem", "proposition-composition-open-restriction-compactifications-f"]
+++
Choose a compactification $f=p\circ j$. For the proper map $p$, the
categories of bounded constructible $\overline{\mathbf Q}_\ell$-complexes
on its source and target are the filtered $2$-colimits of their
categories with coefficients in finite extensions of $\mathbf Q_\ell$, as in
[proposition-dctf-x-qbar-2-colimit]. The direct-image comparisons satisfy
the cocycle condition, and their transposes between finite coefficient
fields are isomorphisms by
[lemma-change-coefficients-exceptional-inverse-image--4]. Thus
`CategoryTheory.CategoryCocone.isIso_mateEquiv_of_isFilteredTwoColimit`
shows that the exceptional comparison for $p$ and
$E\to\overline{\mathbf Q}_\ell$ is an isomorphism.

For the open immersion $j$, the exceptional inverse image is $j^*$,
whose comparison is an isomorphism. The comparison for $Rf_!$ is the
composite of those for $j_!$ and $Rp_*$. The mate of this composite is
the composite of their mates, by `CategoryTheory.mateEquiv_hcomp`.
It follows that the exceptional comparison for $f$ is an isomorphism.

+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--5"
order = 425011
uses = ["theorem-proper-base-change-classical-pro", "theorem-bounded-below-cohomology-comparison"]
+++
Choose an étale-origin witness $K\simeq\nu_X^*L$ with
$L\in D^+(X_{\acute{e}t},A)$. Apply étale proper base change to $L$, using that
the finite ring $A$ is torsion. The comparison of base change with $\nu^*$
identifies its image with the pro-étale base change map; the source and target
comparisons are isomorphisms. Transporting invertibility across these
comparisons proves the result, as in [theorem-proper-base-change-classical-pro].
The arrow identification is
`AlgebraicGeometry.ProEtale.comparison_derivedBaseChangeMap`.

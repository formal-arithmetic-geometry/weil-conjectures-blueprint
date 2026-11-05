+++
kind = "proof"
of = "theorem-smooth-base-change-all-admissible--1"
order = 700003
uses = ["theorem-smooth-base-change-classical-torsion-2", "theorem-comparison-direct-images", "lemma-naturality-pasting-comparison"]
+++
Choose $K_{\acute{e}t}$ and the isomorphism $\nu_X^*K_{\acute{e}t}\simeq K$.
Since $K_{\acute{e}t}$ is bounded, it belongs to the bounded below derived
category. Smooth base change for torsion complexes
[theorem-smooth-base-change-classical-torsion-2], in its étale form
`AlgebraicGeometry.Etale.isIso_baseChange_app_of_boundedConstructible_of_smooth`,
makes its étale base change map invertible.

The base change $f'$ of $f$ is again quasi-compact and quasi-separated.
The direct-image comparison [theorem-comparison-direct-images] and the
pullback comparison identify the source and target with the pro-étale
ones. By [lemma-naturality-pasting-comparison], these identifications carry
the inverse image of the étale map to the pro-étale map at
$\nu_X^*K_{\acute{e}t}$. Hence this map is invertible. Naturality transports
invertibility along $\nu_X^*K_{\acute{e}t}\simeq K$.

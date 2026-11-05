+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--3"
order = 865007
uses = ["theorem-poincare-duality", "proposition-six-operations-change-coefficients"]
+++
The informal argument applies Poincaré duality in degree zero over $\mathbf Z/\ell^n$, using connectedness and self-injectivity of this coefficient ring, and then extends scalars to $A$ by [proposition-six-operations-change-coefficients]. The reachable Lean trace theorem does not use this assertion: it constructs the isomorphisms with $\overline{\mathbf Q}_\ell$ coefficients directly from perfect pairings, as in [theorem-trace-isomorphism-top-degree--9].

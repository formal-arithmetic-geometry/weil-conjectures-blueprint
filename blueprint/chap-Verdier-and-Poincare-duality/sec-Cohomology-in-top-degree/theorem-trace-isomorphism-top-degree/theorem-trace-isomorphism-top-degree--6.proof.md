+++
kind = "proof"
of = "theorem-trace-isomorphism-top-degree--6"
order = 865013
uses = ["theorem-trace-isomorphism-top-degree--4", "proposition-inverting-ell", "corollary-continuity-cohomology"]
+++
Informally, write $E_X$ as the filtered union of the sheaves $\ell^{-n}\mathcal O_{E,X}$ and apply continuity to the integral vanishing bound. Lean instead passes from all compact lattices directly to $\overline{\mathbf Q}_\ell$ in [theorem-trace-isomorphism-top-degree--8]; it does not invoke a separate vanishing theorem for $E_X$.

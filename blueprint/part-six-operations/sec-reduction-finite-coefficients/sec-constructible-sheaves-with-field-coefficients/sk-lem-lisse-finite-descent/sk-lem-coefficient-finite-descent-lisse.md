+++
id = "det-lem-coefficient-finite-descent-lisse"
kind = "lemma"
title = "Descent of lisse $\\overline{\\mathbf Q}_\\ell$-sheaves and their morphisms"
lean = ["AlgebraicGeometry.ProEtale.coefficient_finite_descent_lisse"]
order = 2267
uses = ["det-lem-coefficient-finite-descent-sections"]
+++
Let $X$ be a qcqs scheme.

1. For every lisse $\QbarX$-module $L$ there are a finite $E/\mathbf Q_\ell$, a lisse $E_X$-module
   $L_E$ and an isomorphism $\QbarX\otimes_{E_X}L_E\cong L$.
2. For lisse $E_X$-modules $M,N$, the map
   $\varinjlim_{F\supseteq E}\Hom_{F_X}(M_F,N_F)\to\Hom_{\QbarX}(M_{\Qlb},N_{\Qlb})$ is bijective.

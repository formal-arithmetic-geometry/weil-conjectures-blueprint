+++
id = "prose-05-33"
kind = "hidden"
title = "Brown representability (1)"
order = 522
+++
Let $\Lambda$ be an admissible coefficient ring and fix $N$ in
[$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$](@definition-localizing-subcategory). Since the functor [$Rf_!$](@proposition-construction-independence-rf-shriek) preserves direct sums (Proposition [proposition-construction-independence-rf-shriek]),
the functor $M\mapsto\Hom(Rf_!M,N)$ turns direct sums into products. If
the objects of [$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves) are compact generators of the
[localizing category](@definition-localizing-subcategory), Brown representability produces an object $f^!N$
representing it. The next lemma checks this hypothesis for every admissible $\Lambda$; for $\mathcal O_E$ it uses the compactness proved in
Subsection [subsec-Integral-coefficients] by reduction to torsion coefficients.

Compactness enters a second time. The functor [$Rf_!$](@proposition-construction-independence-rf-shriek) also maps
[$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves) into [$D^b_{\mathrm{ctf}}(Y,\Lambda)$](@definition-constructible-sheaves), so it sends the compact
generators to compact objects. For this reason the adjoint $f^!$
preserves direct sums (Theorem [theorem-existence-exceptional-inverse-image]).

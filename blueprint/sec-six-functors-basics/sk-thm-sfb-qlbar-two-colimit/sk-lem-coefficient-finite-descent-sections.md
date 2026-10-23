+++
id = "det-lem-coefficient-finite-descent-sections"
kind = "lemma"
title = "Finitely many sections of $\\overline{\\mathbf Q}_{\\ell,X}$ lie in one $E_X$"
order = 2181
uses = ["sk-prop-sfb-qlbar-colimit-x", "det-prop-sfb-qlbar-colimit-x-invert-ell"]
+++
Let $X$ be a scheme and $V\in X_{\mathrm{proét}}$ quasi-compact.

1. For a filtered diagram of sheaves of sets (or abelian groups) $(\mathcal F_\alpha)$ on
   $X_{\mathrm{proét}}$, the natural map $\varinjlim_\alpha\mathcal F_\alpha(V)\to(\varinjlim_\alpha\mathcal F_\alpha)(V)$
   is bijective.
2. Consequently $\QbarX(V)=\bigcup_EE_X(V)$, the union over finite subextensions
   $E\subseteq\Qlb$ (the maps $E_X(V)\to\QbarX(V)$ being injective), and any finite set of
   elements of $\QbarX(V)$, or of matrices over it, lies in $E_X(V)$ for a single finite $E$.

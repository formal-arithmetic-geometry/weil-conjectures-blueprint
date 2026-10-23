+++
id = "fin2-lem-lisse-dense-open"
kind = "lemma"
title = "A lisse locus for a constructible sheaf"
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.exists_open_topologicalKrullDim_compl_lt"]
order = 3886
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-noetherian-finite-components", "sk-lem-coefficient-heart"]
+++
Let $X$ be of finite type over $k$ and let $F$ be either a
constructible
$\Lambda$-sheaf on $X_{{\mathrm{et}}}$ for a finite ring $\Lambda$, or a constructible
$\Lambda_X$-module $F\in\Cons(X,\Lambda)$ on $X_{\mathrm{proét}}$ for $\Lambda=E$ or $\Qlb$
([sk-lem-coefficient-heart]). Then there is an open
subscheme $U\hookrightarrow X$ with
$\dim(X\setminus U)<\dim X$ on which the restriction $F|_U$ is
lisse (finite locally constant, respectively locally free of finite rank for the
pro-étale topology).

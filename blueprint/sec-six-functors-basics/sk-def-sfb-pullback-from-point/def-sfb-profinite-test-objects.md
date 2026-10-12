+++
id = "def-sfb-profinite-test-objects"
kind = "definition"
title = "The test objects $X[S]$"
order = 1522
uses = ["def-sfb-profinite-to-proetale", "def-weil-pbc-proetale-site"]
lean = ["AlgebraicGeometry.ProEtale.profiniteToProEtOf"]
+++
Let $X$ be a scheme with structure morphism $\pi_X\colon X\to\Spec\Z$. The
functor
$$
u_X\colon *_{\mathrm{proét}}\longrightarrow X_{\mathrm{proét}},\qquad
S\longmapsto X[S]:=\Spec LC(S,\Z)\times_{\Spec\Z}X\to X ,
$$
is the composite of $u$ ([def-sfb-profinite-to-proetale]) with base change
$V\mapsto V\times_{\Spec\Z}X$ along $\pi_X$. If $S_i$ runs over the finite
quotients of $S$, then $X[S]=\lim_i\coprod_{S_i}X$.

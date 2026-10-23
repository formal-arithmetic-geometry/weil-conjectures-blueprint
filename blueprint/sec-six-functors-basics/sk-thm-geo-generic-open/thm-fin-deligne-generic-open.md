+++
id = "thm-fin-deligne-generic-open"
kind = "theorem"
title = "Generic bounded constructibility for an open immersion"
lean = ["AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn"]
order = 2382
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "lem-asd-smooth-generic-direct-image", "lem-fin-closed-immersion", "lem-fin-coordinate-generic-dimension", "lem-fin-finite-boundary-comparison", "lem-fin-finite-boundary-reconstruction", "lem-fin-generic-radicial-smoothing", "lem-fin-projective-coordinate-boundary", "lem-fin-radicial-exchange-descent", "lemma-weil-pbc-finite-exchange", "sbc-def-base-change-map", "sbc-lem-base-change-composition", "thm-constructible-serre", "thm-sp-truncation-e2", "thm-weil-pbc-bounded-below", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $S$ be integral and of finite type over a field $k$, let
$\ell\ne\operatorname{char}(k)$, and let
$j:X\hookrightarrow Y$ be an open immersion of finite-type
$S$-schemes. For a constructible $\mathbf F_\ell$-sheaf $F$
on $X$, there is a nonempty open $U\subset S$ such that
$Rj_{U,*}F|_{X_U}$ belongs to $D^b_c(Y_U,\mathbf F_\ell)$
and, for every morphism $T\to U$ with Noetherian $T$, its canonical base-change morphism

$$
Rj_{U,*}F|_{X_U}\big|_{Y_T}
\longrightarrow Rj_{T,*}F|_{X_T}
$$

is an isomorphism.

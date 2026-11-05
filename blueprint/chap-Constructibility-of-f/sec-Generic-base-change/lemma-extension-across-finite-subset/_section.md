+++
id = "lemma-extension-across-finite-subset"
kind = "lemma"
title = "Extension across a finite subset"
order = 577
lean = ["AlgebraicGeometry.Etale.HasDirectImageBaseChangeOnPlus.of_finite_boundary"]
uses = ["definition-derived-base-change-map"]
+++
Let $S$ be integral and affine, let $b:Y\to S$ be projective, and let
$j:X\hookrightarrow Y$ be an open immersion with $X$ smooth over $S$. Let
$F$ be a finite locally constant $\Fell$-sheaf on $X_{\acute{e}t}$. Suppose
that there is an open $G\subset Y$ whose reduced complement
$i:Z\hookrightarrow Y$ is finite over $S$, such that
$(Rj_*F)|_G\in\Dbc(G,\Fell)$ and such that for every $k$-scheme $T\to S$ of
finite type the base change map $g_Y^*Rj_*F\to Rj_{T,*}g_X^*F$ is an
isomorphism on $G_T$. Then there is a nonempty open $S_0\subset S$ such that
$Rj_{S_0,*}(F|_{X_{S_0}})\in\Dbc(Y_{S_0},\Fell)$ and such that for every
$k$-scheme $T\to S_0$ of finite type the base change map
$g_Y^*Rj_{S_0,*}(F|_{X_{S_0}})\to Rj_{T,*}g_X^*F$ is an isomorphism.

+++
id = "def-nagata-graph-extension"
kind = "definition"
title = "Graph-extension construction"
order = 244
lean = ["AlgebraicGeometry.Compactification.ProperExtension"]
uses = ["def-nagata-admissible-blowup", "def-nagata-compactification", "def-nagata-elimination-indeterminacy", "def-nagata-global-blowup", "def-nagata-scheme-theoretic-image", "prop-nagata-global-blowup-cover-independent"]
+++
Let $u\colon U\to S$ be a morphism of schemes, let $V\subseteq U$ be an
open subscheme, and let $C=(V\xrightarrow{j}Y\xrightarrow{p}S)$ be a
compactification of $V\to S$. A *graph extension* of $C$ consists of

* a $V$-admissible blow-up $\pi\colon Y^{\mathrm{gr}}\to Y$ (admissible
  with respect to the open $j(V)\subseteq Y$);
* an open subscheme $V^{\mathrm{gr}}\subseteq Y^{\mathrm{gr}}$;
* a proper morphism $\psi^{\mathrm{gr}}\colon V^{\mathrm{gr}}\to U$ with
  $u\circ\psi^{\mathrm{gr}}=p\circ\pi|_{V^{\mathrm{gr}}}$;
* an open immersion $v\colon V\to V^{\mathrm{gr}}$ with $\pi\circ v=j$;

such that $\psi^{\mathrm{gr}}\circ v$ is the inclusion $V\subseteq U$,
$(\psi^{\mathrm{gr}})^{-1}(V)=v(V)$, and the restriction of
$\psi^{\mathrm{gr}}$ over $V$ is an isomorphism
$(\psi^{\mathrm{gr}})^{-1}(V)\xrightarrow{\sim}V$.

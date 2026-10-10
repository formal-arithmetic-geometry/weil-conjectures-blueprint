+++
id = "lemma-nagata-strict-transform-over-complement"
kind = "lemma"
title = "Strict transform on the preserved open"
order = 160
lean = ["AlgebraicGeometry.isPullback_strictTransformOpen"]
uses = ["lemma-nagata-strict-transform-closure-characterization", "prop-nagata-strict-transform-closed-fiber-product", "thm-nagata-global-blowup-complement"]
+++
Let $f\colon Y\to X$ and $\pi\colon X'\to X$ be morphisms and let
$U\subseteq X$ be an open subscheme over which $\pi$ is an isomorphism,
$\pi^{-1}(U)\xrightarrow{\sim}U$ (for instance
$X'=\operatorname{Bl}_{\mathcal I}(X)$ and $U=X\setminus V(\mathcal I)$).
Let $\Omega\subseteq Y\times_XX'$ be the open subscheme lying over $U$.
Then $\Omega$, together with its projection to $Y$ and the map
$\Omega\to\pi^{-1}(U)\xrightarrow{\sim}U$, is a fibre product of $f$ and the
inclusion $U\hookrightarrow X$; that is, $\Omega\cong Y\times_XU$
compatibly with the projections to $Y$.

+++
id = "def-nagata-strict-transform"
kind = "definition"
title = "Strict transform"
order = 144
lean = ["AlgebraicGeometry.strictTransform"]
uses = ["def-nagata-global-blowup", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
Let $f\colon Z\to X$ and $\pi\colon X'\to X$ be morphisms and let
$U\subseteq X$ be an open subscheme. Let
$\Omega\subseteq Z\times_XX'$ be the open subscheme lying over $U$,

$$
\Omega=(Z\times_XU)\times_U(X'\times_XU).
$$

The *strict transform* of $Z$ (relative to $U$) is the
scheme-theoretic image of the open immersion
$\Omega\hookrightarrow Z\times_XX'$, in the sense of
[def-nagata-scheme-theoretic-image]; it is a closed subscheme of
$Z\times_XX'$, namely the smallest closed subscheme of $Z\times_XX'$
through which $\Omega\hookrightarrow Z\times_XX'$ factors, i.e. the
scheme-theoretic closure of $\Omega$. For the blow-up
$X'=\operatorname{Bl}_{\mathcal I}(X)\to X$ of a quasi-coherent ideal
$\mathcal I$ one takes $U=X\setminus V(\mathcal I)$, and speaks of the
strict transform of $Z$ along the blow-up.

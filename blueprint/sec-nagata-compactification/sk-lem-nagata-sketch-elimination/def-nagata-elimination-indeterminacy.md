+++
id = "def-nagata-elimination-indeterminacy"
kind = "definition"
title = "Elimination-of-indeterminacy construction"
lean = ["AlgebraicGeometry.eliminationBoundaryIdeal", "AlgebraicGeometry.eliminationGraphSection", "AlgebraicGeometry.eliminationExtensionCentre", "AlgebraicGeometry.eliminationCentre", "AlgebraicGeometry.eliminationBlowup"]
order = 233
uses = ["def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-composition-of-blowups-comparison", "def-nagata-conrad-quasi-domination", "def-nagata-qc-open-complement-ideal", "def-nagata-dense-compactification", "def-nagata-global-blowup", "def-nagata-scheme-image-comparison", "def-nagata-strict-transform", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-admissible-blowup-preserves-density", "thm-nagata-global-blowup-proper", "lemma-nagata-composition-center-ideal", "lemma-nagata-composition-extended-ideal-equality", "lemma-nagata-conrad-schematically-dense-blowup", "lemma-nagata-qc-open-complement-ideal-exists", "lemma-nagata-dense-flat-pullback", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal", "lemma-nagata-strict-transform-over-complement", "prop-nagata-global-blowup-cover-independent", "thm-nagata-composition-of-blowups", "thm-nagata-conrad-elimination"]
+++
Let $X$ be qcqs, let $U\subseteq X$ be a quasi-compact open, and let
$q\colon Z\to X$ be separated and of finite type such that
$q^{-1}(U)\to U$ is an isomorphism.

1. Let $\mathcal I_0=\mathcal I_X(U)$ be the finite type ideal with
$V(\mathcal I_0)=X\setminus U$ of [def-nagata-qc-open-complement-ideal],
and put $\pi_1\colon X_1=\operatorname{Bl}_{\mathcal I_0}(X)\to X$, a
$U$-admissible blow-up. The open $U_1=\pi_1^{-1}(U)$ is quasi-compact and,
by [lemma-nagata-admissible-blowup-preserves-density],
scheme-theoretically dense in $X_1$.
1. Let $p\colon Z\times_XX_1\to X_1$ be the base change of $q$, and let
$s\colon U_1\to Z\times_XX_1$ be the section of $p$ over $U_1$ induced by
the inverse of $q^{-1}(U)\cong U$; it is a quasi-domination of $U_1$ over
$Z\times_XX_1$ ([def-nagata-conrad-quasi-domination]). Apply
[thm-nagata-conrad-elimination] over the base $X_1$ with $V=U_1$, and select
the resulting $U_1$-admissible centre $\mathcal I$ on $X_1$, together with
an open $W\subseteq\operatorname{Bl}_{\mathcal I}(X_1)$ containing the
inverse image of $U_1$ and an extension $\widetilde s\colon W\to
Z\times_XX_1$ of $s$ over $X_1$ whose graph is closed.
1. Let $K$ be the centre on $X$ representing the composite
$\operatorname{Bl}_{\mathcal I}(X_1)\to X_1\to X$ as one blow-up, given by
the composition construction of [lemma-nagata-admissible-blowup-comp]; its
support is exactly $X\setminus U$. Define

$$
X^{\mathrm{el}}(q,U)=\operatorname{Bl}_K(X)\cong\operatorname{Bl}_{\mathcal I}(X_1),
\qquad
Z^{\mathrm{el}}(q,U)=\operatorname{ST}_{X^{\mathrm{el}}/X}(Z),
$$

together with the strict-transform projection
$q^{\mathrm{el}}\colon Z^{\mathrm{el}}(q,U)\to X^{\mathrm{el}}(q,U)$.
Then $X^{\mathrm{el}}(q,U)\to X$ is a $U$-admissible blow-up of $X$
([def-nagata-admissible-blowup]).

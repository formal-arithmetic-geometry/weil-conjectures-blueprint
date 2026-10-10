+++
id = "thm-nagata-conrad-elimination"
kind = "theorem"
title = "Elimination of indeterminacy for quasi-dominations (Conrad)"
order = 220
lean = ["AlgebraicGeometry.exists_admissibleBlowup_extend_partialSection"]
uses = ["def-nagata-admissible-blowup", "def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-conrad-quasi-domination", "def-nagata-global-blowup", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-quasi-affine-morphism", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-affine-blowup-complement", "lemma-nagata-blowup-proper", "lemma-nagata-conrad-blowup-base-change-reduction", "lemma-nagata-conrad-closed-target-reduction", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-conrad-graph-closure-quasi-finite", "lemma-nagata-conrad-quasi-affine-general", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-localization-ideal-pow", "lemma-nagata-quasi-affine-morphism-of-quasi-finite", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-scheme-image-ideal-qc", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded", "thm-nagata-global-blowup-proper"]
+++
Let $X$ be a quasi-compact and quasi-separated scheme, let
$U\subseteq V\subseteq X$ be quasi-compact opens with $U$ dense in $X$,
and let $p\colon Y\to X$ be separated and of finite type with $Y$
quasi-compact and quasi-separated. Let $f\colon U\to Y$ be a section of
$p$ over $U$ whose image is closed in $p^{-1}(V)$. There are a
$V$-admissible blow-up $\pi\colon\widetilde X\to X$, an open
$W\subseteq\widetilde X$ containing $\pi^{-1}(U)$ and a morphism
$g\colon W\to Y$ with $p\circ g=\pi|_W$ extending $f$ (that is,
$g|_{\pi^{-1}(U)}=f\circ\pi|_{\pi^{-1}(U)}$), whose graph is closed in
$Y\times_X\widetilde X$.

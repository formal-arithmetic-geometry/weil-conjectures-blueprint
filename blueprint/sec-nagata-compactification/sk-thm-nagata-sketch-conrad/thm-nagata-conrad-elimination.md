+++
id = "thm-nagata-conrad-elimination"
kind = "theorem"
title = "Elimination of indeterminacy for quasi-dominations (Conrad)"
order = 220
lean = ["AlgebraicGeometry.exists_admissibleBlowup_extend_partialSection"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-global-blowup", "def-nagata-global-blowup-overlap-basic-map", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-rees-generators-cover-proj", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open"]
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

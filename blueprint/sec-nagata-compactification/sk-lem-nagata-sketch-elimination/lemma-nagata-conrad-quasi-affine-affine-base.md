+++
id = "lemma-nagata-conrad-quasi-affine-affine-base"
kind = "lemma"
title = "Quasi-affine target over an affine base (Conrad)"
order = 315
lean = ["AlgebraicGeometry.exists_isAdmissible_extend_of_isQuasiAffine"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-dense-compactification", "def-nagata-global-blowup", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-quasi-affine-immersion-affine-space-exists", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X$ be affine, let $U\subseteq X$ be a quasi-compact open, let $Y$ be a
quasi-affine scheme, let $p\colon Y\to X$ be locally of finite type, and
let $f\colon U\to Y$ be an $X$-morphism. There is a $U$-admissible blow-up
$\pi\colon\widetilde X\to X$ in which $\pi^{-1}(U)$ is
scheme-theoretically dense, together with an open
$W\subseteq\widetilde X$ containing $\pi^{-1}(U)$ and an $X$-morphism
$\widetilde f\colon W\to Y$ extending $f$ whose graph is closed in
$Y\times_X\widetilde X$; thus $(W,\widetilde f)$ is a quasi-domination of
$\widetilde X$ over $Y$ extending $f$.

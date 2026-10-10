+++
id = "lemma-nagata-conrad-quasi-affine-equal-opens"
kind = "lemma"
title = "Quasi-affine target over a qcqs base, $U=V$ (Conrad)"
order = 212
lean = ["AlgebraicGeometry.exists_isAdmissible_extend_of_isQuasiAffineHom"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-constructible-closed-support", "def-nagata-dense-compactification", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "def-nagata-qc-open-complement-ideal", "def-nagata-quasi-affine-morphism", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-blowup-proper", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-conrad-quasi-affine-affine-base", "lemma-nagata-constructible-closed-support", "lemma-nagata-dense-flat-pullback", "lemma-nagata-ext-scheme-theoretically-dominant-separated", "lemma-nagata-extend-admissible-blowup", "lemma-nagata-ideal-invertible-product-factor", "lemma-nagata-invertible-product-factor", "lemma-nagata-qc-open-complement-ideal", "lemma-nagata-qc-open-complement-ideal-exists", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property", "thm-nagata-global-blowup-proper"]
+++
Let $X$ be qcqs, let $U\subseteq X$ be a quasi-compact open, let
$p\colon Y\to X$ be separated, quasi-affine and locally of finite type, and
let $f\colon U\to Y$ be an $X$-morphism. There is a finite type
quasi-coherent ideal $\mathcal I$ on $X$ with
$V(\mathcal I)\subseteq X\setminus U$ such that
$\widetilde X=\operatorname{Bl}_{\mathcal I}(X)$ carries a quasi-domination
of $\widetilde X$ over $Y$ extending $f$, and such that the inverse image of
$U$ in $\widetilde X$ is scheme-theoretically dense.

As in [lemma-nagata-conrad-quasi-affine-affine-base], $U$ need not be
assumed dense in $X$: the centre constructed below cuts out exactly the
boundary $X\setminus U$, so the inverse image of $U$ becomes
scheme-theoretically dense in $\widetilde X$ in any case.

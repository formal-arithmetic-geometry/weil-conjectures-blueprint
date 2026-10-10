+++
id = "lemma-nagata-conrad-quasi-affine-general"
kind = "lemma"
title = "Quasi-affine target, $U\\subseteq V$ (Conrad)"
order = 216
lean = ["AlgebraicGeometry.exists_isAdmissible_extend_of_isQuasiAffineHom_of_le"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-global-blowup", "def-nagata-quasi-affine-morphism", "lemma-nagata-conrad-dense-in-admissible-blowup", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X$ be qcqs, let $U\subseteq V\subseteq X$ be quasi-compact open
subschemes, let $Y$ be qcqs and let $p\colon Y\to X$ be separated,
quasi-affine and locally of finite type. Let $f\colon U\to Y$ be an
$X$-morphism whose image is closed in $p^{-1}(V)$. There is a finite type
quasi-coherent ideal $\mathcal I$ on $X$ with
$V(\mathcal I)\subseteq X\setminus V$ such that, writing
$\pi\colon\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$, there are an
open $W\subseteq\widetilde X$ containing $\pi^{-1}(U)$ and an $X$-morphism
$g\colon W\to Y$ extending $f$ whose graph is closed in
$Y\times_X\widetilde X$.

Neither $U$ nor $V$ needs to be assumed dense in $X$. The only density used
below is that of the inverse image of $U$ in the blow-up of the smaller base
$X^{\circ}$ of Step 2, and that is exactly the scheme-theoretic density which
[lemma-nagata-conrad-quasi-affine-equal-opens] hands back. Note also
that the centre is only required to avoid the *larger* open $V$, which
is what makes this statement stronger than
[lemma-nagata-conrad-quasi-affine-equal-opens] rather than a special
case of it.

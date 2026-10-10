+++
id = "lemma-nagata-conrad-quasi-affine-affine-base"
kind = "lemma"
title = "Quasi-affine target over an affine base (Conrad)"
order = 210
lean = ["AlgebraicGeometry.exists_isAdmissible_extend_of_isQuasiAffine"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-dense-compactification", "def-nagata-global-blowup", "def-nagata-relative-affine-space", "def-nagata-scheme-image-comparison", "lemma-nagata-admissible-blowup-comp", "lemma-nagata-affine-finite-type-is-quasi-affine", "lemma-nagata-blowup-proper", "lemma-nagata-conrad-affine-space-extension", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-conrad-schematically-dense-blowup", "lemma-nagata-dense-flat-pullback", "lemma-nagata-quasi-affine-immersion-affine-space-exists", "lemma-nagata-scheme-image-universal", "lemma-nagata-scheme-theoretic-closure-minimal", "prop-nagata-global-blowup-cover-independent", "thm-nagata-global-blowup-proper"]
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

## Proof

By [lemma-nagata-quasi-affine-immersion-affine-space-exists] there are
an $n$ and a quasi-compact immersion $i\colon Y\to\mathbb A^n_X$ over $X$.
Put $F=i\circ f\colon U\to\mathbb A^n_X$. By
[lemma-nagata-conrad-affine-space-extension] there is a $U$-admissible
blow-up $\widetilde X_0\to X$, an open $\widetilde W_0\subseteq\widetilde X_0$
containing the inverse image of $U$ and an $X$-morphism
$\widetilde F_0\colon\widetilde W_0\to\mathbb A^n_X$ extending $F$ whose
graph is closed in $\widetilde X_0\times_X\mathbb A^n_X$.

Next make $U$ scheme-theoretically dense. By
[lemma-nagata-conrad-schematically-dense-blowup] there is a
$U$-admissible blow-up $\widetilde X\to\widetilde X_0$ in which $U$ is
scheme-theoretically dense, and by
[lemma-nagata-admissible-blowup-comp] the composite
$\widetilde X\to X$ is again a $U$-admissible blow-up. Let $\widetilde W$ be
the preimage of $\widetilde W_0$ and $\widetilde F$ the composite; the graph
$\Gamma_{\widetilde F}$ is the base change of $\Gamma_{\widetilde F_0}$ and
hence still closed in $\widetilde X\times_X\mathbb A^n_X$.

Because $i$ is an immersion there is an open subscheme
$U'\subseteq\mathbb A^n_X$ such that $i$ factors as a closed immersion
$j\colon Y\hookrightarrow U'$. Put $W=\widetilde F^{-1}(U')$. It is an open
subscheme of $\widetilde X$ containing $U$, hence scheme-theoretically dense
in $\widetilde X$ and containing $U$ as a scheme-theoretically dense open.
Moreover $\Gamma_{\widetilde F|_W} =\Gamma_{\widetilde F}\cap(\widetilde X\times_XU')$ is closed in
$\widetilde X\times_XU'$.

We claim that $\widetilde F|_W$ factors as $j\circ\widetilde f$ for a
(necessarily unique) $\widetilde f\colon W\to Y$. Indeed, the pullback of
the closed immersion $j$ along $\widetilde F|_W$ is a closed subscheme of
$W$; it contains $U$ as an open subscheme, because
$\widetilde F|_U=F=j\circ f$ factors through $Y$. Since $U$ is
scheme-theoretically dense in $W$, the only closed subscheme of $W$
containing $U$ as an open subscheme is $W$ itself, so the pullback is $W$
and the factorization exists.

Then $\widetilde f|_U=f$, and $\Gamma_{\widetilde f} =(1_{\widetilde X}\times j)^{-1}(\Gamma_{\widetilde F|_W})$ is closed in
$\widetilde X\times_XY$. Thus $(W,\widetilde f)$ is the required
quasi-domination.

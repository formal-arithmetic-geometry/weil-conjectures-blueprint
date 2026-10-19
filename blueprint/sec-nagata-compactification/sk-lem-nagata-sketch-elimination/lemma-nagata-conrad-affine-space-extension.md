+++
id = "lemma-nagata-conrad-affine-space-extension"
kind = "lemma"
title = "Extension to $\\mathbb A^n$ after one admissible blow-up (Conrad)"
order = 216
lean = ["AlgebraicGeometry.exists_isAdmissible_extend_affineSpace"]
uses = ["def-nagata-admissible-blowup", "def-nagata-conrad-quasi-domination", "def-nagata-global-blowup", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-relative-affine-space", "lemma-nagata-conrad-dense-in-admissible-blowup", "lemma-nagata-rees-generators-cover-proj", "prop-nagata-affine-blowup-chart-cover", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X=\operatorname{Spec}(A)$ be affine, let $U\subseteq X$ be a
quasi-compact open and let $f\colon U\to\mathbb A^n_X$ be an $X$-morphism.
There is a finite type quasi-coherent ideal $\mathcal I$ on $X$ with
$V(\mathcal I)\subseteq X\setminus U$, so that
$\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$ is a $U$-admissible
blow-up, together with an open subscheme $W\subseteq\widetilde X$ containing
the inverse image of $U$ and an $X$-morphism
$\widetilde f\colon W\to\mathbb A^n_X$ extending $f$, whose graph

$$
\Gamma_{\widetilde f}\hookrightarrow
\widetilde X\times_X\mathbb A^n_X
$$

is closed.

No density hypothesis on $U$ is needed here; when $U$ is dense in $X$, the
open $W$ is automatically dense in $\widetilde X$ by
[lemma-nagata-conrad-dense-in-admissible-blowup].

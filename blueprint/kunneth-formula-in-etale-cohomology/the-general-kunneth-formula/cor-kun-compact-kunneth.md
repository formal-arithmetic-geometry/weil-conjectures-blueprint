+++
id = "cor-kun-compact-kunneth"
kind = "theorem"
title = "K\"unneth formula for compactly supported cohomology"
order = 6159
lean = ["AlgebraicGeometry.Etale.kunnethMap_compactSupport_isIso"]
tags = ["latex:corollary"]
uses = ["def-compact-support-direct-image", "thm-kun-0F1P", "def-kun-kunneth-map", "def-kun-separably-closed"]
+++
Let $k$ be a separably closed field ([def-kun-separably-closed]), let $X$
and $Y$ be schemes of finite type over $k$, let $n\ge1$ be an integer
invertible in $k$, and let $E\in D(X_{\Et},\mathbf Z/n\mathbf Z)$,
$K\in D(Y_{\Et},\mathbf Z/n\mathbf Z)$. Choose compactifications
$j_X:X\hookrightarrow\overline X$ and $j_Y:Y\hookrightarrow\overline Y$ over
$k$, with $\overline X,\overline Y$ proper over $k$, and put
$R\Gamma_c(X_{\Et},E)=R\Gamma(\overline X_{\Et},j_{X,!}E)$ and similarly for
$Y$. Then the composite
$$
\begin{gathered}
R\Gamma_c(X_{\Et},E)\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}R\Gamma_c(Y_{\Et},K)
\\
\xrightarrow{\ \sim\ }
R\Gamma\bigl((X\times_kY)_{\Et},
\operatorname{pr}_1^{-1}j_{X,!}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}j_{Y,!}K\bigr)
\\
\xrightarrow{\ \sim\ }
R\Gamma_c\bigl((X\times_kY)_{\Et},
\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}K\bigr)
\end{gathered}
$$
of the Kunneth map of [thm-kun-0F1P] applied to $j_{X,!}E$ and $j_{Y,!}K$ with
the identification of the second line is an isomorphism; the second arrow
identifies
$\operatorname{pr}_1^{-1}j_{X,!}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}j_{Y,!}K$
with
$j_{X\times_kY,!}(\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}K)$
along the compactification $j_X\times_kj_Y$.

## Proof

The first arrow is an isomorphism by [thm-kun-0F1P], applied to the
complexes $j_{X,!}E\in D(\overline X_{\Et},\mathbf Z/n\mathbf Z)$ and
$j_{Y,!}K\in D(\overline Y_{\Et},\mathbf Z/n\mathbf Z)$ and to the isomorphism
$R\Gamma(\overline X_{\Et},j_{X,!}E)\cong R\Gamma_c(X_{\Et},E)$ which is the
definition of compact support. For the second arrow: the product of the two
open immersions $j_X,j_Y$ is the open immersion $j_X\times_kj_Y$ of
$X\times_kY$ into $\overline X\times_k\overline Y$, which is proper over $k$
because properness is stable under products, so
$j_{X\times_kY,!}=j_{X,!}\boxtimes j_{Y,!}$ is the extension by zero along the
compactification, and the identity
$\operatorname{pr}_1^{-1}j_{X,!}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}j_{Y,!}K\cong(j_X\times_kj_Y)_!(\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}K)$
is the compatibility of the extension by zero with the tensor product and the
inverse image. The independence of the two isomorphisms of the chosen
compactifications is the coherence recorded in the definition of the
compact-support direct image.

Unresolved dependencies: def:weil-extension-by-zero

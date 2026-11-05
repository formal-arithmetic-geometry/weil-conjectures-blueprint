+++
id = "lemma-reduction-curve-over-normal-base--1"
kind = "lemma"
title = "Reduction over a normal base with arbitrary coefficients"
name_showing = false
order = 681001
aliases = ["bp-r205-1"]
lean = ["AlgebraicGeometry.Etale.exists_isPullback_not_isZero_higherDirectImage"]
uses = ["definition-derived-base-change-map", "prose-08-06"]
+++
Let $g:Y'\to Y$ be a morphism of schemes, let $\Lambda$ be a commutative
ring, and let $n\in\mathbf N$ be invertible on $Y$ with $n\Lambda=0$.
Let $q\geq1$ be an integer. Suppose that, after every base change
$T\to Y$, the base change maps along $Y'\times_YT\to T$ in every
integer degree $q'<q$ are isomorphisms for every qcqs morphism $Z\to T$
and every sheaf of $\Lambda$-modules on $Z_{\acute{e}t}$. Suppose that
some such map in degree $q$ is not an isomorphism.

Then there are an affine scheme
$S=\operatorname{Spec}R$ over $Y$ with $R$ a normal domain whose fraction
field $L$ is algebraically closed, an algebraically closed extension
field $\Omega$ of $L$, an integer $m\in\mathbf N$ with $m\mid n$, and, for
$C=Y'\times_YS$, the cartesian square

$$
\begin{CD}
C_\Omega @>{h}>> C\\
@VVV @VVV\\
\operatorname{Spec}\Omega @>>> S
\end{CD}
$$

such that

$$
R^qh_*\underline{\Lambda/m\Lambda}\ne0.
$$

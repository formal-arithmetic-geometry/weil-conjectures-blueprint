+++
id = "lemma-reduction-curve-over-normal-base--1"
kind = "lemma"
title = "Reduction to a curve over a normal base"
order = 682001
aliases = ["bp-r205-1"]
lean = ["AlgebraicGeometry.Etale.exists_isPullback_not_isZero_higherDirectImage"]
+++
Let $g:Y'\to Y$ be a morphism of schemes, let $n\geq1$ be an integer
invertible on $Y$, and let $q\geq1$. Suppose that $\mathrm{BC}(g,n,q-1)$ holds
and that $\mathrm{BC}(g,n,q)$ fails, that is, for some scheme $T$ over $Y$,
some qcqs morphism $Z\to T$ and some sheaf of $\mathbf Z/n$-modules on
$Z_{\acute{e}t}$, the base change map in degree $q$ along $Y'\times_YT\to T$ is not
an isomorphism. Then there are an affine scheme $S=\operatorname{Spec}R$ over
$Y$ with $R$ a normal domain whose fraction field $L$ is algebraically closed,
an algebraically closed extension field $\Omega$ of $L$, an integer $m\geq1$
with $m\mid n$, and, for $C=Y'\times_YS$, the cartesian square

$$
\begin{CD}
C_\Omega @>{h}>> C\\
@VVV @VVV\\
\operatorname{Spec}\Omega @>>> S
\end{CD}
$$

such that

$$
R^qh_*\underline{\mathbf Z/m}\ne0.
$$

If $g$ is affine and smooth of relative dimension one, then $C$ is a smooth
affine curve over $S$.

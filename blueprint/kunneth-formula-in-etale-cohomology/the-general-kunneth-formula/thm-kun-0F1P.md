+++
id = "thm-kun-0F1P"
kind = "theorem"
title = "Kunneth formula, etale cohomology"
order = 6158
lean = ["AlgebraicGeometry.Etale.kunnethMap_isIso"]
uses = ["def-kun-kunneth-map", "def-kun-separably-closed", "lem-kun-0F10", "lem-kun-0F12", "lem-kun-0F1N", "lem-kun-cd-sep-closed-point", "lem-kun-kunneth-via-0F1N", "lem-kun-leray-unbdd"]
+++
Let $k$ be a separably closed field ([def-kun-separably-closed]) and let
$X$ and $Y$ be schemes of finite type over $k$. Let $n\ge1$ be an integer
invertible in $k$. Then for $E\in D(X_{\Et},\mathbf Z/n\mathbf Z)$ and
$K\in D(Y_{\Et},\mathbf Z/n\mathbf Z)$ the Kunneth map of
[def-kun-kunneth-map]
$$
 \kappa_{E,K}:\RGamma(X_{\Et},E)\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\RGamma(Y_{\Et},K)
 \longrightarrow
 \RGamma\bigl((X\times_kY)_{\Et},
 \operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}K\bigr)
$$
is an isomorphism. (*Source:* Stacks Project, Tag
[0F1P](https://stacks.math.columbia.edu/tag/0F1P).)

## Proof

By [lem-kun-0F1N] applied to the diagram
$$
 \begin{array}{ccccc}
  X&\xleftarrow{\;=\;}&X&\xleftarrow{\;\operatorname{pr}_1\;}&X\times_kY\\
  \Big\downarrow{}&&\Big\downarrow{}&&\Big\downarrow{\scriptstyle \operatorname{pr}_2}\\
  \Spec(k)&\longleftarrow&\Spec(k)&\xleftarrow{\;=\;}&Y
 \end{array}
$$
(all schemes of finite type over $k$, $n$ invertible in $k$) we have the
isomorphism
$$
 \varphi:
 E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\underline{\RGamma(Y_{\Et},K)}
 \longrightarrow
 R\operatorname{pr}_{1,*}\bigl(\operatorname{pr}_1^{-1}E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\operatorname{pr}_2^{-1}K\bigr).
$$
We conclude by [lem-kun-kunneth-via-0F1N] and the following two
identifications: first,
$\RGamma((X\times_kY)_{\Et},-)\cong\RGamma(X_{\Et},-)\circ R\operatorname{pr}_{1,*}$
by [lem-kun-leray-unbdd], which applies because $\operatorname{pr}_1$ is a
qcqs morphism of finite type schemes over $k$ and
$\operatorname{cd}(\operatorname{pr}_1)<\infty$ by [lem-kun-0F10](1); second,
$$
 \RGamma\bigl(X_{\Et},E\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\underline{\RGamma(Y_{\Et},K)}\bigr)
 \cong\RGamma(X_{\Et},E)\otimes^{\mathbf L}_{\mathbf Z/n\mathbf Z}\RGamma(Y_{\Et},K)
$$
by [lem-kun-0F12], which applies because $\operatorname{cd}(X)<\infty$ by
[lem-kun-cd-sep-closed-point] and [lem-kun-0F10](2). Hence $\kappa_{E,K}$ (the
Kunneth map of [def-kun-kunneth-map]) is an isomorphism, as desired.

+++
kind  = "proof"
of    = "thm-kun-0f1p"
+++
By [lem-kun-0f1n] applied to the diagram

$$
\begin{array}{ccccc}
X&\xleftarrow{\;=\;}&X&\xleftarrow{\;\pr_1\;}&X\times_kY\\
\Big\downarrow{}&&\Big\downarrow{}&&\Big\downarrow{\scriptstyle \pr_2}\\
\Spec(k)&\longleftarrow&\Spec(k)&\xleftarrow{\;=\;}&Y
\end{array}
$$

(all schemes of finite type over $k$, $n$ invertible in $k$) we
have the isomorphism

$$
\varphi:
E\kunotimes{\kunZn}\underline{\RGamma(Y_{\Et},K)}
\longrightarrow
R\pr_{1,*}\bigl(\pr_1^{-1}E\kunotimes{\kunZn}\pr_2^{-1}K\bigr).
$$

We conclude by [lem-kun-kunneth-via-0f1n] and the following
two identifications: first,
$\RGamma((X\times_kY)_{\Et},-)\cong\RGamma(X_{\Et},-)\circ R\pr_{1,*}$
by [lem-kun-leray-unbdd], which applies because $\pr_1$ is a
qcqs morphism of finite type schemes over $k$ and
$\kuncd(\pr_1)<\infty$ by [lem-kun-0f10](1); second,

$$
\RGamma\bigl(X_{\Et},E\kunotimes{\kunZn}\underline{\RGamma(Y_{\Et},K)}\bigr)
\cong\RGamma(X_{\Et},E)\kunotimes{\kunZn}\RGamma(Y_{\Et},K)
$$

by [lem-kun-0f12], which applies because
$\kuncd(X)<\infty$ by [lem-kun-cd-sep-closed-point] and
[lem-kun-0f10](2). Hence $\kappa_{E,K}$ (the Kunneth map of
[def-kun-kunneth-map]) is an isomorphism, as desired.

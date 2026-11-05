+++
kind = "proof"
of = "proposition-frobenius-local-term-curve"
order = 995
+++
Let $i:\{y\}\hookrightarrow X$ and $j:U=X\setminus\{y\}\hookrightarrow X$.
We split $\psi$ along the localization triangle and compute the two local
terms separately.

*Splitting $\psi$.* Both pieces are stable under $\Phi_X^m$, and in
fact $((\Phi_X^m)^{-1}\{y\})_{\mathrm{red}}=\{y\}$. In the enhanced derived
category, the functorial localization triangle is a two-step filtered
object,

$$
K_U=j_!j^*K\longrightarrow K\longrightarrow i_*i^*K
\xrightarrow{+1},
$$

and $\psi$ induces a coherent map from the $(\Phi_X^m)^*$-pullback of this
filtration to the filtration itself, with induced correspondences
$\psi_U$ and $i_*\psi_{\bar y}$ on the pieces. This rests on two base
change identities. For the open part,
$(\Phi_X^m)^*j_!\simeq j_!(\Phi_X^m|_U)^*$ by base change along inverse
images in the cartesian square. The square for the point, by contrast, is cartesian only after passing to reductions, so there proper base change followed by
nilpotent invariance gives $(\Phi_X^m)^*i_*\simeq i_*(\Phi_X^m|_y)^*$. Both
comparisons are mates of the adjunction units for $j$ and $i$ used in the
triangle, which is why the induced maps are compatible with the filtration.

*Additivity.* The second half of
Proposition [proposition-additivity-trace-classes] applies to the
graph $c_m$, because its hypothesis $\Phi_X^m(\{y\})\subset\{y\}$ holds for
the fixed point $y$. It gives

$$
\operatorname{LT}_y(\psi)
=\operatorname{LT}_y(\psi_U)
+\operatorname{LT}_y(i_*\psi_{\bar y}).
$$

*The two local terms.* The first term is zero by
Lemma [lemma-vanishing-local-term-zero-stalk], since
$(K_U)_{\bar y}=0$. For the second, the description of the closed piece
$u_Z$ in Proposition [proposition-additivity-trace-classes] shows that
$i_*\psi_{\bar y}$ is the pushforward along $i$ of the cohomological
correspondence $\psi_{\bar y}$ on $(y,K_{\bar y})$ for the identity
correspondence of $y$. Its local term is therefore
$\operatorname{tr}_A(\psi_{\bar y}\mid K_{\bar y})$, the trace on
the perfect complex $K_{\bar y}$, by the compatibility with proper
pushforward in Theorem [theorem-proper-pushforward-lefschetz-verdier]
and Lemma [lemma-local-terms-point].

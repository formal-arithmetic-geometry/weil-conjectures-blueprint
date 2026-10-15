+++
kind  = "proof"
of    = "det-lem-int-tensor-pullback"
uses = ["det-lem-int-tensor-shriek", "sk-prop-sfb-cartesian-coefficients", "sk-prop-sf-open-closed-triangle", "sk-prop-integral-criterion", "sk-lem-integral-models", "sk-def-pe-derived-completion"]
+++
By [sk-prop-sfb-cartesian-coefficients], $g^{-1}\mathcal O_{E,Y}=\mathcal O_{E,X}$ and
$g^{-1}(\mathcal O_E/\pi_E^n)_Y=(\mathcal O_E/\pi_E^n)_X$, so $g^*=g^{-1}$ is exact on
module sheaves, needs no deriving, and commutes with reduction:
$g^*(K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)=g^*K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n$ (both are the
cone of $\pi_E^n$ on $g^*K$). The maps $g^*K\to g^*(K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$ are
compatible in $n$ and define $c_K$; its target is
$R\varprojlim_n(g^*K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$, so $c_K$ is the completion map
of $g^*K$, and **$c_K$ is an isomorphism if and only if $g^*K$ is derived
complete** ([sk-def-pe-derived-completion]). Both $g^*$ and
$K\mapsto R\varprojlim_ng^*(K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n)$ are exact functors and
$c$ is a natural transformation between them.

*Local models.* Let $a\colon S\hookrightarrow Y$ be a stratum inclusion and $M$ as in
[det-lem-int-tensor-shriek] (2): there is a pro-étale cover $\{W_k\to S\}$ with
$M|_{W_k}\simeq P_k\otimes_{\mathcal O_E}\mathcal O_{E,W_k}$, $P_k$ a bounded complex of finite
free $\mathcal O_E$-modules. Let $S'=S\times_YX$, with $a'\colon S'\hookrightarrow X$ and
$g_S\colon S'\to S$. The open–closed operations commute with base change
([sk-prop-sf-open-closed-triangle]), so $g^*a_!M\simeq a'_!g_S^*M$. The base
changes $W'_k=W_k\times_SS'$ form a pro-étale cover of $S'$, and
$(g_S^*M)|_{W'_k}\simeq P_k\otimes_{\mathcal O_E}\mathcal O_{E,W'_k}$, the same complex of finite
free modules over the coefficient ring of the new scheme. This is a bounded
complex of finite free $\mathcal O_{E,W'_k}$-modules; it is derived complete since
$\mathcal O_{E,W'_k}$ is, and its reduction $P_k/\pi_E\otimes(\mathcal O_E/\pi_E)_{W'_k}$ is a
bounded complex of finite free modules, hence constructible. Derived
completeness is pro-étale local (restriction to $W'_k$ is exact, preserves
products and hence $R\varprojlim$, and the restrictions to a cover are jointly
conservative), and a finite constant local model on a cover of the single
stratum $S'$ is what constructibility requires. So $g_S^*M\in\Dbc(S',\mathcal O_E)$ by
[sk-prop-integral-criterion], and $g^*a_!M=a'_!g_S^*M\in\Dbc(X,\mathcal O_E)$ by
[det-lem-int-tensor-shriek] (1). In particular $c_{a_!M}$ is an isomorphism.

*Dévissage.* By [det-lem-int-tensor-shriek] (2), every $K\in\Dbc(Y,\mathcal O_E)$ is
obtained from objects $a_!M$ as above by finitely many extensions. The
subcategory of $K$ with $g^*K\in\Dbc(X,\mathcal O_E)$ is closed under extensions,
because $g^*$ is exact and $\Dbc(X,\mathcal O_E)$ is triangulated
([sk-lem-int-integral-heart]); so (1) holds. Similarly the subcategory where
$c_K$ is an isomorphism is closed under extensions by the five lemma, which
proves the first half of (2).

*Comparison with the Stacks Project.* By [sk-lem-integral-models] (1),(2),
restriction of scalars along $\underline{\mathcal O_E}\to\mathcal O_{E,X}$ identifies
$\Dbc(X,\mathcal O_E)$ with the category $\Dc(X,\mathcal O_E)$ of the Stacks Project
(Stacks, Tags 099I, 099L), and it commutes with $g^{-1}$, with reduction
modulo $\pi_E^n$ (both are cones of $\pi_E^n$) and with $R\varprojlim$ (restriction
of scalars is exact and preserves products). The completed inverse image of
the Stacks Project is $R\varprojlim_ng^{-1}(K\otimes^{\mathbf L}\underline{\mathcal O_E}/\pi_E^n)$, i.e.
the restriction of scalars of the target of $c_K$. Hence $c_K$ identifies
$g^*K$ with the completed inverse image.

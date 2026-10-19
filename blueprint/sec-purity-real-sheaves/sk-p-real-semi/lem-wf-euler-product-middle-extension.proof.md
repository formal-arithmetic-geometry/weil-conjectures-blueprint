+++
kind  = "proof"
of    = "lem-wf-euler-product-middle-extension"
uses = ["det-thm-tf-uniform-formula-weil", "lem-wf-boundary-stalk-invariants", "lem-wf-lisse-stalk-vanishing", "prop-wf-weil-sheaf-representation-equivalence", "sk-def-sfb-bounded-constructible", "sk-lem-coefficient-heart", "sk-prop-pe-condensed-point", "sk-prop-sfb-module-pullback-exact", "sk-thm-sf-ctf-stability", "thm-trf-l-function-euler-product"]
+++
This is the curve case of the Euler-product form of the trace formula
[thm-trf-l-function-euler-product], applied with $\Lambda=\Qlb$, i.e. to
$\Dbc(X,\Qlb)$ ([sk-def-sfb-bounded-constructible]), to the curve
$X_0$ (separated of finite type, of dimension one) and the
constructible sheaf $K=j_*\mathcal F$ placed in degree zero, under the
hypotheses of [det-thm-tf-uniform-formula-weil] with which the
trace formula is applied to it. Its $L(X_0,j_*\mathcal F,t)$ is the
left-hand side (the local factor at $x$ being
$\det(1-F_xt^{d(x)}\mid(j_*\mathcal F)_{\bar x})$, with $e_x=d(x)$),
and its items (2) and (3) give

$$
L(X_0,j_*\mathcal F,t)=
\frac{\det(1-Ft,H_c^1(X,j_*\mathcal F))}
{\det(1-Ft,H_c^0(X,j_*\mathcal F))\,\det(1-Ft,H_c^2(X,j_*\mathcal F))}.
$$

It remains to see that the degree-zero factor is $1$, i.e.
$H_c^0(X,j_*\mathcal F)=0$. Let $k:X\hookrightarrow\bar X$ be a smooth
compactification, so that $H_c^0(X,j_*\mathcal F)=\Gamma(\bar X,k_!j_*\mathcal F)$. The
map $\alpha:k_!G\to k_*G=(kj)_*\mathcal F$, $G=j_*\mathcal F$, is injective. Both sides are
constructible: $k_!G$ is $G$ on $X$ and $0$ on the finite complement, and
$k_*G=\mathcal H^0(R(kj)_*\mathcal F)$ with $R(kj)_*$ preserving $\Dbc(-,\Qlb)$
([sk-thm-sf-ctf-stability]); so $\ker\alpha$ is constructible
([sk-lem-coefficient-heart] (1)). Its stalks vanish. Indeed, geometric stalks are exact
(the pullback to a geometric point is exact, [sk-prop-sfb-module-pullback-exact], and its
global sections are exact because every pro-étale cover of the spectrum of an algebraically
closed field has a section, [sk-prop-pe-condensed-point]), so
$(\ker\alpha)_{\bar x}=\ker(\alpha_{\bar x})$, and $\alpha_{\bar x}$ is injective at every
geometric point $\bar x$ of $\bar X$: over $X$ the restriction $k^*\alpha$ is the identity of
$G=k^*k_!G=k^*k_*G$, and over $\bar X\setminus X$ the source stalk is $0$, $k_!$ being
extension by zero. A constructible sheaf with zero stalks vanishes: for each stratum
$a:S\hookrightarrow\bar X$ of the filtration of [sk-lem-coefficient-heart] (3) its lisse
restriction to $S$ vanishes by [lem-wf-lisse-stalk-vanishing] (2), hence so does every
subquotient of the filtration. So $\ker\alpha=0$, and a compactly supported section $s$ is a section of
$(kj)_*\mathcal F$ over $\bar X$, i.e. an element $v\in\Gamma(U,\mathcal F)$, which by
[prop-wf-weil-sheaf-representation-equivalence] is a $\pi_1(U)$-invariant vector of the
geometric generic stalk $\mathcal F_{\bar\eta}$, and its germ at a geometric point
$\bar\infty$ of $\bar X\setminus X\neq\emptyset$ (as $X$ is affine) must vanish. By
[lem-wf-boundary-stalk-invariants] that germ is $v$ itself, viewed in
$((kj)_*\mathcal F)_{\bar\infty}=\mathcal F_{\bar\eta}^{I_\infty}$. Hence $v=0$ and
$s=0$.

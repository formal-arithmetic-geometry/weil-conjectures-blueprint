+++
kind  = "proof"
of    = "lem-wf-euler-product-middle-extension"
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
map $k_!j_*\mathcal F\to k_*j_*\mathcal F=(kj)_*\mathcal F$ is injective: its kernel is
constructible ([sk-lem-coefficient-heart] (1)) with zero stalks, hence zero, geometric
stalks being jointly conservative on constructible sheaves by
[sk-lem-coefficient-heart] (3). So a compactly supported section $s$ is a section of
$(kj)_*\mathcal F$ over $\bar X$, i.e. an element $v\in\Gamma(U,\mathcal F)$, which by
[prop-wf-weil-sheaf-representation-equivalence] is a $\pi_1(U)$-invariant vector of the
geometric generic stalk $\mathcal F_{\bar\eta}$, and its germ at a geometric point
$\bar\infty$ of $\bar X\setminus X\neq\emptyset$ (as $X$ is affine) must vanish. By
[lem-wf-boundary-stalk-invariants] that germ is $v$ itself, viewed in
$((kj)_*\mathcal F)_{\bar\infty}=\mathcal F_{\bar\eta}^{I_\infty}$. Hence $v=0$ and
$s=0$.

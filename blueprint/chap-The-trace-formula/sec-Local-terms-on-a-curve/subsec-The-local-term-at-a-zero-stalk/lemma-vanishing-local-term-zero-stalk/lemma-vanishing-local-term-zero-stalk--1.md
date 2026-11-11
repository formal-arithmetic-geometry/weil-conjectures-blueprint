+++
id = "lemma-vanishing-local-term-zero-stalk--1"
kind = "lemma"
title = "Vanishing of the supported restriction"
order = 990001
aliases = ["bp-r302-1"]
lean = ["AlgebraicGeometry.Etale.CurveLocalModel.sectionsWithSupportRestriction_eq_zero", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.upperStar_map_supportedRestriction_frobeniusGraph_eq_zero"]
uses = ["lemma-local-term-restriction-map", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--6", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "theorem-f-shriek-ell-adic-coefficients--5", "proposition-six-operations-dctf--14", "definition-verdier-dual-evaluation--2", "definition-correspondence--1", "definition-correspondence--2", "definition-correspondence--3", "definition-frobenius-correspondences-their-operators--1", "definition-frobenius-correspondences-their-operators--5", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
Let $k$ be algebraically closed, let $X/k$ be a separated, quasi-compact
smooth curve, and let $h:X\to X$ be a $k$-endomorphism fixing $y\in X(k)$
such that $h^\#\mathfrak m_y\subseteq\mathfrak m_y^2$. Let $\ell$ be a
prime invertible in $k$, let $A$ be a finite commutative $\ell$-primary
ring, and let $L,K\in D^b_{\mathrm{ctf}}(X,A)$ with $K_{\bar y}=0$.
On the strict localization $T$ of $X\times_k X$ at $(y,y)$, let
$\Gamma$ and $\Delta$ be the inverse images of the transposed graph
$(h,\operatorname{id}_X)$ and the diagonal, and put
$P=(L\boxtimes K)|_T$. Then the supported restriction

$$
\rho:R\Gamma_\Gamma(T,P)\longrightarrow R\Gamma_y(\Delta,\delta^*P)
$$

is zero in $D(A)$. In particular, this applies to $h=\Phi_X^m$, $m\geq1$,
and $L=\mathbb D_XK$ in Lemma [lemma-local-term-restriction-map].

There is also a $\Qbarl$-coefficient form. Let $k$ be an algebraically
closed extension of a finite field $k_0$ of characteristic different
from $\ell$, and let $X=X_0\times_{k_0}k$ be a separated smooth curve,
with $X_0$ of finite type over $k_0$. Let $m\geq1$ and
$K\in D^b_{\mathrm{ctf}}(X,\Qbarl)$. Use the graph convention $c=(\operatorname{id}_X,\Phi_X^m)$, put
$P'=K\boxtimes\mathbb D_XK$, and write $F=\Fix(c)$, with maps
$\iota:F\to X$ to the source of the graph and $d:F\to X$ to the
diagonal. If $z:\operatorname{Spec}k\to F$ has image $y\in X(k)$ and
$K_{\bar y}=0$, then the pullback along $z$ of

$$
\rho_{P'}:L\iota^*Rc^!P'\longrightarrow Rd^!L\delta^*P'
$$

is zero. Interchanging the two factors of $X\times_k X$ identifies
this convention with the transposed graph and
$\mathbb D_XK\boxtimes K$ of Lemma [lemma-local-term-restriction-map].

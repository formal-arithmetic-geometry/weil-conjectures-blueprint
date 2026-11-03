+++
id = "prose-03-05"
kind = "hidden"
title = "Pulling back to a scheme (2)"
order = 135
+++
Recall that the admissible coefficient rings are
$A,\Zl,\mathcal O_E,\Ql,E,\overline{\mathbf Q}_\ell$, where $E=\Ql$ is allowed. For $E=\Ql$
we write $\mathbf Z_{\ell,X}=\mathcal O_{\Ql,X}$ and
$\mathbf Q_{\ell,X}=(\Ql)_X$. By the lemma,

$$
\mathbf Z_{\ell,X}\simeq\varprojlim_n(\mathbf Z/\ell^n)_X,
\qquad
\mathbf Q_{\ell,X}\simeq\mathbf Z_{\ell,X}[1/\ell].
$$

For a condensed ring $\Lambda$ we write $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ for the
category of $\Lambda_X$-modules. Its derived category is
$D(X_{\mathrm{pro}\acute{e}t},\Lambda)$.

Duality and the trace map need, besides the constant sheaf, its twists
by roots of unity. The reason is already visible on $\mathbf P^1$ over an
algebraically closed field $k$, for $n$ invertible in $k$. The Kummer
sequence $0\to\mu_n\to\mathbf G_m\xrightarrow{n}\mathbf G_m\to0$ gives
$H^2(\mathbf P^1,\mu_n)\simeq\operatorname{Pic}(\mathbf P^1)/n=\mathbf Z/n$,
by the degree of a line bundle, and this involves no choice; in it the class
of a point is $1$. An identification of $H^2(\mathbf P^1,\mathbf Z/n)$
with $\mathbf Z/n$, on the other hand, requires an isomorphism
$\mu_n\simeq\mathbf Z/n$, that is, a choice of a primitive $n$th root of
unity, and Frobenius does not respect such a choice. Indeed, if $k$ is an
algebraic closure of $\mathbf F_q$, the arithmetic Frobenius acts on
$\mu_{\ell^n}(k)$ by $\zeta\mapsto\zeta^q$, so geometric Frobenius acts on
$\Lambda(1)$ by $q^{-1}$ and on
$H^2(\mathbf P^1,\Lambda)\simeq\Lambda(-1)$ by $q$, in accordance with
$\#\mathbf P^1(\mathbf F_q)=1+q$. Over $\mathbf C$ the twist is
$2\pi i\mathbf Z$: the exponential sequence identifies
$H^2(\mathbf P^1(\mathbf C),2\pi i\mathbf Z)$ with $\mathbf Z$, while an
identification of $H^2(\mathbf P^1(\mathbf C),\mathbf Z)$ with $\mathbf Z$ is a
choice of orientation, and the complex orientation depends on the choice
of $i$. With twists, the trace map
of $\mathbf P^1$ (Proposition [sk-prop-geo-p1-adjunction]) and smooth
purity $f^!\simeq f^*(d)[2d]$ (Theorem [sk-thm-purity-transport]) are
canonical and commute with Frobenius
(Proposition [sk-prop-prop-sp-frobenius-purity]); this is where the factor
$q^d$ in Poincaré duality (c) comes from, and $\Lambda(1)$ has weight
$-2$ (Definition [sk-d-real-weights]).

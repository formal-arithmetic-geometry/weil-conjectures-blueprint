+++
id = "prose-02-53"
kind = "hidden"
title = "Coefficient sheaves (3)"
order = 183
+++
Using the two-term resolution we see that, for every
complex $K$ of $\mathcal O_{E,X}$-modules, the derived reduction
$K\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n)_X$ is the cone of
$\pi_E^n:K\to K$ (Lemma [lemma-reduction-derived-nakayama]).

We call the rings $A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell$ the *admissible*
coefficient rings. Here $E=\mathbf Q_\ell$ is allowed, so that $\mathbf Z_\ell$ and $\mathbf Q_\ell$ are the
case $E=\mathbf Q_\ell$ of $\mathcal O_E$ and $E$. For $E=\mathbf Q_\ell$
we write $\mathbf Z_{\ell,X}=\mathcal O_{\mathbf Q_\ell,X}$ and
$\mathbf Q_{\ell,X}=(\mathbf Q_\ell)_X$. By the comparison lemma above,

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
an isomorphism
$H^2(\mathbf P^1,\mu_n)\simeq\operatorname{Pic}(\mathbf P^1)/n=\mathbf Z/n$,
given by the degree of a line bundle. This isomorphism involves no choice,
and it sends the class of a point to $1$. An identification of
$H^2(\mathbf P^1,\mathbf Z/n)$ with $\mathbf Z/n$, on the other hand,
requires an isomorphism $\mu_n\simeq\mathbf Z/n$, that is, a choice of a
primitive $n$th root of unity. Frobenius does not respect such a choice.

To see this, let $k$ be an algebraic closure of $\mathbf F_q$. The
arithmetic Frobenius acts on $\mu_{\ell^n}(k)$ by $\zeta\mapsto\zeta^q$.
The geometric Frobenius is the inverse of the arithmetic Frobenius in
$\operatorname{Gal}(k/\mathbf F_q)$. Hence it acts on $\Lambda(1)$ by
$q^{-1}$, and on $H^2(\mathbf P^1,\Lambda)\simeq\Lambda(-1)$ by $q$. This
agrees with $\#\mathbf P^1(\mathbf F_q)=1+q$.

Over $\mathbf C$ the twist is $2\pi i\mathbf Z$. The exponential sequence
identifies $H^2(\mathbf P^1(\mathbf C),2\pi i\mathbf Z)$ with $\mathbf Z$.
An identification of $H^2(\mathbf P^1(\mathbf C),\mathbf Z)$ with
$\mathbf Z$, by contrast, is a choice of orientation, and the complex
orientation depends on the choice of $i$.

With twists, the trace map of $\mathbf P^1$
(Proposition [proposition-adjunction-projective-line]) and smooth
purity $f^!\simeq f^*(d)[2d]$
(Theorem [theorem-smooth-purity-all-admissible-coefficients]) are
canonical and commute with Frobenius
(Proposition [proposition-purity-trace-commute-frobenius]). This is
where the factor $q^d$ in Poincaré duality (c) comes from.

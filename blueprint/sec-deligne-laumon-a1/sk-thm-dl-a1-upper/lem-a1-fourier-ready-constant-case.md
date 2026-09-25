+++
id = "lem-a1-fourier-ready-constant-case"
kind = "lemma"
title = "The geometrically constant case of the Fourier-ready reduction"
order = 2998
uses = ["def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-wf-boundary-semicontinuity"]
+++
Let $k_0=\mathbf F_q$, let $X_0=\mathbf P^1_{k_0}$, let
$j:U_0\hookrightarrow X_0$ be a dense open immersion with finite
complement $S_0$, and let $\mathcal F$ be a lisse Weil sheaf on
$U_0$, punctually $\iota$-pure
of weight $w$, whose pullback to $U=U_0\times_{k_0}k$ is
geometrically constant. Then for every $s\in S_0$ every eigenvalue
$\alpha$ of the local Frobenius $F_s$ on the compact-support group
$H_c^1(U,\mathcal F)$ in the convention of
[def-weil-ordinary-compact-cohomology] satisfies

$$
|\iota(\alpha)|^2\leq q_s^{w},
$$

which is the constant-coefficient case of the estimate $w+r$ of the
curve case at $r=1$.

## Proof

Geometric constancy means that the geometric monodromy of $\mathcal F$
is trivial; the inertia groups at the points of $S_0$ are quotients of
the geometric fundamental group, so $\mathcal F$ extends across
$S_0$, and the extension is the
middle extension $j_*\mathcal F$,
which is again geometrically constant.

The quotient $\mathcal G_0:=j_*\mathcal F/j_!\mathcal F$ is concentrated
on the finite set $S_0$, so
$H^1(X,j_*\mathcal F)=0$ — the coefficient is geometrically constant
and $X=\mathbf P^1_k$ has $H^1(\mathbf P^1_k,\bar{\mathbf Q}_\ell)=0$,
whereas for a curve of positive genus this step would fail — while
$H^0(X,\mathcal G_0)=\bigoplus_{s\in S_0}(j_*\mathcal F)_{\bar s}$ is
the direct sum of the boundary stalks. The long exact cohomology
sequence of $j_!\mathcal F\to j_*\mathcal F\to\mathcal G_0\to$
therefore exhibits

$$
H_c^1(U,\mathcal F)\cong H^1(X,j_!\mathcal F)
$$

as a *quotient* of $\bigoplus_{s\in S_0}(j_*\mathcal F)_{\bar s}$
(the connecting map is surjective because the next term
$H^1(X,j_*\mathcal F)$ vanishes).

The eigenvalues of the local Frobenius on a quotient are among those on
the ambient module. By the boundary semicontinuity
[lem-wf-boundary-semicontinuity], applied to the dense open
immersion $j$ with $\beta=w$, every eigenvalue of $F_s$ on the
boundary stalk $(j_*\mathcal F)_{\bar s}$ satisfies
$|\iota(\cdot)|^2\leq q_s^{w}$; summing over $s\in S_0$ gives the
bound on the ambient direct sum and hence on its quotient
$H_c^1(U,\mathcal F)$.

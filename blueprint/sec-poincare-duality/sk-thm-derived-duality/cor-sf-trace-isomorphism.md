+++
id = "cor-sf-trace-isomorphism"
kind = "theorem"
title = "The trace isomorphism"
order = 2615
tags = ["latex:corollary"]
uses = ["cor-cbc-proper-coincidence", "cor-sf-trace", "def-sf-datum", "def-sf-orientation", "def-weil-poincare-trace-cup", "prop-cohomological-finiteness"]
+++
In the setting of [def-sf-datum] and [def-sf-orientation], let
$X$ be smooth and geometrically connected of pure dimension $d$, and either
proper or of the form $X=X_0\times_{k_0}k$ for a smooth, separated
finite-type, geometrically connected $k_0$-scheme $X_0$ (properness is not
assumed). Then the trace map is an isomorphism

$$
\operatorname{tr}_X:H_c^{2d}\bigl(X,\Lambda(d)\bigr)\xrightarrow{\ \sim\ }\Lambda,
\qquad\text{equivalently}\qquad
H_c^{2d}(X,\Lambda)\cong\Lambda(-d),
$$

and the normalization ``the fundamental class goes to $1$'' is a convention
rather than a theorem. If $X$ is proper, then $H_c^{2d}=H^{2d}$ and this is
the trace isomorphism
$\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Lambda)\to\Lambda(-d)$.

## Proof

Take $K=\Lambda_X$ in [cor-sf-trace] and twist by $d$:
$R\Gamma_c(X,\Lambda(d))^\vee\cong R\Gamma(X,\Lambda)[2d]$ (no properness
is used there). Since $X$ is geometrically connected,
$H^0(X,\Lambda)=\Lambda$ with geometric Frobenius acting as the identity,
by the connectedness clause of [prop-cohomological-finiteness], which
needs neither properness nor smoothness; by the same proposition
$H^{-1}(X,\Lambda)=0$ and $H_c^j(X,\Lambda(d))=0$ for $j>2d$. Taking $H^{-2d}$ of both sides therefore gives
$H_c^{2d}(X,\Lambda(d))^\vee\cong\Lambda$: over a field the cohomology of
the dual is the dual of the cohomology, and at the integral and finite
stages the universal-coefficient sequence reduces to this, because the
$\operatorname{Ext}^1$-terms involve $H_c^{2d+1}=0$ and inject into
$H^{-1}(X,\Lambda)=0$. By the finiteness of the cohomology,
$H_c^{2d}(X,\Lambda(d))\cong\Lambda$, i.e.
$H_c^{2d}(X,\Lambda)\cong\Lambda(-d)$. The isomorphism so obtained is the
composite of the counit of $Ra_{X!}\dashv Ra_X^!$ with the orientation,
which is the trace map $\operatorname{tr}_X$ of
[def-weil-poincare-trace-cup] (its definition on $H_c^{2d}$ uses the
counit only, not properness); hence the normalization is a convention. If
$X$ is proper, [cor-cbc-proper-coincidence] identifies $Ra_{X!}$ with
$Ra_{X*}$, so $H_c^{2d}=H^{2d}$ and the untwisted form is
$\operatorname{tr}^{(-d)}_X$.

+++
id = "cor-sf-trace-isomorphism"
kind = "theorem"
title = "The trace isomorphism"
order = 3409
tags = ["latex:corollary"]
uses = ["cor-sf-trace", "def-sf-datum", "def-sf-orientation", "def-weil-poincare-trace-cup", "prop-cohomological-finiteness"]
+++
In the setting of [def-sf-datum] and [def-sf-orientation], let
$X$ be smooth, proper and geometrically connected of pure dimension $d$.
Then the trace isomorphism
$\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Lambda)\to\Lambda(-d)$ holds, and the
normalization ``the fundamental class goes to $1$'' is a convention rather
than a theorem.

## Proof

Take $K=\Lambda_X$ in [cor-sf-trace]: $R\Gamma_c(X,\Lambda)^\vee\cong R\Gamma(X,\Lambda)(d)[2d]$; since $X$ is proper,
$R\Gamma_c=R\Gamma$ by (A4), and since $X$ is geometrically connected
$H^0(X,\Lambda)=\Lambda$ with geometric Frobenius acting as the identity by
[prop-cohomological-finiteness]; taking $H^0$ of both sides and using
the finiteness of the cohomology gives
$\Lambda^\vee\cong H^{2d}(X,\Lambda)(d)$, i.e. $H^{2d}(X,\Lambda)\cong\Lambda(-d)$. The isomorphism so obtained is the
composite of the counit of $Ra_{X!}\dashv Ra_X^!$ with the orientation,
which is the trace map of [def-weil-poincare-trace-cup]; hence the
normalization is a convention.

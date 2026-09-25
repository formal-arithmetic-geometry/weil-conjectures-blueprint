+++
id = "sk-cor-trace"
kind = "section"
title = "The trace isomorphism"
order = 2586
uses = ["sk-def-trace-cup", "sk-lem-finite", "sk-thm-sf-identification"]
+++
*Corollary (sketch).*

In the setting of [sk-def-pairing] with $X_0$ in addition
*proper*, for the constant sheaf $K=\Lambda_X$,

$$
\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Lambda)\xrightarrow{\ \sim\ }
\Lambda(-d)
$$

is an isomorphism, and it is the map produced by the duality at $i=0$;
the normalization ``the fundamental class goes to $1$'' is therefore a
convention, not a theorem. (Blueprint 13, cor:sf-trace; 15,
cor:pod-constant-coefficients, thm:pod-trace-isomorphism.)

## Proof

Take $K=\Lambda_X$ in the proper case of [sk-thm-sf-identification]
and $i=0$: the
degreewise form reads $H^0_c(X,\Lambda)^\vee\cong H^{2d}(X,\Lambda)(d)$.
Since $X$ is proper, $Ra_{X!}\cong Ra_{X*}$ by [sk-def-ops] and hence
$H^0_c=H^0$; since $X$ is geometrically connected, $H^0(X,\Lambda)\cong \Lambda$ with the geometric Frobenius acting as the identity, which is the
$H^0$-clause of the finiteness interface
prop:cohomological-finiteness. Therefore
$\Lambda^\vee\cong H^{2d}(X,\Lambda)(d)$, i.e. $H^{2d}(X,\Lambda)\cong\Lambda(-d)$. The isomorphism produced this way is
the composite of the counit of $Ra_{X!}\dashv Ra_X^!$ with the orientation
[sk-thm-purity-transport], which is exactly the map
$\operatorname{tr}^{(-d)}_X$ of [sk-def-trace-cup]; the normalization
``the fundamental class goes to $1$'' is thus the choice of the canonical
generator of $H^{2d}\cong\Lambda(-d)$, not an additional statement.

Uses: [sk-def-trace-cup], [sk-lem-finite], [sk-thm-sf-identification]

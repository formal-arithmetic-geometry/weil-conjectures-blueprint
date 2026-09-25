+++
id = "sk-thm-sf-global-duality"
kind = "section"
title = "Global Verdier duality"
order = 2280
uses = ["sk-thm-sf-verdier-exchange"]
+++
*Theorem (sketch).*

Let $X$ be smooth, separated of finite type and geometrically connected of
pure dimension $d$ over $k$, with admissible structure morphism $a_X$.
Assume either that $X$ is proper, or that
$X=X_0\times_{k_0}k$ for a smooth, separated finite-type, geometrically
connected $k_0$-scheme $X_0$; in the latter case no properness is required.
For $K\in\Dctf(X,\Lambda)$ there is a canonical isomorphism

$$
\RG_c(X,K)^\vee\xrightarrow{\ \sim\ }\RG\bigl(X,\mathbb D_XK\bigr),
$$

in the point category $\Dbc(s,\Lambda)$ of def:weil-finite-coefficient-point,
natural in $K\in\Dctf(X,\Lambda)$ and compatible with finite reduction, scalar
extension and shifts; for $K=\Lambda_X$ it reads
$\RG_c(X,\Lambda)^\vee\cong\RG(X,\omega_X)$.

## Proof

Apply [sk-thm-sf-verdier-exchange] with $Y=\mathrm{Spec}\,k$ and
$f=a_X$: $\mathbb D_s(Ra_{X!}K)\cong Ra_{X*}\mathbb D_XK$. Evaluating at the
geometric point and using $\omega_s\cong\Lambda$ and
$\mathrm{Fib}_s(Ra_{X!}K)=\RG_c(X,K)$,
$\mathrm{Fib}_s(Ra_{X*}K)=\RG(X,K)$ turns the left-hand side into
$\RG_c(X,K)^\vee$ and the right-hand side into $\RG(X,\mathbb D_XK)$.

Uses: `\Cref{thm:sf-verdier-exchange}`, `def:weil-finite-coefficient-point`

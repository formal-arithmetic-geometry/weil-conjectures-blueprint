+++
id = "sk-thm-poincare-duality"
kind = "theorem"
title = "Poincaré duality"
order = 2796
uses = ["sk-cor-trace", "sk-def-pairing", "sk-def-set", "sk-def-sf-operations", "sk-def-trace-cup", "sk-def-weil", "sk-lem-finite", "sk-prop-sf-biduality-general", "sk-prop-sf-dualizable-biduality", "sk-thm-derived-duality", "sk-thm-frobenius", "sk-thm-purity-transport", "sk-thm-sf-global-duality", "sk-thm-sf-identification", "sk-thm-sf-kunneth-relative", "sk-thm-sf-package", "sk-thm-sf-tensor-hom", "sk-thm-sf-verdier-exchange", "sk-thm-transport"]
tags = ["sketch"]
+++
Let $p$ be prime, $a\ge1$, $q=p^a$, $k_0=\Fq$, $k=\overline{\mathbf F}_q$, $\ell\ne p$. Let $X_0/k_0$ be smooth, proper and geometrically
connected of pure dimension $d$, and put $X=X_0\times_{k_0}k$ with
structure morphism $a_X:X\to\Spec k$ (no admissibility hypothesis: the
exceptional adjoint used is the unconditional one of
[sk-def-sf-operations](vi), [sk-def-set]). Let
$K_X=(\Ql)_X$ with its canonical Weil structure, $F$ the geometric
Frobenius on $\RGamma(X,K_X)$ and on the $H^i(X,\Ql)$, and
$\langle-,-\rangle_i$ the trace–cup pairing with values in $\Ql(-d)$.
Then:

1. **(1)** *Trace.*
$\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Ql)\xrightarrow{\sim}\Ql(-d)$ is an
isomorphism;
1. **(2)** *Finiteness.* $H^i(X,\Ql)$ is
finite-dimensional for all $i$ and vanishes for $i\notin[0,2d]$;
1. **(3)** *Pairing.* $H^i(X,\Ql)\times H^{2d-i}(X,\Ql)\to\Ql(-d)$ is perfect for every $0\le i\le 2d$, and
$\langle y,x\rangle_{2d-i}=(-1)^i\langle x,y\rangle_i$;
1. **(4)** *Frobenius similitudine.* $F$ acts on
$\Ql(-d)$ by $q^d$ and
$\langle Fx,Fy\rangle_i=q^d\langle x,y\rangle_i$;
1. **(5)** *Reciprocity.*
$H^{2d-i}(X,\Ql)\cong H^i(X,\Ql)^\vee(-d)$ Frobenius-equivariantly, with
eigenvalues $q^d/\alpha$ on the left for the eigenvalues $\alpha$ of
$F$ on the right, with multiplicity;
1. **(6)** *Base change.* For every finite extension
$k_0'/k_0$ contained in $k$ with $r=[k_0':k_0]$, the geometric
Frobenius of $k_0'$ is $F^r$, the pairings remain perfect and
$\langle F^rx,F^ry\rangle_i=(q^r)^d\langle x,y\rangle_i$.

+++
id = "sk-thm-betti"
kind = "section"
title = "Betti symmetry and the endpoint factors"
order = 3214
uses = ["sk-def-cohfamily", "sk-def-roots", "sk-thm-intfactors", "sk-thm-poincare-duality", "sk-thm-rationality"]
+++
*Theorem (sketch).*

With $b_i=\deg P_i$ one has, for every $\ell\ne p$,

$$
b_i=\dim_{\Ql}H^{i}(X,\Ql),\qquad b_i=b_{2d-i},\qquad b_0=b_{2d}=1,
$$

and

$$
P_0(T)=1-T,\qquad P_{2d}(T)=1-q^{d}T .
$$

In particular $Z$ has a pole of order $1$ at $T=1$ and, if $d\ge1$, a pole of
order $1$ at $T=q^{-d}$.

## Proof

By [sk-thm-intfactors], $P_i^{(\ell)}=P_{i,\ell} =\det(1-TF_{i,\ell}\mid V_{i,\ell})$ with $V_{i,\ell}=H^{i}(X,\Ql)$, so
$b_i=\deg P_{i,\ell}=\dim V_{i,\ell}$, which is independent of $\ell$. The
symmetry $b_i=b_{2d-i}$ is [sk-thm-poincare-duality] (3). For the endpoints:
$X$ is geometrically connected, so $H^{0}(X,\Ql)=\Ql$ with $F$ acting
trivially, giving $P_0=1-T$ and $b_0=1$; and
$H^{2d}(X,\Ql)=\Ql(-d)$ with $F$ acting by $q^{d}$, giving
$P_{2d}=1-q^{d}T$ and $b_{2d}=1$. Both endpoint computations are
*geometric*, not linear-algebraic: the first uses that a geometrically
connected scheme has constant sheaf cohomology in degree $0$, the second uses
Poincaré duality in top degree together with the Frobenius normalization
$q^{d}$ on $\Ql(-d)$. The pole statements are read off from
[sk-thm-rationality] and the factorization
[sk-thm-tracetodeterminant].

Uses: [sk-def-cohfamily], [sk-def-roots], [sk-thm-intfactors], [sk-thm-poincare-duality], [sk-thm-rationality]

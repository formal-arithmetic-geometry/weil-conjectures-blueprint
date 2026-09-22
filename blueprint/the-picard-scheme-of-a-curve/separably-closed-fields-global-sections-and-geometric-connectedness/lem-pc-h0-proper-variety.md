+++
id = "lem-pc-h0-proper-variety"
kind = "lemma"
title = "Global sections of a proper scheme"
order = 4312
lean = ["AlgebraicGeometry.globalSections_isField_of_isProper", "AlgebraicGeometry.globalSections_eq_base_of_isGeometricallyIntegral"]
uses = ["def-pc-scheme", "def-pc-morphism-conventions", "lem-pc-coherent-hi", "lem-pc-finite-extension-alg-closed", "def-pc-geometrically-irreducible"]
+++
Let $k$ be a field and $X$ a proper scheme over $k$.

1. If $X$ is a variety over $k$ (e.g. connected and integral), then
   $H^0(X,\mathcal{O}_X)$ is a finite field extension of $k$.
2. If $X$ is geometrically integral over $k$, then
   $H^0(X,\mathcal{O}_X)=k$.

## Proof

(1) Put $A=H^0(X,\mathcal{O}_X)$. The structure morphism
$f:X\to\operatorname{Spec}(k)$ is proper, so by [lem-pc-coherent-hi] (with
$S=\operatorname{Spec}(k)$, $A=k$, $\mathcal{F}=\mathcal{O}_X$) the
$k$-vector space $A$ is finite dimensional. Since $X$ is a (connected,
integral) variety, $A$ is a domain: the restriction map
$H^0(X,\mathcal{O}_X)\to\kappa(\eta)$ to the generic point $\eta$ is
injective (the structure sheaf injects into the constant sheaf of the
function field of the integral $X$), so $A$ is a subring of a field. A
finite dimensional $k$-algebra which is a domain is a field: it is Artinian
(finite dimensional over a field), a finite product of local Artin rings,
and a domain has exactly one factor, so it is a local Artinian domain, i.e.
a field. Hence $A$ is a finite field extension of $k$.

(2) Since $X$ is proper over $k$ and $k\to\bar k$ is a flat ring map, the
flat base change for coherent cohomology of the divisors chapter gives
$H^0(X_{\bar k},\mathcal{O}_{X_{\bar k}})=A\otimes_k\bar k$. By part (1)
applied over the algebraically closed field $\bar k$ (the scheme
$X_{\bar k}$ is geometrically integral, hence integral and connected, and
proper over $\bar k$; it is a variety and (1) applies),
$A\otimes_k\bar k$ is a finite field extension of $\bar k$, hence equals
$\bar k$ [lem-pc-finite-extension-alg-closed]. Consequently
$A\otimes_k\bar k=\bar k$; since $A\to A\otimes_k\bar k$ is injective and
$A$ is finite over $k$, comparing dimensions gives that $A$ is
$1$-dimensional as a $k$-vector space, i.e. $A=k$.

*Import note.* The source's last parenthesis is a run of unfinished
dimension-counting attempts ("$\dim_k(A\otimes_k\bar k)=\dim_k(A)\cdot[\bar
k:k]$-style ... -free rank arguments"); the conclusion above states the
count it is reaching for — injectivity plus finiteness forces
$\dim_kA=1$ — and drops the abandoned phrasings.

Unresolved dependencies: lem:sc-flat-base-change-coherent

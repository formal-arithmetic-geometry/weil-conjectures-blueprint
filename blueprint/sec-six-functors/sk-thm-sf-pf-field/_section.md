+++
id = "sk-thm-sf-pf-field"
kind = "section"
title = "Projection formula: rational and algebraically closed stages"
order = 2097
uses = ["sk-thm-sf-pf-adic"]
lean = ["AlgebraicGeometry.Etale.hasProjectionFormula_field"]
+++
*Theorem (sketch).*

Let $f:X\to Y$ be a separated morphism of finite type, let $E/\Ql$ be a
finite extension inside $\Qlb$, and let $F$ be $E$ or $\Qlb$. Let $K$ and
$L$ be $\ell$-adic bounded constructible complexes of finite Tor amplitude
on $X$ and $Y$ with coefficients in $F$: over $E$, rationalizations of
derived-complete $\Dctf$-objects over $\mathcal O_E$; over $\Qlb$, objects
represented at a finite stage $E'/\Ql$ in this way. Then the projection map

$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^L L\longrightarrow Rf_!\bigl(K\otimes^L Lf^*L\bigr)
$$

is an isomorphism, compatibly with the extension functors and with finite
reduction of the integral representatives.

## Proof

Rationalization $-\otimes^L_{\mathcal O_E}E$ is exact, commutes with $Rf_!$,
$\otimes^L$ and $Lf^*$, and carries the mate-theoretic projection
transformation to the mate-theoretic projection transformation, since units
and counits are transported; an exact functor carries isomorphisms to
isomorphisms. For $\Qlb$ each object is represented over a finite stage by
def:weil-algebraically-closed-coefficients, and compatibility with scalar
extension makes the finite-stage system descend to the $2$-colimit.

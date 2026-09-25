+++
id = "sk-lem-sf-kunneth-star"
kind = "section"
title = "Ordinary Künneth with an identity factor"
order = 2217
uses = ["sk-prop-sf-comparison", "sk-rem-sf-pf-done", "sk-thm-smooth-base-change"]
+++
*Lemma (sketch).*

Let $f:X\to Y$ be a morphism of separated finite-type $k$-schemes, let $Z$ be
a further such scheme, and let $L\in\Dctf(X,\Lambda)$,
$Q\in\Dctf(Z,\Lambda)$. Then the canonical comparison

$$
Rf_*L\boxtimes Q\ \xrightarrow{\ \sim\ }\
R(f\times\operatorname{id}_Z)_*\bigl(L\boxtimes Q\bigr)
$$

is an isomorphism, natural in $L$ and $Q$.

## Proof

Write $p_X:X\times Z\to X$, $p_Z:X\times Z\to Z$ and $p_Y:Y\times Z\to Y$,
$p_Z':Y\times Z\to Z$ for the projections, so that
$p_Z=p_Z'\circ(f\times\operatorname{id}_Z)$ and the square with vertical maps
$f\times\operatorname{id}_Z$ and $f$ is Cartesian. The base morphism $p_Y$ is
a projection, hence smooth, so smooth base change
([sk-thm-smooth-base-change]) gives
$R(f\times\operatorname{id}_Z)_*p_X^*L\cong p_Y^*Rf_*L$. Writing the
external product as
$L\boxtimes Q=p_X^*L\otimes^L_\Lambda(f\times\operatorname{id}_Z)^*p_Z'^*Q$
and applying the projection formula ([sk-rem-sf-pf-done], discharging
fix-prop-projection-formula) to the right-hand side gives

$$
R(f\times\operatorname{id}_Z)_*\bigl(L\boxtimes Q\bigr)
\cong R(f\times\operatorname{id}_Z)_*\bigl(p_X^*L\bigr)
\otimes^L_\Lambda p_Z'^*Q
\cong p_Y^*Rf_*L\otimes^L_\Lambda p_Z'^*Q
= Rf_*L\boxtimes Q .
$$

Both steps are natural in $L$ and $Q$ by functoriality of base change and of
the projection formula, so the composite is the canonical comparison;
[sk-prop-sf-comparison] transports it between the coefficient stages. The
same statement is 0F1N and SGA 5, III, 1.1 and 1.6.4.

Uses: `\Cref{prop:sf-comparison}`, `\Cref{rem:sf-pf-done}`, `\Cref{thm:smooth-base-change}`, `fix-prop-projection-formula`

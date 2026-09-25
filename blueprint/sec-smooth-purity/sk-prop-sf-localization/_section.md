+++
id = "sk-prop-sf-localization"
kind = "section"
title = "Supported localization"
order = 1906
uses = ["sk-lem-sf-determination", "sk-prop-sf-closed-unit", "sk-prop-sf-open-closed-triangle"]
+++
*Proposition (sketch).*

Let $i:Z\hookrightarrow X$ be a closed immersion of finite-type $k$-schemes,
with complementary open $j:U\hookrightarrow X$. For $L\in\Dctf(X,\Lambda)$ at
a coefficient stage of [sk-def-sf-setting], the adjunction maps of
[sk-def-sf-operations] form a distinguished triangle

$$
Ri_*Ri^!L\longrightarrow L\longrightarrow Rj_*j^*L\xrightarrow{+1}.
$$

## Proof

This is the previous triangle turned around by adjunction. Apply
$\operatorname{Hom}(-,L)$ to the triangle of
[sk-prop-sf-open-closed-triangle] for an arbitrary
$M\in\Dctf(X,\Lambda)$ and rewrite the two outer terms. On the closed side,
$Ri_*=Ri_!$ and $Ri_!\dashv Ri^!$, then $i^*\dashv Ri_*$, give

$$
\operatorname{Hom}(Ri_*i^*M,L)\cong\operatorname{Hom}(i^*M,Ri^!L)
\cong\operatorname{Hom}(M,Ri_*Ri^!L);
$$

on the open side, $j_!\dashv j^*$ and $j^*\dashv Rj_*$ give

$$
\operatorname{Hom}(j_!j^*M,L)\cong\operatorname{Hom}(j^*M,j^*L)
\cong\operatorname{Hom}(M,Rj_*j^*L).
$$

So $\operatorname{Hom}(M,-)$ carries the two candidate maps — the counit
$Ri_*Ri^!L\to L$ and the unit $L\to Rj_*j^*L$ — to a long exact sequence,
for every $M$ and all shifts. Complete the counit to a distinguished triangle
$Ri_*Ri^!L\to L\to C\xrightarrow{+1}$. Comparing its long exact sequence with
the one above gives a natural isomorphism
$\operatorname{Hom}(M,C)\cong\operatorname{Hom}(M,Rj_*j^*L)$ in every degree,
so $C\cong Rj_*j^*L$ compatibly with the maps from $L$
([sk-lem-sf-determination] for the two-out-of-three step).
[sk-prop-sf-closed-unit] is what makes the first rewriting an isomorphism on
the nose rather than up to the unit.
Source: open–closed localization in SGA 4, XVII–XVIII; used in SGA 5, III,
proof of 1.7.4.

Uses: `\Cref{lem:sf-determination}`, `\Cref{prop:sf-closed-unit}`, `\Cref{prop:sf-open-closed-triangle}`

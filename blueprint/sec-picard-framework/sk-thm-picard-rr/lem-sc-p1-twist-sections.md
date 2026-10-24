+++
id = "lem-sc-p1-twist-sections"
kind = "lemma"
title = "Sections of the twists"
lean = ["AlgebraicGeometry.ProjectiveLine.nonempty_H_zero_twist_equiv_twistSectionPairs"]
order = 682
uses = ["def-sc-p1-standard"]
+++
Let $k$ be a field, $d\in\mathbf Z$, and let $\mathcal O(d)$
be a twisted structure sheaf as in [def-sc-p1-standard], with
generating section $g_0$ over $U_0=\Spec k[t]$ and generating
section $g_1$ over $U_1=\Spec k[s]$, $s=1/t$. Then the
sections of $\mathcal O(d)$ over $\mathbf P^1_k$ are exactly the
pairs $(p,q)\in k[t]\times k[s]$ with

$$
p(t)=t^{d}q(1/t)\qquad\text{in }k[t,t^{-1}],
$$

$p$ being the coefficient of $g_0$ over $U_0$ and $q$ the
coefficient of $g_1$ over $U_1$.

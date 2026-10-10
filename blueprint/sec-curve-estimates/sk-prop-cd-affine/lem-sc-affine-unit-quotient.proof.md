+++
kind  = "proof"
of    = "lem-sc-affine-unit-quotient"
+++
Choose $C\subseteq\overline C$ with finite complement $S$
by [lem-sc-compactification]. The divisor of a unit is
supported on $S$. Its divisor is zero if and only if it and its
inverse extend regularly to $\overline C$: this is the valuation
criterion in [lem-sc-divisor-class-curve]. Such an extended
unit belongs to $k^\times$ by [lem-sc-global-functions].
Consequently the divisor map identifies
$\mathcal O_C(C)^\times/k^\times$ with a subgroup $L$ of
$\bigoplus_{P\in S}\mathbf Z[P]$. A subgroup of a finite rank
free abelian group is finitely generated free, so $L/nL$ is finite.
The natural map from the unit group modulo powers to $L/nL$ is
surjective. It is injective: if $\operatorname{div}(u)=n\operatorname{div}(v)$
for a unit $v$, then $u/v^n\in k^\times$, which has an $n$-th
root because $k$ is algebraically closed. Thus $u$ is an
$n$-th power, and the desired quotient is isomorphic to $L/nL$.

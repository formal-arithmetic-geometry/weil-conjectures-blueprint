+++
id = "sk-prop-sf-finiteness"
kind = "proposition"
title = "Finiteness and constructibility"
order = 1704
lean = ["AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_hasInvertibleExponent", "AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerShriek"]
tags = ["sketch"]
+++
Let $\Lambda$ be a finite commutative ring whose exponent is invertible on
$X$ and let $f:X\to Y$ be a morphism of schemes locally of finite type over a
field $k$, with $Y$ quasi-compact (hence of finite type over $k$). If $f$ is quasi-compact, then $Rf_*$ carries $\Dbc(X,\Lambda)$ into
$\Dbc(Y,\Lambda)$ (*separatedness of $f$ is not needed*); if $f$ admits a
compactification, then
$Rf_!$ carries $\Dbc(X,\Lambda)$ into $\Dbc(Y,\Lambda)$, and if moreover $e$
bounds the dimensions of the geometric fibres, then $R^qf_!\mathcal F=0$ for
$q>2e$.
Moreover the torsion cohomological dimension of a finite-type $k$-scheme of
dimension $d$ over a field $k$ with $\mathrm{cd}_{\mathrm{tor}}(k)\le c$ is
bounded by $2d+c$; in particular $\mathrm{cd}_{\mathrm{tor}}(\Spec K)=0$ for
$K$ separably closed.

*Why $Y$ is assumed quasi-compact.* Bounded constructibility is not local on
$Y$: the bound on the cohomological degrees has to be uniform. Let
$f:\bigsqcup_{n\ge0}\mathbf P^n_k\to\bigsqcup_{n\ge0}\Spec k$ be the disjoint
union of the structure morphisms; it is proper (so quasi-compact, and it
admits a compactification), and $X$, $Y$ are locally of finite type over $k$.
The stalk of $R^{2n}f_*\Lambda=R^{2n}f_!\Lambda$ at the $n$-th point is
$H^{2n}(\mathbf P^n_{\bar k},\Lambda)\cong\Lambda(-n)\neq0$, so $Rf_*\Lambda$
is not bounded although $\Lambda_X\in\Dbc(X,\Lambda)$. The vanishing
$R^qf_!\mathcal F=0$ for $q>2e$ is local on $Y$ and holds without this
hypothesis.

+++
id = "det-prop-diagonal-tower-trace"
kind = "lemma"
title = "The $\\ell$-adic trace of the projective line and the integration identities"
lean = ["AlgebraicGeometry.ProEtale.diagonalTower_trace"]
order = 2751
uses = ["det-prop-diagonal-tower-limit", "sk-lem-geo-p1-cohomology", "sk-prop-geo-p1-adjunction", "thm-amb-p1-decomposition", "def-amb-p1-trace", "lem-amb-p1-diagonal-integrals"]
+++
Let $q:\mathbf P^1_Y\to Y$ be the projection, let $p_1,p_2$ be the two
projections of $W=\mathbf P^1_Y\times_Y\mathbf P^1_Y$, and let $\delta_{\Zl}$ be
the morphism of [det-prop-diagonal-tower-limit].

1. In the derived category of inverse systems on $Y_{\mathrm{proét}}$, the unit
   and the class of a section give an isomorphism
   $\mathbf Z/\ell^\bullet\oplus\mathbf Z/\ell^\bullet(-1)[-2]\xrightarrow{\sim}Rq_*\mathbf Z/\ell^\bullet$.
   Twisting by $(1)[2]$, projecting onto the second summand and applying
   $R\varprojlim$ defines a $\Zl$-linear trace
   $\operatorname{Tr}_q:Rq_*\Zl(1)[2]\to\Zl$ in $D(Y_{\mathrm{proét}},\Zl)$ whose
   reductions are the torsion traces of [sk-lem-geo-p1-cohomology]. The same
   construction over $\mathbf P^1_Y$ gives $\operatorname{Tr}_{p_i}$.
2. For $i=1,2$,
   $\operatorname{Tr}_{p_i}\circ Rp_{i*}(\delta_{\Zl})=1_{\Zl}$ in
   $D((\mathbf P^1_Y)_{\mathrm{proét}},\Zl)$, where $Rp_{i*}\Delta_*\Zl=\Zl$.

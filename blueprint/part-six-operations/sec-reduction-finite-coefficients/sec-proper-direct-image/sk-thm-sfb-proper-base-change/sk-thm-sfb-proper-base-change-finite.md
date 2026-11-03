+++
id = "det-thm-sfb-proper-base-change-finite"
kind = "lemma"
title = "Proper direct image, base change and projection formula for finite coefficients"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.finiteProperBaseChange"]
order = 2390
uses = ["sk-prop-ctf-finite-proper", "sk-thm-properbasechange", "sk-cor-pbc-proet-finite", "sk-thm-pe-constructible-comparison"]
+++
Let $A$ be a finite commutative ring killed by a power of $\ell$, and $p\colon X\to Y$ proper
between standing schemes.

1. $Rp_*$ maps $\Dctf(X,A)$ into $\Dctf(Y,A)$.
2. For a cartesian square with $g\colon Y'\to Y$, the base change map
   $g^*Rp_*K\to Rp'_*g'^*K$ is an isomorphism in $D(Y'_{\mathrm{proét}},A)$ for $K\in\Dctf(X,A)$.
3. For $K\in\Dctf(X,A)$ and $M\in\Dctf(Y,A)$ the projection formula map
   $Rp_*K\otimes^{\mathbf L}_AM\to Rp_*(K\otimes^{\mathbf L}_Ap^*M)$ is an isomorphism.

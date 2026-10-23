+++
id = "det-sp-thick-origin-homotopy"
kind = "lemma"
title = "The contraction of the thickened origin acts trivially"
order = 3579
uses = ["det-sp-defect-definition", "det-sp-dnc-base-change"]
+++
Let $X=\mathbf A^1_k$, $Z=V(x^m)$ with $m\geq1$, $M$ a finite $A$-module, and
$E=e^*\operatorname{Sp}_{X,Z}(M_X)$ with $\operatorname{Sp}_{X,Z}$ and $e$ as in
[det-sp-defect-definition]. For $a\in k$ let $H_a\colon X\to X$, $x\mapsto ax$. Since
$H_a^{\cdot}(x^m)=a^mx^m\in(x^m)$, each $H_a$ lifts to
$\widetilde H_a\colon\mathcal D_ZX\to\mathcal D_ZX$ by [det-sp-dnc-base-change], and $H_a$ induces
the identity on $Z_{\mathrm{red}}$. Let $\phi_a\colon E\to E$ be the endomorphism induced by the
pullback exchange for $\widetilde H_a$ (using $H_{a,\eta}^*M=M$ and the identification
$(H_a|_Z)^*E\simeq E$ given by nilpotent invariance). Then $\phi_1=\operatorname{id}_E$ and
$\phi_0=\phi_1$.

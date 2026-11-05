+++
id = "lemma-descent-vanishing-finite-etale"
kind = "lemma"
title = "Descent of vanishing along a finite étale cover"
order = 986
lean = ["AlgebraicGeometry.Etale.exists_rightDerivedPullback_app_comp_eq_smul", "AlgebraicGeometry.Etale.exists_sectionsRestriction_app_comp_eq_smul", "DerivedCategory.eq_zero_of_comp_trace_of_isUnit"]
+++
Let $f:W'\to W$ be a finite étale morphism of schemes of constant degree
$n$, with $n$ invertible in $A$, and let $L\in D(W_{\acute{e}t},A)$. Then the
pullback map $R\Gamma(W,L)\to R\Gamma(W',f^{-1}L)$ has a left inverse in
$D(A)$. In particular, a morphism $\alpha:M\to R\Gamma(W,L)$ in $D(A)$ is
zero if its composite with this pullback map is zero.

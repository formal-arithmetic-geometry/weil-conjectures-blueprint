+++
id = "sk-prop-ind-heart"
kind = "proposition"
title = "Ind-constructible sheaves"
order = 2422
uses = ["sk-def-sfb-constructible"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$. Recall that the ind-category $\operatorname{Ind}(\mathcal C)$ of a small category
$\mathcal C$ has as objects the filtered diagrams in $\mathcal C$ ("formal filtered colimits"), with
$\Hom(\varinjlim_\alpha C_\alpha,\varinjlim_\beta D_\beta)=\varprojlim_\alpha\varinjlim_\beta\Hom(C_\alpha,D_\beta)$.

Let $\IndCons(X,\Lambda)\subset\Mod(X_{\mathrm{proét}},\Lambda)$ be the full subcategory of filtered
colimits, computed in $\Mod(X_{\mathrm{proét}},\Lambda)$, of constructible sheaves
([sk-def-sfb-constructible]).

1. The functor $\operatorname{Ind}(\Cons(X,\Lambda))\to\Mod(X_{\mathrm{proét}},\Lambda)$ sending a formal
   filtered colimit to the actual colimit is fully faithful, with essential image
   $\IndCons(X,\Lambda)$.
2. $\IndCons(X,\Lambda)$ is closed in $\Mod(X_{\mathrm{proét}},\Lambda)$ under filtered colimits, direct
   sums, kernels, cokernels and extensions. In particular it is a Grothendieck abelian category and its
   inclusion is exact.

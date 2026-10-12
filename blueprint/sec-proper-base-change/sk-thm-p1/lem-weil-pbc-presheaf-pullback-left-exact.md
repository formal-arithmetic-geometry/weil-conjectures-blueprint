+++
id = "lem-weil-pbc-presheaf-pullback-left-exact"
kind = "lemma"
title = "The presheaf pullback along a left exact functor is left exact"
order = 1157
lean = ["CategoryTheory.lan_preservesFiniteLimits_of_preservesFiniteLimits"]
tags = ["mathlib", "stacks-00VC"]
+++
Let $\mathcal C,\mathcal D$ be categories whose objects and morphisms form sets (Stacks' convention for the underlying categories of sites), and $b:\mathcal C\to\mathcal D$ a functor. Let $\mathrm{PAb}(\mathcal C)$, $\mathrm{PAb}(\mathcal D)$ be the categories of presheaves of abelian groups (contravariant functors to abelian groups, natural transformations as morphisms). Let $b^p:\mathrm{PAb}(\mathcal D)\to\mathrm{PAb}(\mathcal C)$, $\mathcal G\mapsto\mathcal G\circ b$. For $Y\in\mathcal D$ let $\mathcal I_Y$ be the category of pairs $(X,\phi)$, $X\in\mathcal C$, $\phi:Y\to b(X)$, a morphism $(X,\phi)\to(X',\phi')$ being $f:X\to X'$ with $b(f)\circ\phi=\phi'$, and for $\mathcal F\in\mathrm{PAb}(\mathcal C)$ put

$$
 b_p\mathcal F(Y)=\varinjlim_{(X,\phi)\in\mathcal I_Y^{\mathrm{op}}}\mathcal F(X),
$$

with the restriction maps and functoriality induced by $(X,\phi)\mapsto(X,\phi\circ g)$ for $g:Y'\to Y$. Then:

1. $b_p:\mathrm{PAb}(\mathcal C)\to\mathrm{PAb}(\mathcal D)$ is a functor left adjoint to $b^p$: $\operatorname{Hom}(b_p\mathcal F,\mathcal G)\cong\operatorname{Hom}(\mathcal F,b^p\mathcal G)$ naturally in $\mathcal F,\mathcal G$;
2. if $\mathcal C$ has finite limits (a final object and fibre products) and $b$ commutes with them, then every $\mathcal I_Y^{\mathrm{op}}$ is filtered and $b_p$ commutes with finite limits; in particular for a morphism $\varphi:\mathcal F_1\to\mathcal F_2$ of abelian presheaves the map $b_p(\ker\varphi)\to\ker(b_p\varphi)$ is an isomorphism, kernels of presheaves being computed sectionwise.

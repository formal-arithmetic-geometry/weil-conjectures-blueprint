+++
id = "det-def-sfb-filtered-two-colimit-cocone"
kind = "definition"
title = "Cocones of categories"
order = 2576
+++
Let $I$ be a preordered set and $(\mathcal C_i)_{i\in I}$ a family of categories. A *cocone of
categories* over $(\mathcal C_i)$ with *vertex* a category $\mathcal D$ consists of

- for all $i\le j$ in $I$, a *transition functor* $T_{ij}\colon\mathcal C_i\to\mathcal C_j$;
- for all $i\in I$, a functor $\Phi_i\colon\mathcal C_i\to\mathcal D$;
- for all $i\le j$, a natural isomorphism $\theta_{ij}\colon\Phi_j\circ T_{ij}\xrightarrow{\sim}\Phi_i$,
  with components $\theta_{ij,x}\colon\Phi_j(T_{ij}x)\to\Phi_i(x)$ for $x\in\mathcal C_i$.

No compatibility between the $T_{ij}$ for different pairs (such as $T_{jk}T_{ij}\cong T_{ik}$),
nor between the $\theta_{ij}$, is part of the data. All categories and functors are ordinary ones.

+++
id = "sk-def-sfb-filtered-two-colimit"
kind = "definition"
title = "Filtered 2-colimits of categories"
order = 2575
lean = ["CategoryTheory.CategoryCocone", "CategoryTheory.CategoryCocone.EssSurjObj", "CategoryTheory.CategoryCocone.HomSurj", "CategoryTheory.CategoryCocone.HomInj", "CategoryTheory.CategoryCocone.IsFilteredTwoColimit", "CategoryTheory.CategoryCocone.IsFilteredTwoColimit.exists_iso", "CategoryTheory.CategoryCocone.IsFilteredTwoColimit.exists_map_eq"]
tags = ["sketch"]
+++
Let $I$ be a preordered set (in the applications a directed one) and $(\mathcal C_i)_{i\in I}$
categories. A *cocone of categories* with vertex a category $\mathcal D$ consists of

- transition functors $T_{ij}\colon\mathcal C_i\to\mathcal C_j$ for $i\le j$,
- functors $\Phi_i\colon\mathcal C_i\to\mathcal D$, and
- natural isomorphisms $\theta_{ij}\colon\Phi_j\circ T_{ij}\cong\Phi_i$ for $i\le j$.

No coherence between the transition functors is required. The cocone *is a filtered 2-colimit*
if it satisfies:

- **(Obj)** every object of $\mathcal D$ is isomorphic to $\Phi_i(x)$ for some $i\in I$ and
  $x\in\mathcal C_i$;
- **(Hom-surj)** for all $i,j\in I$, $x\in\mathcal C_i$, $y\in\mathcal C_j$ and every morphism
  $\varphi\colon\Phi_i(x)\to\Phi_j(y)$ there are $k\ge i,j$ and a morphism
  $g\colon T_{ik}x\to T_{jk}y$ in $\mathcal C_k$ with
  $\varphi=\theta_{jk,y}\circ\Phi_k(g)\circ\theta_{ik,x}^{-1}$;
- **(Hom-inj)** for every $k\in I$ and morphisms $g,g'\colon x\to y$ in $\mathcal C_k$ with
  $\Phi_k(g)=\Phi_k(g')$ there is $k'\ge k$ with $T_{kk'}(g)=T_{kk'}(g')$.

In particular, in a filtered 2-colimit every object of $\mathcal D$ comes from a finite stage,
and morphisms of $\mathcal C_k$ identified in $\mathcal D$ are identified at a finite stage.
This is a property of ordinary categories and functors; no higher categories are involved.

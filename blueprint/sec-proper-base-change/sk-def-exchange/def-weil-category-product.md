+++
id = "def-weil-category-product"
kind = "definition"
title = "Products of families of objects in a category; countable products"
order = 1046
lean = ["CategoryTheory.Limits.piObj, CategoryTheory.Limits.Pi.π, CategoryTheory.Limits.Pi.lift, CategoryTheory.Limits.Pi.map, CategoryTheory.Limits.HasCountableProducts"]
tags = ["sheaf-dag", "mathlib", "stacks-002I"]
+++
Let $\mathcal C$ be a category and $(K_i)_{i\in I}$ a family of objects of $\mathcal C$ indexed by a set $I$. A *product* of the family is an object $\prod_iK_i$ with morphisms $\mathrm{pr}_i:\prod_iK_i\to K_i$ (the *projections*) such that for every object $L$ and every family of morphisms $g_i:L\to K_i$ there is exactly one morphism $g=(g_i)_i:L\to\prod_iK_i$ with $\mathrm{pr}_i\circ g=g_i$ for all $i$. It is unique up to unique isomorphism compatible with the projections. For families $(K_i)$, $(K'_i)$ with products and morphisms $\varphi_i:K_i\to K'_i$, $\prod_i\varphi_i$ is the morphism $(\varphi_i\circ\mathrm{pr}_i)_i$. The category $\mathcal C$ *has countable products* if every family indexed by a countable set has a product.

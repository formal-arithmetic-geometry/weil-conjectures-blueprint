+++
id = "def-weil-pbc-category-colimit"
kind = "definition"
title = "Colimit of a diagram in a category"
lean = ["CategoryTheory.Limits.colimit"]
tags = ["sheaf-dag", "mathlib", "stacks-002D"]
+++
Let $I$ be a small category and $D:I\to\mathcal C$ a functor (a diagram). A *cocone* on $D$ is an object $L$ with morphisms $\iota_i:D(i)\to L$ such that $\iota_j\circ D(a)=\iota_i$ for every $a:i\to j$. A *colimit* of $D$ is a cocone $(\varinjlim_ID,(\iota_i))$ such that for every cocone $(M,(\mu_i))$ there is exactly one morphism $u:\varinjlim_ID\to M$ with $u\circ\iota_i=\mu_i$ for all $i$; it is unique up to unique isomorphism, and one is chosen when it exists. In particular a family of morphisms $\mu_i:D(i)\to M$ compatible with the transition maps induces the *canonical map* $\varinjlim_ID\to M$. The colimit is *filtered* when $I$ is a filtered category (Stacks, Categories, Definition 002V: $I$ has at least one object, every two objects map to a common object, every two parallel arrows are equalized by some arrow; a nonempty directed poset is filtered).

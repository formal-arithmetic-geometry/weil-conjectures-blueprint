+++
id = "lemma-connected-components-images-homomorphisms--1"
kind = "lemma"
title = "Connected components and images of homomorphisms (1)"
name_showing = false
order = 1720002
aliases = ["bp-r534-1"]
lean = ["AlgebraicGeometry.finite_connectedComponents", "AlgebraicGeometry.GrpObj.isClopen_connectedComponent_onePoint", "AlgebraicGeometry.instGrpObjOverSchemeSpecOfIdentityComponent", "AlgebraicGeometry.GrpObj.irreducibleSpace_identityComponent", "AlgebraicGeometry.GrpObj.range_conj_subset_connectedComponent", "AlgebraicGeometry.GrpObj.image_mulLeft_connectedComponent_onePoint", "AlgebraicGeometry.GrpObj.range_identityComponentTranslate"]
uses = []
+++
Let $k$ be a field and $G$ a group scheme of finite type over $k$.
Then $G$ has finitely many connected components, and its identity
component $G^\circ$ is an open, closed, irreducible normal subgroup
scheme.

Left translation by a rational point $g\in G(k)$ maps the connected
component of $1$ onto the connected component of $g$; this assertion
does not require $G$ to be of finite type. If $k$ is algebraically
closed and $G$ is of finite type, every connected component contains
such a point, so every component is a coset of $G^\circ$.

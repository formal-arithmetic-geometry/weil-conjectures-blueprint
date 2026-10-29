+++
id = "lem-weil-pbc-termwise-adjunction-homotopy"
kind = "lemma"
title = "An adjunction of additive functors induces an adjunction on the homotopy categories of complexes, termwise"
uses = ["def-weil-abstract-derived-category"]
lean = ["CategoryTheory.Adjunction.mapHomologicalComplex", "CategoryTheory.Adjunction.mapHomologicalComplex_unit_app_f", "CategoryTheory.Adjunction.mapHomologicalComplex_counit_app_f", "CategoryTheory.Adjunction.mapHomotopyCategory", "CategoryTheory.Adjunction.mapHomotopyCategory_unit_app_quotient", "CategoryTheory.Adjunction.mapHomotopyCategoryPlus"]
order = 1413
tags = ["stacks-08BJ"]
+++
Let $\mathcal A,\mathcal B$ be additive categories, $v:\mathcal B\to\mathcal A$ left adjoint to $u:\mathcal A\to\mathcal B$ with $u,v$ additive, unit $\eta:\mathrm{id}\to uv$ and counit $\varepsilon:vu\to\mathrm{id}$. For cochain complexes write $v(M)=(v(M^r),v(d^r))_r$ and $u(I)=(u(I^r),u(d^r))_r$, and $K(\mathcal A)$, $K(\mathcal B)$ for the homotopy categories (cochain complexes, morphisms of complexes modulo homotopy) [def-weil-abstract-derived-category]. Then: (a) the termwise maps $\eta_M=(\eta_{M^r})_r:M\to u(v(M))$ and $\varepsilon_I=(\varepsilon_{I^r})_r:v(u(I))\to I$ are morphisms of complexes, natural in $M$ and $I$, and make the termwise functors adjoint, $v\dashv u$, on the categories of complexes; (b) $u$ and $v$ carry homotopic morphisms to homotopic morphisms, so induce functors $v:K(\mathcal B)\to K(\mathcal A)$, $u:K(\mathcal A)\to K(\mathcal B)$, and these are adjoint with unit and counit the homotopy classes of $\eta_M$ and $\varepsilon_I$; in particular

$$
 \operatorname{Hom}_{K(\mathcal A)}(v(M),I)\xrightarrow{\ \sim\ }\operatorname{Hom}_{K(\mathcal B)}(M,u(I)),\qquad [f ]\longmapsto[u(f)\circ\eta_M],
$$

with inverse $[g ]\mapsto[\varepsilon_I\circ v(g)]$, is a bijection natural in $M\in K(\mathcal B)$ and $I\in K(\mathcal A)$; (c) both functors preserve bounded below complexes, and the same holds on the homotopy categories $K^+$ of bounded below complexes.

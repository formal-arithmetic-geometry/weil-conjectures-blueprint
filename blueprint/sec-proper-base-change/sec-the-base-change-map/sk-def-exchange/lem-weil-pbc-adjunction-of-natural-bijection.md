+++
id = "lem-weil-pbc-adjunction-of-natural-bijection"
kind = "lemma"
title = "An adjunction from hom-set bijections natural in both variables"
lean = ["CategoryTheory.Adjunction.mkOfHomEquiv"]
order = 1410
tags = ["mathlib", "stacks-0037"]
+++
Let $F:\mathcal C\to\mathcal D$ and $G:\mathcal D\to\mathcal C$ be functors and let $\Psi_{X,Y}:\operatorname{Hom}_{\mathcal D}(FX,Y)\to\operatorname{Hom}_{\mathcal C}(X,GY)$ be bijections, natural in $X\in\mathcal C$ and $Y\in\mathcal D$: $\Psi_{X',Y}(a\circ F(f))=\Psi_{X,Y}(a)\circ f$ and $\Psi_{X,Y'}(b\circ a)=G(b)\circ\Psi_{X,Y}(a)$. Then $F\dashv G$ is an adjunction with hom bijection $\Psi$: the morphisms $\eta_X=\Psi_{X,FX}(\mathrm{id}_{FX}):X\to GFX$ and $\varepsilon_Y=\Psi_{GY,Y}^{-1}(\mathrm{id}_{GY}):FGY\to Y$ are natural transformations $\eta:\mathrm{id}\to GF$ (unit) and $\varepsilon:FG\to\mathrm{id}$ (counit) satisfying the triangle identities, and $\Psi_{X,Y}(a)=G(a)\circ\eta_X$, $\Psi^{-1}_{X,Y}(b)=\varepsilon_Y\circ F(b)$.

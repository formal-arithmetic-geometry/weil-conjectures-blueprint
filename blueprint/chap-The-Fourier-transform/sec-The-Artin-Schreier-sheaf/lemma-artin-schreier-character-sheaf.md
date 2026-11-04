+++
id = "lemma-artin-schreier-character-sheaf"
kind = "lemma"
title = "The Artin–Schreier character sheaf"
order = 1211
lean = ["AlgebraicGeometry.artinSchreier", "AlgebraicGeometry.isLisse_artinSchreier", "AlgebraicGeometry.nonempty_iso_tensorObj_artinSchreierOf", "AlgebraicGeometry.nonempty_iso_dual_artinSchreier", "AlgebraicGeometry.WeilSheaf.traceFunction_artinSchreier", "AlgebraicGeometry.isPunctuallyPureOfWeight_artinSchreier"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-trace-function", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
Let $\psi:k_0\to E^\times$ be a nontrivial additive character.
There is a lisse rank-one $E$-sheaf $\mathcal L_\psi$ on
$\mathbf A^1_{k_0}$, with a specified trivialization at zero, such that

$$
m^*\mathcal L_\psi\simeq
\operatorname{pr}_1^*\mathcal L_\psi\otimes
\operatorname{pr}_2^*\mathcal L_\psi,
\qquad
\mathcal L_\psi^\vee\simeq\mathcal L_{\psi^{-1}}.
$$

Here $m$ is the addition map, and the isomorphisms respect the
trivializations at zero. For $x\in\mathbf F_{q^n}$, the Frobenius
trace is

$$
t_{\mathcal L_\psi,n}(x)
=\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(x)\bigr).
$$

In particular $\mathcal L_\psi$ is pure of weight zero.

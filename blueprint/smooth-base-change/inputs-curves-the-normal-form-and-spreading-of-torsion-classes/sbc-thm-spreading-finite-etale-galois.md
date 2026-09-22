+++
id = "sbc-thm-spreading-finite-etale-galois"
kind = "theorem"
title = "Spreading a finite étale Galois cover"
order = 5140
lean = ["AlgebraicGeometry.exists_galoisCover_extending_genericFiber"]
uses = ["def-sbc-normal-dominant-galois", "def-sbc-smooth-morphisms"]
+++
Let $S$ be a quasi-compact and quasi-separated integral normal
[def-sbc-normal-dominant-galois] scheme with generic point $\eta$. Let
$C\to S$ be a quasi-compact and quasi-separated smooth
[def-sbc-smooth-morphisms] morphism with geometrically connected fibres, and
fix a section $\sigma:S\to C$. Let $Z\to C_\eta$ be a finite étale Galois
cover with group $G$, assume $|G|$ is invertible on $S$, and assume $Z$ has
a $\kappa(\eta)$-rational point mapping to $\sigma(\eta)$. Then there is a
finite étale Galois cover $\widetilde Z\to C$ with group $G$ whose
restriction to $C_\eta$ is the given cover $Z\to C_\eta$.

(*Stacks Project, Fundamental Groups of Schemes, [Tag
0EZJ](https://stacks.math.columbia.edu/tag/0EZJ) = Lemma 58.31.9.*)

## Proof

This is the recorded classical input named in the statement, Stacks Project,
Fundamental Groups of Schemes, Lemma 58.31.9 ([Tag
0EZJ](https://stacks.math.columbia.edu/tag/0EZJ)): a finite étale Galois
cover of the generic fibre whose group has order invertible on the base
spreads out to a finite étale Galois cover of the whole smooth family with
geometrically connected fibres. The blueprint uses it in this form; no
separate proof is given.

Unresolved dependencies: def:weil-pbc-scheme-conventions

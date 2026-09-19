+++
id = "lemma-weil-pbc-epsilon-adjunction-equations-v1"
kind = "lemma"
title = "Naturality and triangle equations for the comparison adjunction"
order = 807
uses = ["def-weil-pbc-epsilon-unit-counit", "lemma-weil-pbc-epsilon-counit-representative-descent-v1", "lemma-weil-pbc-epsilon-geometric-morphism-construction-v1"]
+++
The displayed unit and counit are natural in coefficient sheaves and satisfy
the two triangle identities. Their components commute with restriction on
both sites.

## Proof

For $\alpha:F\to F'$, both routes around the unit naturality square send
$s\in F(U)$ to $(1_{\iota_XU},\alpha_U(s))$. For $\beta:G\to G'$, both
routes around the counit square send $(a,s)$ to
$\beta_W(G(a)(s))=G'(a)(\beta_{\iota_XU}(s))$. These equalities commute
with restriction and descend to sheaves by the preceding lemma.

A local section of $\epsilon_X^{-1}F$ is represented by $(a,s)$. The first
triangle composite replaces $s$ by its identity representative and evaluates
along $a$, returning $(a,s)$. A section
$s\in(\epsilon_{X,*}G)(U)=G(\iota_XU)$ is sent by the second composite to
$(1_{\iota_XU},s)$ and then evaluated along the identity, returning $s$.
Local representatives detect sheaf maps, so both composites are identities.

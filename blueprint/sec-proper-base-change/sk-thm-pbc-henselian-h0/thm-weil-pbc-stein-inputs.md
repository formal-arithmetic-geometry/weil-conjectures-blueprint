+++
id = "thm-weil-pbc-stein-inputs"
kind = "theorem"
title = "The two classical inputs of Stein connectedness"
lean = ["AlgebraicGeometry.Scheme.Hom.isFinite_steinFactorizationBase", "AlgebraicGeometry.Scheme.Hom.isConnected_inter_preimage_zeroLocus"]
order = 1650
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-stein-factorization", "def-weil-pbc-scheme-conventions"]
tags = ["latex:openproblem"]
+++
Let $A$ be a commutative ring, $S=\operatorname{Spec}A$, and let $p:Y\to S$ be
proper [def-weil-pbc-scheme-conventions], with Stein factorization
$Y\to\operatorname{Spec}B\to S$, $B=H^0(Y,\mathcal O_Y)$
[def-weil-pbc-stein-factorization].

- (i) *Finiteness.* If $A$ is Noetherian, then $A\to B$ is finite, i.e. the
  second map $\operatorname{Spec}B\to S$ of the Stein factorization is finite.
- (ii) *Connectedness.* If $(A,I)$ is a henselian pair
  [def-weil-pbc-henselian-terminology], then every irreducible closed subset
  $C$ of $Y$ meets the closed fibre $Y_0=p^{-1}(V(I))$ in a nonempty connected
  subset.

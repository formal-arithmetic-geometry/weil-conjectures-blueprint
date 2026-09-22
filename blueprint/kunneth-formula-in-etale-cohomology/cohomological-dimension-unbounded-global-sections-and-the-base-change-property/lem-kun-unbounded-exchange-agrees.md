+++
id = "lem-kun-unbounded-exchange-agrees"
kind = "lemma"
title = "The unbounded exchange extends the bounded exchange"
order = 6046
lean = ["AlgebraicGeometry.Etale.unboundedExchange_eq_derivedExchange"]
uses = ["def-weil-pbc-underived-exchange", "def-kun-unbounded-exchange", "def-weil-pbc-derived-exchange"]
+++
For $K\in\Dplus(X_{\Et})$ the exchange morphism $\Ex_{\square,K}$ of
[def-kun-unbounded-exchange] is the exchange morphism of
[def-weil-pbc-derived-exchange]; in particular for sheaves (complexes
concentrated in degree $0$) with $\Lambda$-module structure it agrees with
the underived exchange morphism.

## Proof

Both morphisms are defined as the same adjoint mate of the same composite
and are independent of the K-injective model, so they agree.

Unresolved dependencies: lem:weil-pbc-derived-exchange-replacement

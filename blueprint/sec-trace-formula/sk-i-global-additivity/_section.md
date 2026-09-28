+++
id = "sk-i-global-additivity"
kind = "section"
title = "Compact trace additivity"
order = 2372
uses = ["sk-d-operator", "sk-d-six", "sk-d-trace", "sk-d-weil", "sk-p-trace", "sk-prop-sf-open-closed-triangle", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.trace_globalOperator_eq_trace_add_trace"]
+++
*Proposition (sketch).*

For a closed immersion $i_0:Z_0\hookrightarrow X_0$ and its open
complement $j_0:U_0\hookrightarrow X_0$, the induced
Frobenius coefficient morphisms on the functorial
compact localization triangle satisfy

$$
\tr_A(F_{c,m},R\Gamma_c(X,K))=
\tr_A(F_{c,m},R\Gamma_c(U,j^*K))+
\tr_A(F_{c,m},R\Gamma_c(Z,i^*K)).
$$

These are traces of perfect complexes; invertibility
of the coefficient morphism is unnecessary.

## Proof

Applying compact cohomology to [sk-prop-sf-open-closed-triangle] gives a
functorial compact localization triangle, and
compact cohomology of a finite-Tor constructible complex is perfect, so the
three global operators form an endomorphism of a distinguished triangle of
perfect complexes. Triangle additivity of the ordinary categorical trace
in [sk-p-trace] applied to that endomorphism gives the displayed
identity. Only exactness of the global operator and the formal laws of the
trace are used; no trace of an individual, possibly nonperfect,
cohomology module occurs, and the coefficient morphism need not be
invertible.

Uses: [sk-d-six], [sk-d-trace], [sk-d-weil], [sk-p-trace], [sk-prop-sf-open-closed-triangle], [sk-thm-sf-package]

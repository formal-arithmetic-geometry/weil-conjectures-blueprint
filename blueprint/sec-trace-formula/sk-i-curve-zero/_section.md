+++
id = "sk-i-curve-zero"
kind = "section"
title = "Zero-stalk vanishing on a smooth curve"
order = 2341
uses = ["sk-d-curve-pieces", "sk-d-local-term", "sk-d-trace-class", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.localTerm_traceClass_eq_zero_of_isZero"]
+++
*Proposition (sketch).*

In the smooth-curve setting, if $K_{\bar x}=0$
then the local term $\LT_{\bar x}(\varphi_m)$ is
zero. The same holds for an arbitrary Frobenius coefficient morphism
$\Phi_m^*K\to K$.

## Proof

The fixed point $\bar x$ is an isolated, hence open-and-closed, component of
the fixed scheme. The trace-class source is the internal Hom
$\RHom(c_2^*K,c_1^!K)$; by purity in relative dimension zero in
[sk-thm-sf-package], which identifies $c_1^!K$ and $c_2^*K$ with $K$ on the fixed
scheme, its stalk at $\bar x$ is $\RHom(K_{\bar x},K_{\bar x})$, and the
mate of the coefficient morphism restricts to the mate of $u_{\bar x}$.
The trace map is the composite of an evaluation, the fixed-square base
change and the dualizing composition, each local on the fixed scheme, so
its restriction to the component $\bar x$ is computed from
$(K_{\bar x},u_{\bar x})$ alone. A vanishing stalk therefore forces the
restriction, and with it the local term, to vanish. Locality uses no
invertibility, so the coefficient-morphism form follows at the same time.

Uses: [sk-d-curve-pieces], [sk-d-local-term], [sk-d-trace-class], [sk-thm-sf-package]

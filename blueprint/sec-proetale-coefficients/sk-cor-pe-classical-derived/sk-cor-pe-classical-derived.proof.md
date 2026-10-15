+++
kind = "proof"
of = "sk-cor-pe-classical-derived"
uses = ["det-pe-classical-derived-weak-serre", "det-pe-classical-derived-equivalence"]
+++
Kernels and cokernels are handled by exactness and full faithfulness of
$\nu_X^*$ ([sk-thm-pe-classical-sheaves]). Given an extension of two classical
sheaves, apply $\nu_{X,*}$; since $R^1\nu_{X,*}\nu_X^*F=0$, the result is a short
exact sequence whose pullback is the original extension
([det-pe-classical-derived-weak-serre]). By the derived unit of
[sk-prop-sf-comparison] every classical sheaf is $\nu_{X,*}$-acyclic, so the
bounded-below hypercohomology spectral sequence, or equivalently induction on
truncations, reduces the counit $\nu_X^*R\nu_{X,*}K\to K$ in
$D^+(X_{\Proet},\Lambda)$ to the comparison for sheaves. Hence it is an
isomorphism for every bounded-below complex with classical cohomology sheaves,
whatever its terms (Stacks Project, Tag 09B1;
[det-pe-classical-derived-equivalence]).

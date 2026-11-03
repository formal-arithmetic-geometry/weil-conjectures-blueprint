+++
kind = "proof"
of = "det-def-sfb-sheaf-tensor-closed"
+++
Using the adjunction $a\dashv$ (inclusion), the presheaf adjunction of
[det-def-sfb-sheaf-tensor-presheaf], and full faithfulness of the inclusion of sheaves,
$$
\Hom_{\Sh}\bigl(a(\mathcal F\otimes_p\mathcal G),\mathcal H\bigr)\cong\Hom_{\mathrm{PSh}}(\mathcal F\otimes_p\mathcal G,\mathcal H)\cong\Hom_{\mathrm{PSh}}(\mathcal G,[\mathcal F,\mathcal H])=\Hom_{\Sh}(\mathcal G,[\mathcal F,\mathcal H]),
$$
the last because $[\mathcal F,\mathcal H]$ is a sheaf. Each step is natural. So
$\mathcal F\otimes-$ is left adjoint to $\mathcal{H}om(\mathcal F,-)$ and preserves all
colimits; by the symmetry, so does $-\otimes\mathcal F$. A colimit-preserving functor between
abelian categories preserves finite biproducts and cokernels, so it is additive and right exact.

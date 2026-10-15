+++
kind = "proof"
of = "det-pe-products-exact"
+++
Products of sheaves are computed sectionwise ([det-pe-sections-limits-colimits]). Let $W$
be an affine weakly contractible object. By [det-pe-wc-sections-exact] each
$0\to A_i(W)\to B_i(W)\to C_i(W)\to0$ is an exact sequence of $\mathcal R(W)$-modules. A
product of exact sequences of modules is exact: kernels and images are computed
coordinatewise, and for surjectivity a tuple $(c_i)\in\prod_iC_i(W)$ lifts to
$(b_i)\in\prod_iB_i(W)$ by choosing a preimage $b_i$ of each $c_i$ (axiom of choice). Hence
the evaluation at $W$ of the product sequence is exact for every such $W$, and by
[det-pe-sections-conservative] the product sequence of sheaves is exact.

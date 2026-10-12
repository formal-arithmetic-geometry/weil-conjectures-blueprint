+++
kind  = "proof"
of    = "lem-sfb-finite-upper-star-braided"
+++
The structure map $\delta_{F,G}\colon g^*(F\otimes G)\to g^*F\otimes g^*G$ is the
adjoint of $(\eta_F\otimes\eta_G)$ followed by the lax structure map of $g_*$, with $\eta$
the unit of $g^*\dashv g_*$. The braiding commutes with this composite by naturality of the
braiding and the compatibility of the lax structure of $g_*$ with the braiding
([def-sfb-finite-lower-star-lax-monoidal]). Transposing back gives

$$
\beta_{g^*F,g^*G}\circ\delta_{F,G}=\delta_{G,F}\circ g^*(\beta_{F,G}).
$$

Since $\delta$ is invertible, this is the compatibility of the strong monoidal structure with
the symmetries.

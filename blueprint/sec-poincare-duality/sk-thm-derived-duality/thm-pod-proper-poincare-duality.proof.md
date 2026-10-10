+++
kind  = "proof"
of    = "thm-pod-proper-poincare-duality"
+++
Step 1: the comparison of the global-section functors. Since $X_0$ is proper by hypothesis, so is its base change $X$, and the structure morphism $a_X$ is proper; so by [cor-cbc-proper-coincidence] the canonical comparison $Ra_{X!}\to Ra_{X*}$ is an isomorphism, giving the canonical identification $R\Gamma _c(X,K)\cong R\Gamma (X,K)$ of [def-pod-derived-poincare-pairing] used in the construction. Step 2: transport of the pairing. The derived Poincare pairing $\beta _K$ of [thm-pod-derived-poincare-duality] is a morphism of the complex $R\Gamma _c(X,K)\otimes ^L_A R\Gamma (X,K^\vee (d))[2d]$ into $A$, so it transports along the identification of the first factor to the displayed pairing of $R\Gamma (X,K)\otimes _A^LR\Gamma (X,K^\vee (d))[2d]\to A$. Step 3: the adjoint. The adjoint of the transported pairing is the transported adjoint (the tensor–internal-Hom adjunction is functorial in both variables, and the identification of the first factor is transported back and forth by that canonical isomorphism), so the inverse of the transported adjoint

$$
R\Gamma (X,K)^\vee \xrightarrow {\  \sim \  }R\Gamma \bigl(X,K^\vee (d)\bigr)[2d]
$$

is the canonical isomorphism of [thm-pod-derived-poincare-duality] read through the identification, in particular it is a canonical isomorphism. Step 4: the degreewise forms. These are the field-stage part of [thm-pod-derived-poincare-duality], namely [thm-pod-degreewise-perfectness-over-a-field], with the twist elimination of [prop-pod-degree-of-the-pairing]; the finite dimensionality and the perfectness statements of the theorem are the ones of those two statements (for the proper $X$, $H_c^i=H^i$), so no further input is needed.

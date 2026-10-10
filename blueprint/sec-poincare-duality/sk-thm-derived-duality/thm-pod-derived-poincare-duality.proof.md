+++
kind  = "proof"
of    = "thm-pod-derived-poincare-duality"
+++
Step 1: the two constituent isomorphisms. By [thm-pod-global-verdier-duality] there is the canonical isomorphism

$$
R\Gamma _c(X,K)^\vee \xrightarrow {\  \sim \  }R\Gamma (X,\mathbb D_XK),
$$

and by [thm-sf-dual-perfect] (its hypothesis being the perfectness of $K$ over $\Lambda _X$) there is the canonical identification

$$
R\Gamma (X,\mathbb D_XK)\xrightarrow {\  \sim \  } R\Gamma \bigl(X,K^\vee (d)\bigr)[2d].
$$

Step 2: the composite is the inverse of the adjoint of the pairing. By [thm-pod-identification-of-the-comparison], the adjoint of the derived pairing $\beta _K$ of [def-pod-derived-poincare-pairing] is the inverse of the composite of these two isomorphisms; hence the composite is an isomorphism if and only if the pairing is perfect, by the definition of [def-pod-perfect-derived-pairing]. Step 3: perfectness of the objects. By [thm-pod-point-perfectness], $R\Gamma _c(X,K)$ is a perfect point complex in the sense of [def-pod-perfect-point-complex]; its dual $R\Gamma _c(X,K)^\vee$ is perfect by [def-pod-perfect-point-complex] (the dual of a bounded complex of finite projective modules is again a bounded complex of finite projective modules), and the shift of a perfect point complex is perfect, again by [def-pod-perfect-point-complex]. Step 4: the conclusion. The composite is an isomorphism by Step 1, and its two objects are perfect by Step 3; hence the adjoint of $\beta _K$ is an isomorphism and $\beta _K$ is a perfect derived pairing according to [def-pod-perfect-derived-pairing]. Step 5: naturality and compatibility. Both constituent isomorphisms are natural in $K$ and compatible with finite reduction, scalar extension, shifts, and truncations, by the statements of [thm-pod-global-verdier-duality], [thm-sf-dual-perfect], and [thm-pod-point-perfectness], so the composite and the pairing inherit these properties; the transpose form is the pairing of [def-pod-derived-poincare-pairing] itself. Step 6: the inputs, separated. The first isomorphism of Step 1 is the abstract global duality [thm-sf-global-duality] in its concrete form (valid without properness: $Ra_{X!}$ and $Ra_{X*}$ enter as different functors and are never compared), and the second is the smooth-purity orientation [thm-pur-finite-coefficient-smooth-purity] of the purity chapter; the identification consumed in Step 2 is [thm-sf-identification], and the finiteness consumed in Step 3 is [thm-pod-point-perfectness].

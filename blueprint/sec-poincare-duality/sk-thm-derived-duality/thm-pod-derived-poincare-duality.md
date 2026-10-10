+++
id = "thm-pod-derived-poincare-duality"
kind = "theorem"
title = "Derived Poincare duality"
order = 2438
uses = ["def-pod-derived-poincare-pairing", "def-pod-perfect-derived-pairing", "def-pod-perfect-point-complex", "thm-pod-global-verdier-duality", "thm-pod-identification-of-the-comparison", "thm-pod-point-perfectness", "thm-pur-finite-coefficient-smooth-purity", "thm-sf-dual-perfect", "thm-sf-global-duality", "thm-sf-identification"]
+++
In the Poincare duality conventions of this chapter (the fixed setting; $X_0$ is not assumed proper), let $\Lambda \in \{ A,\mathcal O_E,E,\overline{\mathbf Q}_{\ell }\}$, let $K\in D^b_{ctf}(X,\Lambda )$ be a bounded constructible finite-Tor complex that is perfect over $\Lambda _X$, let $K^\vee =R\mathcal Hom_X(K,\Lambda _X)$ be its coefficient dual with Tate twist $K^\vee (d)$, and let $\beta _K$ be the derived Poincare pairing (the composite of the mixed-support cup product, the evaluation, and the normalized smooth trace). Then $\beta _K$ is a perfect derived pairing in the sense of [def-pod-perfect-derived-pairing]: the inverse of its tensor–internal-Hom adjoint is the canonical isomorphism

$$
R\Gamma _c(X,K)^\vee \xrightarrow {\  \sim \  } R\Gamma \bigl(X,K^\vee (d)\bigr)[2d].
$$

The statement is natural in $K$, compatible with finite reduction, scalar extension, shifts and truncations, and its transpose form

$$
R\Gamma _c(X,K)\otimes _\Lambda ^LR\Gamma \bigl(X,K^\vee (d)\bigr)[2d] \longrightarrow \Lambda
$$

is the pairing of [def-pod-derived-poincare-pairing].

+++
kind  = "proof"
of    = "thm-trf-lefschetz-verdier"
+++
The categorical trace on the left is defined because the global
operator $T_c(u)$ of [def-trf-global-operator] is a morphism of
$D^b_{\mathrm{fin}}(A)$, hence an endomorphism of a perfect complex,
by [lem-trf-global-operator-perfect]. With this, the
localization theorem [thm-trf-fixed-point-localization] gives

$$
\operatorname{tr}_A(T_c(u)\mid R\Gamma_c(X,K))
=\int_F\operatorname{Tr}_c(u).
$$

The component integration formula
[lem-trf-integration-component-sum] (applicable since each component
$\beta$, being closed in the proper $F$, is proper over $s$) rewrites
the right side as

$$
\sum_{\beta\in\pi_0(F)}
\int_\beta\bigl(\operatorname{Tr}_c(u)|_\beta\bigr).
$$

Each summand is $\operatorname{LT}_\beta(u)$ by
[def-trf-local-term], which proves the comparison.

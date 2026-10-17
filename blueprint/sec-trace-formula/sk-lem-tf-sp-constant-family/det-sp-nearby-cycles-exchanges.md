+++
id = "det-sp-nearby-cycles-exchanges"
kind = "lemma"
title = "Pullback and proper exchanges for nearby cycles"
+++
Let $S$ be a strictly henselian trait with a chosen geometric generic point $\bar\eta$ (for
instance the strict henselization of $\operatorname{Spec}k[t]_{(t)}$ for an algebraically closed
field $k$), let $\ell$ be invertible on $S$, and let $A$ be a finite commutative ring annihilated
by a power of $\ell$. For $\mathcal Y\to S$ separated of finite type, let $\bar{\mathcal Y}$ be its
pullback to the integral closure $\bar S$ of $S$ in the chosen separable closure of its fraction
field, let $\bar i$ and $\bar j$ be the inclusions of the special fibre $\mathcal Y_s$ and of the
geometric generic fibre $\mathcal Y_{\bar\eta}$ into $\bar{\mathcal Y}$, and put

$$
R\Psi_{\mathcal Y}(L)=\bar i^{*}R\bar j_*L_{\bar\eta}
\qquad(L\in D^b_c(\mathcal Y_{\eta,\mathrm{\acute et}},A)).
$$

Let $f\colon\mathcal Y'\to\mathcal Y$ be a morphism of separated finite-type $S$-schemes.

1. **(Pullback exchange.)** Restricting to the special fibre the base-change map
   $\bar f^*R\bar j_*\to R\bar j'_*f_{\bar\eta}^*$ of the square formed by $\bar f$ and the
   generic-fibre inclusions gives a natural transformation of functors
   $D^b_c(\mathcal Y_{\eta,\mathrm{\acute et}},A)\to D(\mathcal Y'_{s,\mathrm{\acute et}},A)$

   $$
   f_s^*R\Psi_{\mathcal Y}\longrightarrow R\Psi_{\mathcal Y'}f_\eta^*,
   $$

   which is invertible when $f$ is smooth.
1. **(Proper exchange.)** If $f$ is proper, proper base change for $\bar f$ along $\bar i$ and the
   identification $R\bar f_*R\bar j'_*=R\bar j_*Rf_{\bar\eta*}$ give an isomorphism of functors
   $D^b_c(\mathcal Y'_{\eta,\mathrm{\acute et}},A)\to D(\mathcal Y_{s,\mathrm{\acute et}},A)$

   $$
   Rf_{s*}R\Psi_{\mathcal Y'}\xrightarrow{\sim}R\Psi_{\mathcal Y}Rf_{\eta*}.
   $$

Both exchanges are compatible with composition of morphisms.

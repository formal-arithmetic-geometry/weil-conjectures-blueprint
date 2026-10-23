+++
id = "det-sp-constant-family-vanishing"
kind = "lemma"
title = "The specialization unit of a constant family is invertible"
order = 3570
uses = ["det-sp-nearby-cycles-exchanges"]
+++
Let $k$ be algebraically closed, $A$ a finite commutative ring annihilated by a power of a prime
$\ell$ invertible in $k$, and $S$ the strict henselization of $\operatorname{Spec}k[t]_{(t)}$, with
nearby cycles $R\Psi$ and pullback and proper exchanges as in [det-sp-nearby-cycles-exchanges].
For a separated finite-type $k$-scheme $Y$ and $L\in D^b_c(Y_{\mathrm{\acute et}},A)$, let
$\sigma_Y(L)\colon L\to R\Psi_{Y\times S}(L_\eta)$ be the restriction to the special fibre $Y$ of
the adjunction unit of $\bar j$ on the pullback of $L$, and let
$B_Y(L)=\operatorname{cofib}(\sigma_Y(L))$, formed in a derived enhancement. Then $B_Y(L)=0$, that
is, $\sigma_Y(L)$ is an isomorphism, naturally in $L$. Moreover

$$
B_Y(Rf_*L')\simeq Rf_*B_{Y'}(L')\quad(f\text{ proper}),\qquad
B_{Y'}(f^*L)\simeq f^*B_Y(L)\quad(f\text{ smooth}),
$$

that is, $\sigma$ is compatible with the proper and the smooth exchanges.

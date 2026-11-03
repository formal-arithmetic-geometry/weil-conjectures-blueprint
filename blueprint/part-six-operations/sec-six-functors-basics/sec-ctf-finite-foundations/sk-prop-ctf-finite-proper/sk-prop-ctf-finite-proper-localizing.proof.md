+++
kind = "proof"
of = "det-ctf-finite-proper-localizing"
+++
*Étale statements.* On $\D(X_{\mathrm{ét}},A)$: $Rp_*$ preserves $\Dctf$ by [det-ctf-finite-proper-tor]; it preserves
arbitrary direct sums of unbounded complexes by [lem-amb-proper-coproducts] (finite cohomological dimension,
Stacks, Tag 0F0D). Proper base change $g^*Rp_*K\to Rp'_*g'^*K$ holds for bounded below $K$
([sk-thm-properbasechange]); for unbounded $K$, both sides commute with the truncation tower: by the uniform
bound $R^qp_*=0$ for $q>2d$ (and likewise for $p'$), $\mathcal H^q$ of either side only depends on
$\tau_{\geq q-2d-1}K$, which is bounded below, so the map is an isomorphism in each degree (equivalently
Stacks, Tag 0F0C). These $A$-linear statements follow from the abelian-group statements by forgetting
coefficients ([Stacks, Tag 0D6J](https://stacks.math.columbia.edu/tag/0D6J)).

*Transfer.* By [sk-prop-ctf-finite-comparison], $\nu^*$ identifies $\D(X_{\mathrm{ét}},A)=\Loc(\Dctf(X_{\mathrm{ét}},A))$ with
$\Loc(\Dctf(X,A))$, compatibly with $Rp_*$, $g^*$ and $j_!$ and with sums. So (1) and (2) hold on
$\Loc(\Dctf(-,A))$. In particular $Rp_*$ maps $\Dctf(X,A)$ into $\Dctf(Y,A)$, and maps $\Loc(\Dctf(X,A))$ into
$\Loc(\Dctf(Y,A))$ (it preserves the small subcategory and sums, so its localizing closure).

*Extension by zero.* $j_!$ is exact, left adjoint to $j^*$ (so preserves sums), and stalkwise it is either
the stalk of the input or zero; hence it preserves constructibility (add the closed complement as a stratum)
and finite Tor amplitude. Composing with (1) gives the claims for $Rp_*j_!$.

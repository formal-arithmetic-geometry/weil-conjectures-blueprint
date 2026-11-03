+++
kind  = "proof"
of    = "lem-sfb-point-upper-star-tensor"
+++
Both tensor products are sheafified objectwise tensor products, and
sheafification is monoidal. Also,
$\mathrm{sheafify}\circ\operatorname{Lan}_{u^{\mathrm{op}}}$ inverts
sheafification. So it suffices to show that $\operatorname{Lan}_{u^{\mathrm{op}}}$
commutes with the objectwise tensor product of presheaves.

At $V$, the Kan extension is a colimit over the opposite of the category of
pairs $(S,\ V\to u(S))$. That category is cofiltered because $u$ preserves
finite limits ([lem-sfb-profinite-to-proetale-finite-limits]), so the colimit
is filtered. In a filtered category the diagonal is cofinal, and $\otimes_\Z$
commutes with filtered colimits in each variable. Hence
$$
\colim\,(F(S)\otimes G(S))\cong\colim F(S)\otimes\colim G(S).
$$
This isomorphism is the comparison map.

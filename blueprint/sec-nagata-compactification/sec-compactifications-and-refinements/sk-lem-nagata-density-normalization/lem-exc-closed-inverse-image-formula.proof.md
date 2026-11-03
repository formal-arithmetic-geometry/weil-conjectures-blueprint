+++
kind  = "proof"
of    = "lem-exc-closed-inverse-image-formula"
+++
Work with sheaves on the bases by [lem-weil-pbc-ind-etale-basis]. Underived
direct image is $(i_*G)(W)=G(u(W))$. A morphism $F\to i_*G$ therefore gives
$F(v(V))\to G(u(v(V)))=G(V)$, hence $P_F\to G$. Conversely $P_F\to G$
defines
$$
 F(W)\longrightarrow F(v(u(W)))\longrightarrow G(u(W)),
$$
where the first arrow is restriction along the counit $v(u(W))\to W$ of
[def-exc-closed-site-lift], [lem-exc-closed-site-adjunction]. The triangle
identities, or evaluation of these formulas, show that the two constructions
are inverse. Sheafification does not change maps to $G$. Thus $P_F^a$ has
the adjunction that defines $i^*$ in the pro-etale operations, proving the
formula.

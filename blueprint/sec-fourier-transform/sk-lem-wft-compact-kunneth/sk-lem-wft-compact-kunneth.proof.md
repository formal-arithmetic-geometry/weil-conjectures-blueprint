+++
kind  = "proof"
of    = "sk-lem-wft-compact-kunneth"
+++
Let $u:X\times_SY\to X$ and $v:X\times_SY\to Y$ be the projections.
By proper base change ([det-prop-sf-cbc]), $Ru_!v^*L\simeq a^*Rb_!L$. Applying
the projection formula ([sk-thm-sf-package]) first to $u$ and then to $a$, we
get

$$
 Rc_!(u^*K\otimes v^*L)
  \simeq Ra_!(K\otimes a^*Rb_!L)
  \simeq Ra_!K\otimes Rb_!L.
$$

This isomorphism is natural and compatible with Weil structures
([sk-def-sf-weil-complexes]), because base change and the projection formula
are. For smooth maps, the compatibility with traces ([sk-def-sp-trace])
follows from the composition law for the counits
([sk-prop-sp-trace-composition]), together with the base change of the
purity isomorphism ([sk-prop-sp-purity-bc]).

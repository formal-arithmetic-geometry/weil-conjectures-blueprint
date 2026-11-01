+++
kind  = "proof"
of    = "lem-pur-support-localization-triangle"
+++
By [lem-pur-support-exact], the three complexes in
[def-pur-support-triangle] form a short exact sequence. Its cone
triangle is distinguished, and the cone-to-quotient quasi-isomorphism
identifies its third term with $j_*j^*I(K)$.

The sheaf functor $s^!$ of [def-pur-flasque-support] is right
adjoint to $s_*$: every map $s_*N\to M$ has image supported on
$Z$, hence factors uniquely through $\mathcal G_ZM$, giving
$\operatorname{Hom}_X(s_*N,M)=\operatorname{Hom}_Z(N,s^!M)$.
Since $s_*$ is exact for a closed immersion, the right derived
functor $Rs^!$ of $s^!$ on $D^+$, computed on injective resolutions by
$s^!I(K)$, is right adjoint to $s_*$ on $D^+$; on the domain of the
exceptional inverse image of [def-weil-exceptional-inverse-image],
uniqueness of right adjoints identifies the two.
The restriction $j^*$ preserves injectives because its left adjoint
$j_!$ is exact by [def-weil-open-closed-recollement].
Thus $j_*j^*I(K)$ computes $Rj_*j^*K$.

The comparison theorem for the resolutions of
[def-sp-kinjective-bridge] and the natural kernel and
quotient maps give canonicality and functoriality in the sense of
[def-pur-triangle-meaning]. Finally, along an etale map the site
is localized: the support kernel and the open direct image are
computed on the same objects after restriction. Etale restriction
preserves injectives, since its extension-by-zero left adjoint is
exact. Applying this to the displayed injective model identifies its
derived pullback with the model for the base-changed pair, proving
etale base-change compatibility.

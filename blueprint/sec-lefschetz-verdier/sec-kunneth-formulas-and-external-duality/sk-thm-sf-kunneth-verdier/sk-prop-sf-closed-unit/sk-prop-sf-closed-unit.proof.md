+++
kind  = "proof"
of    = "sk-prop-sf-closed-unit"
+++
The direct image $i_*$ of a closed immersion is exact, and so is $i^*$; the
counit $i^*i_*\to\operatorname{id}$ is an isomorphism — on geometric stalks
over $Z$ the two sides agree. Since both functors are exact they need no
deriving, so on the unbounded derived categories $Li^*Ri_*=i^*i_*\cong
\operatorname{id}$ and the counit of $Li^*\dashv Ri_*$ is an isomorphism;
hence $Ri_*:D(Z_{\mathrm{et}},\mathcal A)\to D(X_{\mathrm{et}},\mathcal A)$
is fully faithful. Since $i$ is proper, $Ri_!\cong Ri_*$ (computed with the
compactification $(\operatorname{id}_Z,i)$), so $Ri_!$ is fully faithful too,
and $Ri^!$ is its right adjoint ([lem-exc-closed-ambient], unconditional on
the ordinary étale derived categories). For every $P\in D(Z_{\mathrm{et}},
\mathcal A)$ the composite

$$
\operatorname{Hom}(P,Q)\xrightarrow{\ (\eta_i^!)_*\ }
\operatorname{Hom}(P,Ri^!Ri_!Q)\cong\operatorname{Hom}(Ri_!P,Ri_!Q)
$$

is the action of $Ri_!$ on morphisms, which is bijective by full
faithfulness; so $(\eta_i^!)_*$ is bijective for every $P$, and by Yoneda
$\eta_i^!:Q\to Ri^!Ri_!Q$ is an isomorphism.

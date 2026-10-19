+++
kind = "proof"
of = "det-tf-contracting-vanishing"
uses = ["det-tf-cone-zero-sections", "det-tf-fixed-deformation-points", "det-tf-sp-trace-morphism", "det-tf-sp-theta-open-constant", "det-sp-zero-section-vanishing"]
+++
Deform $c$ to the normal cones: the lifted legs
$\widetilde c_i:\mathcal D_EC\to\mathcal D_ZX$, base changed from $T=\operatorname{Spec}k[t]_{(t)}$
to its strict henselization $S$, form a correspondence over $S$ whose generic fibre is $c$ and
whose special fibre is $\gamma=(\gamma_1,\gamma_2):N_EC\to N_ZX\times N_ZX$. Let $\widetilde F$ be
its fixed scheme. By [det-tf-fixed-deformation-points],
$\widetilde F_{\mathrm{red}}=(F_c\times S)_{\mathrm{red}}$.

Specialize $u$ along this family. The nearby cycles of the pullback of $K$ to the generic fibre
of $\mathcal D_ZX$ form the specialization $\operatorname{Sp}_{X,Z}(K)$ on $N_ZX$, and by
[det-tf-sp-trace-morphism] the trace class of the specialized morphism
$u_s:\gamma_2^*\operatorname{Sp}_{X,Z}(K)\to\gamma_1^!\operatorname{Sp}_{X,Z}(K)$ is
$\operatorname{sp}_{\widetilde F}(\operatorname{Tr}_c(u))=\theta_{\widetilde F}S_{\widetilde F}(\operatorname{Tr}_c(u))\sigma_{\widetilde F}$.

Verdier's zero-section theorem [det-sp-zero-section-vanishing] identifies the restriction of $\operatorname{Sp}_{X,Z}(K)$ to the
zero section $Z\subset N_ZX$ with the restriction of $K$ to $Z$. Together with nilpotent invariance
for $Z_{\mathrm{red}}\to Z$ and $i^*K=0$, this gives $\operatorname{Sp}_{X,Z}(K)|_Z=0$. By
[det-tf-cone-zero-sections] (2), $\gamma_2$ maps $N_EC$ set-theoretically into the zero section,
and nilpotent invariance gives $\gamma_2^*\operatorname{Sp}_{X,Z}(K)=0$. So $u_s$ has zero source,
and its trace class is zero.

Hence $\operatorname{sp}_{\widetilde F}(\operatorname{Tr}_c(u))=0$. Since
$\widetilde F_{\mathrm{red}}=F_c\times S$ up to reduction, [det-tf-sp-theta-open-constant]
identifies $\operatorname{sp}_{\widetilde F}$ with the identity, under the constant-family and
nilpotent-invariance identifications. It is therefore injective, and $\operatorname{Tr}_c(u)=0$.

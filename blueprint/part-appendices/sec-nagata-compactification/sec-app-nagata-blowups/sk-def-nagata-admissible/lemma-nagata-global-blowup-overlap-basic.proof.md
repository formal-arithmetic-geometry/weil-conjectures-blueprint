+++
kind  = "proof"
of    = "lemma-nagata-global-blowup-overlap-basic"
uses = ["prop-nagata-affine-blowup-restrict"]
+++
Put $A=A_V=\Gamma(V,\mathcal O_X)$ and $B=A_W=\Gamma(W,\mathcal O_X)$.
Since $W=D(s)$ is a basic open of the affine scheme $V$, the restriction
$\varphi\colon A\to B$ is a localization of $A$ away from $s$, and under
$V\cong\operatorname{Spec}A$, $W\cong\operatorname{Spec}B$ the inclusion
$W\subseteq V$ is $\operatorname{Spec}\varphi$. Since $\mathcal I$ is
quasi-coherent, $I_W=\Gamma(V,\mathcal I)_s=I_VB$. Hence the transition map
$\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)$ of
[def-nagata-global-blowup-local-model] is the morphism
$r_\varphi\colon\operatorname{Bl}_{I_VB}(\operatorname{Spec}B)\to
\operatorname{Bl}_{I_V}(\operatorname{Spec}A)$ of
[def-nagata-affine-blowup-restriction-map], and the structure morphisms are
those of the two affine blow-ups. By [prop-nagata-affine-blowup-restrict]
the square formed by $r_\varphi$, the two structure morphisms and
$\operatorname{Spec}B\to\operatorname{Spec}A$ is cartesian; transporting
along $V\cong\operatorname{Spec}A$ and $W\cong\operatorname{Spec}B$ gives
the claim.

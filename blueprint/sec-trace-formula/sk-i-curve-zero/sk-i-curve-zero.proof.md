+++
kind = "proof"
of = "sk-i-curve-zero"
uses = ["sk-lem-tf-curve-restriction-zero", "sk-lem-tf-curve-supported-pairing", "sk-lem-tf-fixed-points"]
+++
By [sk-lem-tf-curve-restriction-zero] the supported restriction
in [sk-lem-tf-curve-supported-pairing] is zero in $D(A)$, so its
composite with evaluation and integration, which is the proétale
local term, is zero in $A$.

*Complement.* Since $X$ is smooth of relative dimension one, so is $X_0$, and
$\varphi_m$ is a morphism $\Phi_m^*K\to K$ with $\Phi_m=\Phi_X^m$. By [sk-lem-tf-fixed-points]
the fixed scheme $\Fix(1,\Phi_m)$ is a finite disjoint union of reduced points, so $B$ is
the component $\{\bar x\}$ and $\LT_B(\varphi_m)=\LT_{\bar x}(\varphi_m)$. The assertion is
the case $v=\varphi_m$, $y=\bar x$ of the corollary.

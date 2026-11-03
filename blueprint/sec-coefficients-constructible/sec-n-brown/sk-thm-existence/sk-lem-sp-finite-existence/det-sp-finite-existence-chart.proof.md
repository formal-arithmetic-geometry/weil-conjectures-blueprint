+++
kind = "proof"
of = "det-sp-finite-existence-chart"
uses = ["cor-pur-affine-space-purity", "lem-pur-co-smooth-etale-locality", "lem-amb-etale-adjoint-locality", "cor-amb-affine-space-adjunction", "det-sf-mate-open-restriction"]
+++
*(1)* For separated étale $e$ of finite type, extension by zero $e_!$ is exact
on sheaves and left adjoint to $e^*$ ([lem-amb-etale-adjoint-locality]). It
agrees with the compactly supported direct image $Re_!$: by Zariski's main
theorem $e$ factors as an open immersion $j_e$ followed by a finite morphism
$\pi$, and $R\pi_*j_{e!}=\pi_*j_{e!}$ is extension by zero, its geometric stalks
being $(e_!F)_{\bar y}=\bigoplus_{e(\bar x)=\bar y}F_{\bar x}$. Uniqueness of
right adjoints gives $e^!\simeq e^*$ (so $\omega_e\simeq\Lambda_n$, as in
[lem-pur-co-smooth-etale-locality]). The counit is the adjunction counit
$e_!e^*F\to F$, which on stalks is the sum map.

*(2)* This is the affine-space adjunction [cor-amb-affine-space-adjunction],
with counit the composite of $d$ affine-line counits; at the constant sheaf it
is the integration isomorphism $\operatorname{Tr}_{p_d}$, and in general it is
$1\otimes\operatorname{Tr}_{p_d}$ after the projection formula. The induced
comparison $p_d^*K(d)[2d]\to p_d^!K$ is the affine-space purity isomorphism of
[cor-pur-affine-space-purity].

*(3)* By [det-sf-mate-open-restriction], $j^*f^!\simeq(fj)^!$, and
$(fj)^!=(p_de)^!\simeq e^!p_d^!$ by the composition isomorphism, with counit
the composite of the two counits. By (1) and (2) the composite $Rp_{d!}\circ e_!$ is left
adjoint to $e^*p_d^*(-)(d)[2d]$, with counit
$\tau_K\circ Rp_{d!}(\sigma)$. Uniqueness of right adjoints (with their counits)
gives the unique counit-preserving isomorphism
$j^*f^!K\simeq e^*p_d^*K(d)[2d]$, natural in $K$.

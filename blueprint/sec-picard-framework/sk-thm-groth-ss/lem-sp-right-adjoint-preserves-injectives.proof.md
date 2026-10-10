+++
kind  = "proof"
of    = "lem-sp-right-adjoint-preserves-injectives"
+++
By [def-sp-injective-resolutions], $I\in\mathcal B$ is injective iff for
every monomorphism $N\hookrightarrow N'$ in $\mathcal B$ the map

$$
 \operatorname{Hom}_{\mathcal B}(N',I)\longrightarrow
 \operatorname{Hom}_{\mathcal B}(N,I)
$$

is surjective. By the adjunction

$$
 \operatorname{Hom}_{\mathcal B}(uM,N)\cong
 \operatorname{Hom}_{\mathcal A}(M,u_*N),
$$

the injectivity of $u_*I$ is equivalent to the surjectivity of
$\operatorname{Hom}(uM',I)\to\operatorname{Hom}(uM,I)$ for every monomorphism
$M\hookrightarrow M'$ in $\mathcal A$; this holds because $u$ is exact, hence
preserves monomorphisms, and $I$ is injective.

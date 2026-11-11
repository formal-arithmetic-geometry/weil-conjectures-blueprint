+++
kind = "proof"
of = "theorem-classical-sheaves-essential-image"
order = 116
uses = ["proposition-etale-implications", "proposition-pro-etale-affines-form-basis"]
+++
A left adjoint is fully faithful exactly when its unit is an isomorphism,
and the essential image is then the set of objects on which the counit is
an isomorphism. We check both on pro-étale affines, where
(2.6) computes $\nu_X^*$.

Evaluating (2.5) on an étale object
$V$ gives $F(V)$, so $F\xrightarrow{\sim}\nu_{X,*}\nu_X^*F$, which proves
full faithfulness. Moreover,
every $\nu_X^*F$ is classical by (2.6).
Conversely, let $G$ be classical. On a pro-étale affine the counit
$\nu_X^*\nu_{X,*}G\to G$ is

$$
(\nu_X^*\nu_{X,*}G)(U)
=\varinjlim_iG(U_i)\longrightarrow G(U),
$$

which is an isomorphism by (2.4). Since
pro-étale affines form a covering basis
(Proposition [proposition-pro-etale-affines-form-basis]), the counit is an
isomorphism of sheaves.
